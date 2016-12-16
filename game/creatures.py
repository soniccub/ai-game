import blocks

class Creatures:

    def __init__(self, size, main, frame, screen_size):

        self.creatures_list = []
        self.size = size
        self.main = main
        self.frame = frame
        self.screen_size = screen_size


        #self.creature_create()
        self.creatures_list.append(Creature(self.frame,[0, 0]))

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
    def __init__(self, frame, position, blueprint=[]):
        self.frame = frame
        self.position = position
        self.blueprint = blueprint
        self.block_size = [10, 10]
        self.blocks = []

        if len(blueprint) == 0:
            self.blueprint = Blueprint(self)
        self.creature_creation()




    def creature_creation(self):
        for i in self.blueprint.blocks:

            coords = [i[1][0] * self.block_size[0] + self.position[0],
                      i[1][0] * self.block_size[1] + self.position[1]]
            self.blocks.append(self.block_create(i[0], coords, [i[1][0], i[1][1]]))

    def block_create(self, block_str, coord, coord_on_creature):
        print(block_str)
        if block_str == "GenericBlock":
            new_block = blocks.bodyblock.GenericBlock(self, coord, coord_on_creature)

        elif block_str == "MoveBlock":
            new_block = blocks.bodyblock.MoveBlock(self, coord, coord_on_creature)

        elif block_str == "StorageBlock":
            new_block = blocks.bodyblock.StorageBlock(self, coord, coord_on_creature)

        elif block_str == "VineBlock":


            new_block = blocks.bodyblock.VineBlock(self, coord, coord_on_creature, self.blueprint.vineprint)


        elif block_str == "ReproductionBlock":

            new_block = blocks.bodyblock.ReproductionBlock(self, coord, coord_on_creature, self.blueprint.blocks)


        elif block_str == "BrainBlock":
            new_block = blocks.bodyblock.GenericBlock(self, coord, coord_on_creature)




        elif block_str == "GeneralSensor":
            new_block = blocks.bodyblock.GenericBlock(self, coord, coord_on_creature)



        return new_block





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

    def draw(self):

        for block in self.blocks:

            if block.type == "body":

                temp_cord = self.frame.coord_switch(block.position)
                print(block.position)
                if self.frame.position_on_screen(temp_cord, self.block_size):
                    self.frame.frame.create_rectangle(temp_cord[0] - self.block_size[0] / 2,
                                                      temp_cord[1] - self.block_size[1] / 2,
                                                      temp_cord[0] + self.block_size[0] / 2,
                                                      temp_cord[1] + self.block_size[1] / 2,
                                                        fill=block.color)
                else:
                    print(1)
                    pass






















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


