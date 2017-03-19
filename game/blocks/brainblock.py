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
        self.creature.food -= 2
        self.brain.network.mutate(self.creature.food, self.creature.food_level_max())

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





    def network_run(self, input_list):


        position_angle_list = []
        sense_list = []
        sensor_input = []
        for i in self.creature.sensors:
            sense_list.append(i.sense())
        for i in range(len(self.creature.sensors)):
            for ii in range(self.creature.sensors[i].sense_detail):
                detail_input = 0
                for iii in sense_list[i][0]:
                    if (ii * (180 / self.creature.sensors[i].sense_detail) - self.creature.sensors[i].sense_direction <= iii[0]) % 360 \
                            <= (-self.creature.sensors[i].sense_direction + (ii + 1) * (180 / self.creature.sensors[0].sense_detail)) % 360:
                        if 1 - math.sqrt((iii[1][0]**2 + iii[1][1]**2))/self.creature.sensors[i].max_sense_distance > detail_input:
                            detail_input = 1 - math.sqrt((iii[1][0]**2 + iii[1][1]**2))/self.creature.sensors[i].max_sense_distance

                sensor_input.append(detail_input)
                    ### Only senses the closest object and puts that into the network
                    ### Splits it up in equal amounts of degrees based on the "level" of the sensor











        self.creature.activate(self.network.run_network(sensor_input))


    def output(self, output):
        self.creature.activate(output)


    def network_create(self):
        ### In order : sensors as they appear in list in order : food level : blocks in order (touch)

        self.network = blocks.network.Network(self, 1 + len(self.creature.blocks) + len(self.creature.sensors) * self.creature.sensors[0].sense_detail, self.creature.active_block_list)

    def copy(self, new_creature):
        pass






