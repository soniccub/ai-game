import math
### Upkeep is max 10 min 0.1
### Numbers picked on whim, calibrated soon?





### Stores small amount of food
### low upkeep
### Basic building block

class GenericBlock:
    color = "#d2b48c"
    type = "body"
    activatable = False

    def __init__(self, creature, block_position, blueprint_coords):

        self.creature = creature
        self.position = block_position
        self.coords = blueprint_coords
        if self.coords[0] == 0:
            if self.coords[1] > 0:
                self.direction = 90
            else:
                self.direction = 270

        elif self.coords[1] == 0:
            if self.coords[0] > 0:
                self.direction = 0
            else: self.direction = 180
        else:
            self.direction = math.atan(self.coords[1] / self.coords[0]) * 180 / math.pi
            if self.coords[0] < 0:
                self.direction += 180
            print(self.direction, self.coords)
        self.y_edges = []
        self.x_edges = []


    def upkeep(self):

        self.creature.food -= 0.1

    def activate(self, blank):
        pass


class StorageBlock:
    color = "#d20400"
    type = "body"
    activatable = False
    def __init__(self, creature, block_position,  blueprint_coords):
        self.creature = creature
        self.position = block_position
        self.coords = blueprint_coords
        if self.coords[0] == 0:
            if self.coords[1] > 0:
                self.direction = 90
            else:
                self.direction = 270

        elif self.coords[1] == 0:
            if self.coords[0] > 0:
                self.direction = 0
            else:
                self.direction = 180
        else:
            self.direction = math.atan(self.coords[1] / self.coords[0]) * 180 / math.pi
            if self.coords[0] < 0:
                self.direction += 180
        self.y_edges = []
        self.x_edges = []

    def upkeep(self):
        self.creature.food -= 0.5






### Vine blocks repeat a certian confirgeration of blocks over and over again, includes itself
### activates once enough food stored
### can include any block, including reproductive

class VineBlock:
    color = "#007f00"
    type = "body"
    activatable = True
    def __init__(self, creature, block_position,  blueprint_coords):
        self.creature = creature
        self.position = block_position
        self.coords = block_position
        if self.coords[0] == 0:
            if self.coords[1] > 0:
                self.direction = 90
            else:
                self.direction = 270

        elif self.coords[1] == 0:
            if self.coords[0] > 0:
                self.direction = 0
            else:
                self.direction = 180
        else:
            self.direction = math.atan(self.coords[1] / self.coords[0]) * 180 / math.pi
            if self.coords[0] < 0:
                self.direction += 180

        self.y_edges = []
        self.x_edges = []



    def upkeep(self):
        self.creature.food -= 3


### Grows a certian confirgertion off of it, once enough food is stored
### Only sensors, storage, and generic
### New field added to network, network must re-learn
class GrowthBlock:
    color = "#993f6c"
    type = "body"
    activatable = True
    def __init__(self, creature, blueprint, block_position, blueprint_coords):
        self.creature = creature
        self.blueprint = blueprint
        self.position = block_position
        self.coords = block_position
        if self.coords[0] == 0:
            if self.coords[1] > 0:
                self.direction = 90
            else:
                self.direction = 270
        elif self.coords[1] == 0:
            if self.coords[0] > 0:
                self.direction = 0
            else:
                self.direction = 180
        else:
            self.direction = math.atan(self.coords[1] / self.coords[0]) * 180 / math.pi
            if self.coords[0] < 0:
                self.direction += 180

        self.y_edges = []
        self.x_edges = []

    def upkeep(self):
        self.creature.food -= 3


### Once enough food is avialble makes a creature with blueprint of creature with it
### Can create growth and vine blocks for max reproductive effect
### new brain_block and network, must learn
class ReproductionBlock:
    color = "#ffa500"
    type = "body"
    activatable = True
    def __init__(self, creature, block_position,  blueprint_coords, blueprint):

        self.creature = creature
        self.blueprint = blueprint
        self.position = block_position
        self.coords = blueprint_coords
        if self.coords[0] == 0:
            if self.coords[1] > 0:
                self.direction = 90
            else:
                self.direction = 270

        elif self.coords[1] == 0:
            if self.coords[0] > 0:
                self.direction = 0
            else:
                self.direction = 180
        else:
            self.direction = math.atan(self.coords[1] / self.coords[0]) * 180 / math.pi
            if self.coords[0] < 0:
                self.direction += 180

        self.y_edges = []
        self.x_edges = []

    def upkeep(self):
        self.creature.food -= 6

    def activate(self, power):
        pass

class MoveBlock:
    color = "#00a500"
    type = "body"
    activatable = True

    def __init__(self, creature, block_position, blueprint_coords):

        self.creature = creature


        self.position = block_position
        self.coords = blueprint_coords
        self.y_edges = []
        self.x_edges = []
        if self.coords[0] == 0:
            if self.coords[1] > 0:
                self.direction = 90
            else:
                self.direction = 270
        elif self.coords[1] == 0:
            if self.coords[0] > 0:
                self.direction = 0
            else:
                self.direction = 180
        else:
            self.direction = math.atan(self.coords[1] / self.coords[0]) * 180 / math.pi
            if self.coords[0] < 0:
                self.direction += 180

    def upkeep(self):
        self.creature.food -= 2

    def activate(self, power):
        self.creature.food -= power
        self.creature.move(self.coords, power)
        #print(self.position, 10)





