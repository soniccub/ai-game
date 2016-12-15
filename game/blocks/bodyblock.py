### Upkeep is max 10 min 0.1
### Numbers picked on whim, calibrated soon?





### Stores small amount of food
### low upkeep
### Basic building block
class GenericBlock:
    def __init__(self, creature):
        self.creature = creature

    def upkeep(self):
        self.creature.food -= 0.1

### Allows creature to move
### Activated by brain block
### High upkeep while moving, lower while not
class MoveBlock:
    def __init__(self, creature):
        self.creature = creature
        self.active = False

    def upkeep(self):
        if self.active:
            self.creature.food -= 7
        else:
            self.creature.food -= 1



### Stores large amount of food
### passive
### Low upkeep, higher than generic block
class StorageBlock:
    def __init__(self, creature):
        self.creature = creature

    def upkeep(self):
        self.creature.food -= 0.5



### Vine blocks repeat a certian confirgeration of blocks over and over again, includes itself
### activates once enough food stored
### can include any block, including reproductive

class VineBlock:
    def __init__(self, creature):
        self.creature = creature


    def upkeep(self):
        self.creature.food -= 3

### Grows a certian confirgertion off of it, once enough food is stored
### Only sensors, storage, and generic
### New field added to network, network must re-learn
class GrowthBlock:
    def __init__(self, creature, blueprint):
        self.creature = creature
        self.blueprint = blueprint

    def upkeep(self):
        self.creature.food -= 3


### Once enough food is avialble makes a creature with blueprint of creature with it
### Can create growth and vine blocks for max reproductive effect
### new brain_block and network, must learn
class ReproductionBlock:
    def __init__(self, creature, blueprint):
        self.creature = creature
        self.blueprint = blueprint

    def upkeep(self):
        self.creature.food -= 6


