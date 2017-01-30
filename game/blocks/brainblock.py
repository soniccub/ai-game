import math

### Brain - not actual block
### Bigger brain = more resource drain
### Adds dorect connection to networks
### Controls networks and acts as overall brain
### More add




class BrainBlock():
    pass


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


    def network_input(self, inputs):
        pass

    def output(self, output):
        self.creature.activate(output)

    def network_create(self):
        pass