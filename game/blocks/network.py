import random
import math


### This makes small networks which sensors are sent to.
### Brain blocks hold a network
### Each brain has a set of sensors that activate it
### When a sensor activates or changes the network is run again
### brain control center has options to change sensor settings on old networks
### Settings only changed if world has adding during life and not normal evolution


class Network:
    def __init__(self, upper, inputs, outputs, length=3, connections=[]):

        ### Setting inputs and outputs of the newtork
        self.upper = upper
        self.inputs = inputs
        self.outputs = outputs

        self.length = length

        ### [beginning,end,length]
        self.size = [self.inputs, self.outputs, self.length]
        self.neurons = []
        self.network_creation(connections)

    def signal(self, current_row, inputs):
        if self.neurons[current_row][0].output:
            return inputs
        temp_input = []
        for i in (self.neurons[current_row - 1]):
            temp_input.append(0)

        for i in range(len(self.neurons[current_row])):
            single_input = self.neurons[current_row][i].input(inputs[i])
            for ii in range(len(temp_input)):
                temp_input[ii] += single_input[ii]


        next_row = current_row + 1
        return self.signal(next_row, temp_input)

    def run_network(self, inputs):

        return self.signal(0, inputs)

    def output(self, output):
        self.output_list.append(output)

        if len(self.output_list) == len(self.outputs):
            return self.output_list

    def network_creation(self, connection=[]):

        ### Size 0 in inputs
        temp_list = []
        temp_list.append([])
        for i in range(len(self.size[1])):
            temp_list[0].append(Neuron(self, None, True, True))

        i = self.length-2
        while i > 0:
            temp_list.append([])
            for ii in range(self.size[0]):
                temp_list[i].append(Neuron(self, temp_list[i-1], True))
            i -= 1
        even_temper_list = []
        for i in range(self.size[0]):
            even_temper_list.append(Neuron(self, temp_list[self.length-2]))
        temp_list.append(even_temper_list)

        for i in range(len(temp_list)):
            self.neurons.append(temp_list[self.length-i-1])


        ### Initializes last neurons
        if len(connection) != 0:
            for i in range(len(self.neurons)):
                self.neurons[i].set_copy_weights(connection[i])

    def add_input(self, input_position):
        for i in range(self.length):
            if not i == self.length:
                self.neurons[i].insert(input_position, Neuron(self, self.neurons[i + 1]))
        for i in range(len(self.neurons)):
            for ii in range(len(self.neurons[i])):
                if i != self.length and i != self.length - 1:
                    self.neurons[i][ii].connections.insert(input_position, self.neurons[i][input_position])
                    self.neurons[i][ii].connections.insert(input_position, random.randrange(201) / 100)
                    self.neurons[i][ii].output_averages.insert(input_position, 0.5)

    def add_output(self, output_position):
        self.neurons[self.length].insert(output_position, Neuron(self, None, True))
        for i in self.neurons[self.length - 1]:
            i.connection_weights.insert(output_position, random.randrange(201) / 100)

    def running_average_average(self):
        avg = [0, 0]
        for i in self.neurons:
            for ii in i:
                avg[0] += ii.input_running_avg
                avg[1] += 1

        avg = avg[0] / avg[1]
        return avg

    def mutate(self, last_food):
        running_avg_avg = self.running_average_average()
        for i in self.neurons:
            for ii in i:
                if random.randrange(last_food) > 25:
                    if ii.input_running_avg > random.randrange(
                            201) / 100 + running_avg_avg / 2 or ii.input_running_avg < random.randrange(
                            201) / 100 + running_avg_avg / 2:
                        ii.change_weights()
                elif random.randrange(last_food) > 50:
                    if abs(ii.input_running_avg - running_avg_avg) / running_avg_avg < 0.1:
                        ii.change_weights()

    def copy(self):
        copy_list = []
        for i in self.neurons:
            for ii in i:
                copy_list.append(ii.connection_weights)

    def set_copy(self, weights, mutation=False):

        for i in range(len(self.neurons)):
            for ii in range(len(self.neurons[i])):
                self.neurons[i][ii].set_copy_weights(weights[i + ii])

        if mutation:
            # Mutation = [output/input, position] if not false
            # output = 1 input = 0
            if mutation[0] == 0:
                for i in len(range(self.neurons)):
                    if not i == len(self.neurons):
                        self.neurons[i].insert(mutation[1], Neuron(self, self.neurons[i+1]))
                for i in len(range(self.neurons)):
                    for ii in len(range(self.neurons[i])):
                        if i != len(self.neurons):
                            self.neurons[i][ii].connection_weights.insert(mutation[1], random.randrange(0, 200) / 100)

            elif mutation[0] == 1:
                self.neurons[-1].insert(mutation[1], Neuron(self, None, True))
                for i in range(len(self.neurons[-2])):
                    self.neurons[-2][i].connection_weights.insert(mutation[-2], random.randrange(0,200)/100)










class Neuron:
    def __init__(self, network, connections, output=False, connection_weights=False):
        ### Connections it has
        ### [neuron, weight]


        self.connections = connections


        self.connection_weights = []
        self.output = output
        self.last_input = 0
        if not output and not connection_weights:
            self.set_wieghts()
        self.network = network
        self.output_averages = []

        self.input_running_avg = 1

    def set_copy_weights(self, weights):
        self.connection_weights = weights

    def set_wieghts(self):
        for i in range(len(self.connections)):
            self.connection_weights.append(random.randrange(201) / 100)

    def input(self, input):
        output = []
        self.input_running_avg += (self.input_running_avg - input) / 5000

        if not self.output:
            for i in range(len(self.connection_weights)):
                output.append(self.connection_weights[i] * input)

        else:
            self.out_put(input)
        self.last_input = input
        return output

    def out_put(self, output):
        self.network.output(output)

    def change_weights(self):

        for i in range(len(self.connection_weights)):
            self.connection_weights[i] += random.randrange(-5, 5, 1) / 100
