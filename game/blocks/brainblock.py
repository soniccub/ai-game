

### Brain block
### Adds dorect connection to networks
### Controls networks and acts as overall brain
### More add




class BrainBlock():
    pass


class BrainBlockAction:
    def __init__(self, brain_block, abilities, brain_size):
        self.block = brain_block
        self.abilities = abilities
        self.brain_size = brain_size

        self.length_max = 50
        self.max_brain_size = 100

        self.length = int(self.brain_size/self.max_brain_size * self.length_max)

    def set_network(self):

        self.network = N.Network()




class BrainBlockStim():
    def __init__(self, block, sensors, abilities, brain_size):
        ### Each network is connected to a brain-type block
        ### Each brain-type block is part of a creature in the same way

        self.block = block

        ### Each creature has a network control if it has a brain block

        self.network_control = self.block.network_control

        ### Inputs to the network from the world around the creature

        self.sensors = sensors

        ### output of the network are an ability being called

        self.abilities = abilities
        ### Intel determines length of networks

        ### calculates length of the network
        self.brain_size = brain_size

        self.maxbrain_size = 100
        self.max_size = 20
        self.network_length = int(brain_size/self.maxbrain_size * self.max_size)

    def set_network(self):


        self.network = N.Network(self.sensors, self.abilities,self.network_length)


    def return_ability(self, inputs):
        ### This runs network and then
        self.network.run_network(inputs)

