import math
import blocks.network

### Brain - not actual block
### Bigger brain = more resource drain
### Adds dorect connection to networks
### Controls networks and acts as overall brain
### More add




class BrainBlock():
    color = "#FFB6C1"
    activatable = False
    type = "brain"

    def __init__(self, creature, position, coords_on_creature, brain_size):
        self.active_blocks = []
        self.creature = creature
        self.position = position
        self.coords = coords_on_creature
        self.brain_size = brain_size
        self.y_edges = []
        self.x_edges = []
        self.food_storage = 25


        self.direction = self.creature.direction
        for block in self.creature.blocks:
            if block.activatable:
                self.active_blocks.append(block)

    def upkeep(self):
        self.creature.food -= 50
    def input(self, inputs):
        self.brain.network_run(inputs)

    def create_brain(self):
        self.brain = Brain(self.creature, self.creature.active_block_list, self.brain_size)


class Brain:
    def __init__(self, creature, abilities, brain_size):
        self.creature = creature
        self.ability_list = abilities
        self.brain_size = brain_size

        self.network_length = brain_size
        self.network_create()




    def upkeep(self):
        self.creature.food -= self.brain_size[0] * self.brain_size[1] * self.size_upkeep_ratio


    def network_run(self, input_list):


        position_angle_list = []
        sense_list = []
        for i in self.creature.sensors:
            sense_list.append(i.sense())



            sensor_input = []
            #print(i.sense())
        for iii in range(self.creature.sensors[0].sense_detail):
            detail_input = 0
                #print(sense_list)
            for ii in sense_list:
                for i in ii[0]:


                    #print(ii)
                    if iii * (180 / self.creature.sensors[0].sense_detail) <= i[0] and (iii + 1) * (180 / self.creature.sensors[0].sense_detail) >= i[0]:
                        if (self.creature.sensors[0].max_sense_distance - math.sqrt((i[1][0]**2 + i[1][1]**2)))/self.creature.sensors[0].max_sense_distance > detail_input:
                            detail_input = self.creature.sensors[0].max_sense_distance - math.sqrt((i[1][0]**2 + i[1][1]**2))/self.creature.sensors[0].max_sense_distance

                ### Only senses the closest object and puts that into the network
                ### Splits it up in equal amounts of degrees based on the "level" of the sensor
            input_list.append(detail_input)
            #print(0,detail_input)
        self.creature.activate(self.network.run_network(input_list))


    def output(self, output):
        self.creature.activate(output)


    def network_create(self):
        ### In order : sensors as they appear in list in order : food level : blocks in order (touch)

        self.network = blocks.network.Network(self, 1 + len(self.creature.blocks) + len(self.creature.sensors) * self.creature.sensors[0].sense_detail, self.creature.active_block_list)







