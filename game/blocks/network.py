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
        print(0,self.neurons)
        if self.neurons[current_row][0].output:
            return inputs
        temp_input = []
        for i in range(len(self.neurons[current_row + 1])):
            temp_input.append(0)
        for i in range(len(self.neurons[current_row])):
            add_input = self.neurons[current_row][i].input(inputs[i])
            for ii in range(len(temp_input)):

                #print(0, add_input, temp_input)
                temp_input[ii] += add_input[ii]






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
        ### Initializes last neurons
        for i in range(len(self.size[1])):
            temp_list[0].append(Neuron(self, [i, len(self.outputs)], [None], True))

        ### Defines all middle ones, ignores first two and last
        i = self.size[2]
        while i > 1:

            temp_list.append([])

            for ii in self.size[1]:
                # print(temp_list)
                temp_list[self.length - i + 1].append(Neuron(self, [ii, i], temp_list[self.inputs - i]))
            i -= 1
        ### The first row, which may have a different size than the others.
        for i in self.size:
            temp_list[1].append(Neuron(self, [i, 0], [temp_list[len(temp_list) - 1]]))

        i = len(temp_list) - 1
        while i > -1:
            self.neurons.append(temp_list[i])
            i += -1


class Neuron():
    def __init__(self, network, position, connections, output=False):
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
            print(self.connection_weights)

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




