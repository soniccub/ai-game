import blocks

class Creatures:

    def __init__(self, size, main, frame, screen_size):

        self.creatures_list = []
        self.size = size
        self.main = main
        self.frame = frame
        self.screen_size = screen_size


        #self.creature_create()

    def creature_create(self):
        ### For every set of 20 spaces
        for i in range(-self.size[0]/2, self.size[0]/2, 20):
            for ii in range(-self.size[1]/2, self.size[1]/2, 20):
                #create_creature(i,ii)
                pass
    def generation(self):
        pass


    def tick(self):
        pass

    def draw(self):
        pass

    def creature_creation(self, position):
        self.creatures_list.append(Creature(position))



class Creature:
    def __init__(self, position, blueprint):

        self.position = position
        self.blueprint = blueprint




class Blueprint:

    def __init__(self, size, old_print=[]):
        self.center = [0, 0]
        if len(old_print) == 0:
            self.create_print()
        else:
            self.old_print_change()

    def create_print(self):
        self.size = [3, 3]
        self.block_positions = []
        for i in range(self.size[0]):
            self.block_positions.append([])
            for ii in range(self.size[1]):
                ### Block will be replaced with class object

                self.block_positions[i].append([[i, ii], "block"])


        self.block_positions[1][1][1] = brainblock.BrainBlock()









    def old_print_change(self):
        pass


