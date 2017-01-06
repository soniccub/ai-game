import random
import math

### This makes small networks which sensors are sent to.
### Brain blocks hold a network
### Each brain has a set of sensors that activate it
### When a sensor activates or changes the network is run again
### brain control center has options to change sensor settings on old networks
### Settings only changed if world has adding during life and not normal evolution



class Network():
    def __init__(self, upper, inputs, outputs, length):

        ### Setting inputs and outputs of the newtork
        self.upper = upper
        self.inputs = inputs
        self.outputs = outputs

        self.length = length

        ### [beginning,,end,length]
        self.size = [self.inputs, self.outputs, self.length]
        self.neurons = []
        self.network_creation()


    def signal(self, current_row, next_row, inputs):
        if current_row.output:
            return inputs
        temp_input = []
        new_next_row = []


        for i in next_row:
            temp_input.append(0)

        for i in range(len(next_row)):
            single_input = current_row[i].input(inputs[i])
            temp_input = [x + y for x, y in zip(temp_input, single_input)]

        ### To get the list of neurons for next run-through
        for i in next_row[0].connections:
            new_next_row.append(i[0])

        self.output_list = []


        return self.signal()

    def network_creation(self):
        ### Size 0 in inputs
        temp_list = []
        temp_list.append([])
        ### Initializes last neurons
        for i in range(len(self.size[1])):
            temp_list[0].append(Neuron(self,[i, self.length], [None], True))

        ### Defines all middle ones, ignores first two and last
        i = self.size[2]
        while i > 1:


            temp_list.append([])

            for ii in self.size[1]:
                #print(temp_list)
                temp_list[self.length-i+1].append(Neuron(self, [ii, i], temp_list[self.length-i]))
            i -= 1
        ### The first row, which may have a different size than the others.
        for i in self.size[0]:
            temp_list[1].append(Neuron(self,[i, 0], [temp_list[len(temp_list)-1]]))

        i = len(temp_list)-1
        while i > -1:
            self.neurons.append(temp_list[i])
            i += -1






    def run_network(self, inputs):


        return self.signal(self.neurons[0],self.neurons[1], inputs)



    def output(self, output):
        self.output_list.append(output)

        if len(self.output_list) == len(self.outputs):


            return self.output_list




class Neuron():
    def __init__(self, network, position, connections, output=False):
        ### Connections it has
        ### [neuron, weight]
        self.connections = connections


        if not output:
            self.set_wieghts()
        self.network = network
    def set_wieghts(self):
        self.connection_weights = []
        for i in range(len(self.connections)):
            self.connection_weights.append([self.connections[i],random.randrange(200)/100])
            print(self.connection_weights)




    def input(self, input):
        output = []
        if not self.output:
            for i in self.connections:
                output.append([i[1] * input])
        else:




            self.out_put(input)

    def out_put(self, output):
        self.network.output(output)



object = Network([2,2,2,2,2],[2,2,2,2,2],20)