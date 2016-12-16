### Upkeep is max 10 min 0.1
### Numbers picked on whim, calibrated soon?





### Stores small amount of food
### low upkeep
### Basic building block

class GenericBlock:
    color = "#d2b48c"
    type = "body"
    def __init__(self, creature, block_position, blueprint_coords):
        self.creature = creature
        self.position = block_position
        self.coords = blueprint_coords



    def upkeep(self):
        self.creature.food -= 0.1


    def draw(self):
        pass





### Allows creature to move
### Activated by brain block
### High upkeep while moving, lower while not
class MoveBlock:
    color = "#d2b48c"
    type = "body"
    def __init__(self, creature, position,  blueprint_coords):
        self.creature = creature
        self.active = False
        self.position = position
        self.coords = blueprint_coords

    def upkeep(self):
        if self.active:
            self.creature.food -= 7
        else:
            self.creature.food -= 1

    def draw(self):
        pass



### Stores large amount of food
### passive
### Low upkeep, higher than generic block
class StorageBlock:
    color = "#3f362a"
    type = "body"
    def __init__(self, creature, block_position,  blueprint_coords):
        self.creature = creature
        self.position = block_position
        self.coords = blueprint_coords

    def upkeep(self):
        self.creature.food -= 0.5

    def draw(self):
        pass


### Vine blocks repeat a certian confirgeration of blocks over and over again, includes itself
### activates once enough food stored
### can include any block, including reproductive

class VineBlock:
    color = "#007f00"
    type = "body"
    def __init__(self, creature, block_position,  blueprint_coords):
        self.creature = creature
        self.position = block_position
        self.coords = blueprint_coords


    def upkeep(self):
        self.creature.food -= 3

### Grows a certian confirgertion off of it, once enough food is stored
### Only sensors, storage, and generic
### New field added to network, network must re-learn
class GrowthBlock:
    color = "#993f6c"
    type = "body"
    def __init__(self, creature, blueprint, block_position, blueprint_coords):
        self.creature = creature
        self.blueprint = blueprint
        self.position = block_position
        self.coords = blueprint_coords

    def upkeep(self):
        self.creature.food -= 3

    def draw(self):
        pass
### Once enough food is avialble makes a creature with blueprint of creature with it
### Can create growth and vine blocks for max reproductive effect
### new brain_block and network, must learn
class ReproductionBlock:
    color = "#ffa500"
    type = "body"
    def __init__(self, creature, blueprint, block_position,  blueprint_coords):
        self.creature = creature
        self.blueprint = blueprint
        self.position = block_position
        self.coords = blueprint_coords

    def upkeep(self):
        self.creature.food -= 6

    def draw(self):
        pass



