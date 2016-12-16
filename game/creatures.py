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
    def __init__(self, position, blueprint, creature_size):

        self.position = position
        self.blueprint = blueprint
        self.block_size = [10, 10]
        self.blocks = []
        self.creature_size = creature_size





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








class Blueprint:

    def __init__(self, size, creature, old_print=[]):
        ### blueprint of creature
        ### Creature is blocks within blueprint/ if growth or vine block can grow into these blocks
        self.center = [0, 0]
        self.creature = creature

        if len(old_print) == 0:
            ### This creates a new blueprint from scratch, reserved for new creatures when creating world
            self.create_print()
        else:
            self.old_print_change()

    def create_print(self):
        self.size = [3, 3]
        self.blocks = []
        ### Takes every coord in the new 3x3 creature to be created and makes a generic block at that position

        for i in range(-1, 1):
            for ii in range(-1, 1):
                block_position = [i, ii]
                self.blocks.append(bodyblock.GenericBlock(self.creature, [block_position[0] * self.creature.block_size[0] + self.creature.position[0],
                           block_position[1] * self.creature.block_size[1] + self.creature.position[1]], block_position))

                ### Next comes changing the type of block...... was going to just have 9 of those above but this isnt too much better

            ### This changes the type of block into the default creature configuration
        for i in range(self.blocks):
            if self.blocks[i].position == [-1, -1] or self.blocks[i].position == [1, -1]:
                self.blocks[i] = self.block_change(self.blocks[i], "MoveBlock")

            elif self.blocks[i].position == [0, 0]:
                pass
                self.blocks[i] = self.block_change(self.blocks[i], "BrainBlock")

            if self.blocks[i].position == [0, -1]:
                self.blocks[i] = self.block_change(self.blocks[i], "ReproductionBlock")

            ### Note add sensor blocks when code done



















    def block_change(block, new_block_string):
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
                new_block = bodyblock.VineBlock(block.creature, block.position, block.coords, block.creature.blueprint)

        if new_block_string == "ReproductionBlock":

            try:
                new_block = bodyblock.ReproductionBlock(block.creature, block.position, block.coords, block.blueprint)
            except NameError:
                new_block = bodyblock.ReproductionBlock(block.creature, block.position, block.coords, block.creature.blueprint)

        if new_block_string == "BrainBlock":
            pass


        return new_block




    def old_print_change(self):
        pass


