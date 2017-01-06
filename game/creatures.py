import blocks
import math
import random
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
        for i in self.creatures_list:
            i.activate([[0, 0], [0, 0], [0, 0], [0, 0]])

    def draw(self):
        for creature in self.creatures_list:
            creature.draw()

    def creature_creation(self, position):
        self.creatures_list.append(Creature(position))












class Creature:
    def __init__(self, frame, position, blueprint=[]):
        self.food = 1000
        self.frame = frame
        self.position = position
        self.blueprint = blueprint
        self.block_size = [10, 10]
        self.blocks = []

        self.direction = 90


        if len(blueprint) == 0:
            self.blueprint = Blueprint(self)
        self.creature_creation()
        self.active_block_list = []
        for i in self.blocks:
            if i.activatable:
                self.active_block_list.append(i)

        for i in self.active_block_list:
            i.activate([10, 10])
        self.block_edges_create()

    def activate(self, power_list):
        ### Each run of the neural network will return a list of "powers"
        ### The power is the strength of each activation in the list of possible activatible objects
        for i in range(len(self.active_block_list)):
            self.active_block_list[i].activate(power_list[i])





    def creature_creation(self):
        for i in self.blueprint.blocks:

            coords = [i[1][0] * self.block_size[0] + self.position[0],
                      i[1][1] * self.block_size[1] + self.position[1]]

            self.blocks.append(self.block_create(i[0], coords, [i[1][0], i[1][1]]))

    def block_create(self, block_str, coord, coord_on_creature):
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

    def block_change(self, block, new_block_string):
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

    def move_direction(self, position, power):
        return math.atan(position[1]/position[0]) * 180/math.pi * power

    def update_position(self, position, strength):
        #move_distance = len(self.blocks)/self.block_power_ratio
        direction_change = self.move_direction(position, strength)
        #self.direction_update(direction_change, strength)

        changeX = 0
        changeY = 0

        for i in self.blocks:

            i.position[0] += changeX
            i.position[1] += changeY

    def direction_change(self, direction):


        for block in self.blocks:
            block.last_direction = block.direction
            block.direction += direction
            block.direction %= 360


            for i in range(len(block.x_edges)):

                block.x_edges[i] = math.cos(i * math.pi/2 + math.pi/4) * self.block_size[0] / math.sqrt(2) + self.position[0] \
                                    + math.cos((block.direction - self.direction) * math.pi/180) * self.block_size[0] * math.sqrt(block.coords[0]**2 + block.coords[1]**2)


                block.y_edges[i] = math.sin(i * math.pi / 2 + math.pi / 4) * self.block_size[1] / math.sqrt(2) + self.position[1] \
                    + math.sin((block.direction - self.direction) * math.pi/180) * self.block_size[1] * math.sqrt(block.coords[0]**2 + block.coords[1]**2)

    def block_edges_create(self):
        for block in self.blocks:
            for i in range(4):

                block.x_edges.append(math.cos(i * math.pi/2 + math.pi/4) * self.block_size[0] / math.sqrt(2) + self.position[0]
                    + math.cos((block.direction - self.direction) * math.pi/180) * self.block_size[0] * math.sqrt(block.coords[0]**2 + block.coords[1]**2))
                block.y_edges.append(
                    math.sin(i * math.pi / 2 + math.pi / 4) * self.block_size[1] / math.sqrt(2) + self.position[1]
                    + math.sin((block.direction - self.direction) * math.pi/180) * self.block_size[1] * math.sqrt(block.coords[0]**2 + block.coords[1]**2))

    def position_update(self, new_position):
        for block in self.blocks:
            for i in block.x_edges:
                i += new_position[0] - block.position[0]

            for i in block.y_edges:
                i += new_position[1] - block.position[1]
            block.position = new_position


    def move(self, power, block):
        self.direction_change(self.move_direction(block.coords, power))


    def draw(self):

        for block in self.blocks:

            if block.type == "body":
                edge_list = []
                for i in range(len(block.x_edges)):
                    #print(i, block.x_edges[i], block.color, block.x_edges)
                    edge_list.append(self.frame.coord_switch([block.x_edges[i], block.y_edges[i]]))

                self.frame.frame.create_polygon(edge_list[0],edge_list[1], edge_list[2],edge_list[3], fill=block.color)












class Blueprint:

    def __init__(self, creature, old_print=[]):

        ### blueprint of creature
        ### Creature is blocks within blueprint/ if growth or vine block can grow into these blocks
        self.name_list = ["Generic_Block", "MoveBlock", "StorageBlock", "ReproductionBlock", "MoveBlock",
                          "GeneralSensor"]
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
        change_chance = 3
        new_block_chance = 2
        # 2%
        for i in self.blocks:
            if random.randrange(100) < self.change_chance:
                self.name_change(i)
        for i in self.block_edges_open():
            if random.randrange(100) < self.new_block_chance:
                self.new_block(i)



    def new_block(self, coords):
        self.blocks.append(random.choice(self.name_list), coords)

    def name_change(self, block):

        block[0] = random.choice(self.name_list)




    def block_edges_open(self):
        block_edges = []
        for i in self.blocks:
            for ii in range(4):
                if ii == 1:
                    block_edges.append(i[1][0] + 1, i[1][1])
                elif ii == 2:
                    block_edges.append(i[1][0] - 1, i[1][1])
                elif ii == 3:
                    block_edges.append(i[1][0], i[1][1] + 1)
                elif ii == 4:
                    block_edges.append(i[1][0] + 1, i[1][1] - 1)
        temp_edge = []
        for i in range(len(block_edges)):
            for ii in self.blocks:
                if not block_edges[i] == ii[1]:
                    temp_edge.append(block_edges[i])
        block_edges = temp_edge



        return block_edges



