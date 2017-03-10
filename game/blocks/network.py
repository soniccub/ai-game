import random
import math

### This makes small networks which sensors are sent to.
### Brain blocks hold a network
### Each brain has a set of sensors that activate it
### When a sensor activates or changes the network is run again
### brain control center has options to change sensor settings on old networks
### Settings only changed if world has adding during life and not normal evolution



class Network():
    def __init__(self, upper, inputs, outputs, length = 3):

        ### Setting inputs and outputs of the newtork
        self.upper = upper
        self.inputs = inputs
        self.outputs = outputs

        self.length = length


        ### [beginning,end,length]
        self.size = [self.inputs, self.outputs, self.length]
        self.neurons = []
        self.network_creation()


    def signal(self, current_row, inputs):
        if self.neurons[current_row][0].output:
            #print(inputs,current_row)
            return inputs
        temp_input = []
        for i in (self.neurons[current_row]):
            temp_input.append([0])

        for i in len(range(self.neurons[current_row])):
            temp_input[i] += self.neurons[current_row][i].input(inputs[i])







        next_row = current_row + 1
        return self.signal(next_row,  temp_input)



    def run_network(self, inputs):


        return self.signal(0, inputs)


    def output(self, output):
        self.output_list.append(output)

        if len(self.output_list) == len(self.outputs):


            return self.output_list

    def network_creation(self):
        ### Size 0 in inputs
        temp_list = []
        temp_list.append([])
        for i in range(len(self.size[1])):
            temp_list[0].append(Neuron(self, None, True))

        i = self.length
        while i > 0:
            temp_list.append([])
            for ii in range(self.size[0]):

                temp_list[self.length-i+1].append(Neuron(self, temp_list[self.length-i]))
            i -= 1
        even_temper_list = []
        even_temperestest_list = []
        for i in range(self.size[0]):

            even_temper_list.append(Neuron(self, temp_list[-1]))
        temp_list.append(even_temper_list)

        for i in temp_list:
            self.neurons.append(i)

        ### Initializes last neurons


class Neuron():
    def __init__(self, network, connections, output=False):
        ### Connections it has
        ### [neuron, weight]
        self.connections = connections

        self.output = output
        self.last_input = 0
        if not output:
            self.set_wieghts()
        self.network = network

    def set_wieghts(self):
        self.connection_weights = []
        for i in range(len(self.connections)):
            self.connection_weights.append([self.connections[i], random.randrange(201)/100])
    def input(self, input):
        output = []
        if not self.output:
            for i in self.connection_weights:
                output.append(i[1] * input)

        else:
            self.out_put(input)
        self.last_input = input
        return output

    def out_put(self, output):
        self.network.output(output)

    def change_weights(self):
        for i in range(self.connections):
            self.connections[i][1] += random.randrange(-5, 5, 1) / 100




