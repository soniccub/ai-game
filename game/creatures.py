import blocks

class Creatures:

    def __init__(self, size, main, frame, screen_size):

        self.creatures_list = []
        self.size = size
        self.main = main
        self.frame = frame
        self.screen_size = screen_size


        #self.creature_create()
        self.creatures_list.append(Creature([0,0]))

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
        for creature in self.creatures_list:
            creature.draw()

    def creature_creation(self, position):
        self.creatures_list.append(Creature(position))






class Creature:
    def __init__(self, position, blueprint=[]):

        self.position = position
        self.blueprint = blueprint
        self.block_size = [10, 10]
        self.blocks = []

        if len(blueprint) == 0:
            self.blueprint = Blueprint(self)




    def creature_creation(self):
        for i in self.blueprint.blocks:

            coords = [i[1][0] * self.block_size[0] + self.position[0],
                      i[1][0] * self.block_size[1] + self.position[1]]
            self.blocks.append(self.block_create(i[0], coords, [i[1][0], i[1][1]]))

    def block_create(self, block_str, coord, coord_on_creature):
        if block_str == "GenericBlock":
            new_block = bodyblock.GenericBlock(self, coord, coord_on_creature)

        elif block_str == "MoveBlock":
            new_block = bodyblock.MoveBlock(self, coord, coord_on_creature)

        elif block_str == "StorageBlock":
            new_block = bodyblock.StorageBlock(self, coord, coord_on_creature)

        elif block_str == "VineBlock":


            new_block = bodyblock.VineBlock(self, coord, coord_on_creature, self.blueprint.vineprint)


        elif block_str == "ReproductionBlock":

            new_block = bodyblock.ReproductionBlock(self, coord, coord_on_creature, self.blueprint.blocks)


        elif block_str == "BrainBlock":
            pass

        return new_block

    def draw(self):


        for block_number in range(self.blocks):
            for block in self.blocks[block_number]:
                block[2].position
                ### In blocks first and second position are coords while third is the object

                if block[2].type == "body":

                    temp_cord = self.frame.coord_switch(block[2].position)
                    if self.frame.position_on_screen(temp_cord, self.block_size):
                        self.frame.frame.create_rectangle(temp_cord[0] - self.block_size[0] / 2,
                                                          temp_cord[1] - self.block_size[1] / 2,
                                                          temp_cord[0] + self.block_size[0] / 2,
                                                          temp_cord[1] + self.block_size[1] / 2,
                                                          fill=block[2].color)
                    else:
                        pass



    def block_change(self ,block, new_block_string):
        if new_block_string == "GenericBlock":
            new_block = bodyblock.GenericBlock(block.creature, block.position, block.coords)

        if new_block_string == "MoveBlock":
            new_block = bodyblock.MoveBlock(block.creature, block.position, block.coords)

        if new_block_string == "StorageBlock":
            new_block = bodyblock.StorageBlock(block.creature, block.position, block.coords)

        if new_block_string == "VineBlock":
            try:

                new_block = bodyblock.VineBlock(block.creature, block.position, block.coords, block.blueprint)
            except NameError:
                new_block = bodyblock.VineBlock(block.creature, block.position, block.coords,
                                                        block.creature.blueprint)


        if new_block_string == "ReproductionBlock":

            try:
                new_block = bodyblock.ReproductionBlock(block.creature, block.position, block.coords, block.blueprint)
            except NameError:
                new_block = bodyblock.ReproductionBlock(block.creature, block.position, block.coords,
                                                        block.creature.blueprint)

        if new_block_string == "BrainBlock":
            pass

        return new_block






















class Blueprint:

    def __init__(self, creature, old_print=[]):

        ### blueprint of creature
        ### Creature is blocks within blueprint/ if growth or vine block can grow into these blocks

        self.center = [0, 0]
        self.creature = creature

        if len(old_print) == 0:

            ### This creates a new blueprint from scratch, reserved for new creatures when creating world

            self.create_print()
        else:
            self.old_print_change()
        self.vineprint = list(self.blocks)


    def create_print(self):
        self.size = [3, 3]
        self.blocks = []
        ### Takes every coord in the new 3x3 creature to be created and makes a generic block at that position

        self.blocks.append(["GeneralSensor", [-1, 1]])
        self.blocks.append(["GeneralSensor", [1, 1]])

        self.blocks.append(["MoveBlock", [-1, -1]])
        self.blocks.append(["MoveBlock", [1, -1]])

        self.blocks.append(["BrainBlock", [0, 0]])
        self.blocks.append(["ReproductionBlock", [0, -1]])

        self.blocks.append(["GenericBlock", [-1, 0]])
        self.blocks.append(["GenericBlock", [1, 0]])
        self.blocks.append(["GenericBlock", [0, 1]])





    def old_print_change(self):
        pass


