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
        
        self.direction = self.creature.direction
        for block in self.creature.blocks:
            if block.activatable:
                self.active_blocks.append(block)


class Brain:
    def __init__(self, creature, abilities, brain_size):
        self.creature = creature
        self.ability_list = abilities
        self.brain_size = brain_size

        self.network_length = brain_size[0]
        self.network_height = brain_size[1]

        self.size_upkeep_ratio = self.creature.creatures.main.brain_size_food_ratio


    def upkeep(self):
        self.creature.food -= self.brain_size[0] * self.brain_size[1] * self.size_upkeep_ratio


    def network_run(self):


        input_list = []
        position_angle_list = []


        for i in self.creature.sensors:
            sense_list = i.sense

            input = 0
            sensor_input = []
            for iii in range(i.sense_detail):
                detail_input = 0
                for ii in sense_list:
                    if iii * (180/i.sense_detail) >= ii[2] and (iii+1) * (180/i.sense_detail) <= ii[2] :
                        if (i.max_sense_distance - math.sqrt((ii[2][0]**2 + ii[2][1]**2)))/i.max_sense_distance > detail_input:
                            detail_input = (i.max_sense_distance -
                                             math.sqrt((ii[2][0]**2 + ii[2][1]**2)))/i.max_sense_distance
                ### Only senses the closest object and puts that into the network
                ### Splits it up in equal amounts of degrees based on the "level" of the sensor
                sensor_input.append(detail_input)






    def output(self, output):
        self.creature.activate(output)

    def network_create(self,):
        ### In order : sensors as they appear in list in order : food level : blocks in order (touch)

        self.network = network.Network(self, [3 + len(self.creature.blueprint) + len(self.creature.sensors) * self.creature.sensors.sense_detail, self.creature.abilities ])


