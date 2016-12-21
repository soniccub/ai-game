import blocks
import math

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
        self.direction = 0
        self.block_turn_ratio = 1/2

        self.block_power_ratio = 10

        if len(blueprint) == 0:
            self.blueprint = Blueprint(self)
        self.creature_creation()
        self.active_block_list = []
        for i in self.blocks:
            if i.activatable:
                self.active_block_list.append(i)

        for i in self.active_block_list:
            i.activate([10, 10])


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



    def move_direction(self, position, power):
        position_list = []
        for i in self.blocks:
            position_list.append(i.coords)
        x_average = 0
        y_average = 0
        for i in position_list:
            x_average += i[0]
            y_average += i[1]

        x_average /= len(position_list)
        y_average /= len(position_list)

        direction = math.atan(abs(y_average+position[1])/abs(x_average+position[0])) * 180/math.pi

        if position[0] > 0 and position[1] > 0:
            pass
        elif position[0] < 0 and position[1] > 0:
            direction += 90
        elif position[0] < 0 and position[1] < 0:
            direction += 180

        elif position[0] > 0 and position[1] < 0:
            direction += 270


        return direction

    def update_position(self, position, strength):
        move_distance = len(self.blocks)/self.block_power_ratio
        direction_change = self.move_direction(position, strength)
        self.direction_update(direction_change, strength)


        changeX = move_distance * math.cos(self.direction) * strength[0] + math.cos(self.direction) * strength[1]
        changeY = move_distance * math.sin(self.direction) * strength[0] + math.sin(self.direction) * strength[1]

        for i in self.blocks:

            i.position[0] += changeX
            i.position[1] += changeY

    def direction_update(self, direction_change, power):

        if direction_change % 270 != direction_change or direction_change < 90:
            if direction_change > 270:
                direction_change -= 360

            self.direction -= direction_change / 180 * math.sqrt(power[0] ** 2 + power[1] ** 2)






        elif direction_change > 90 and direction_change < 180:

            self.direction += direction_change / 180 * math.sqrt(power[0] ** 2 + power[1] ** 2)



            #self.direction += len(self.blocks)/self.block_turn_ratio * direction_change
            self.direction %= 360
        print(direction_change, self.direction)

    def draw(self):

        for block in self.blocks:

            if block.type == "body":

                block.position[0] += (math.cos(self.direction * math.pi/180) -
                                      math.cos(block.last_direction * math.pi / 180)) * block.coords[0] * self.block_size[0]
                block.position[1] += (math.sin(self.direction * math.pi/180) -
                                      math.sin(block.last_direction * math.pi / 180)) * block.coords[1] * self.block_size[1]
                block.last_direction = self.direction
                temp_cord = self.frame.coord_switch(block.position)


                if self.frame.position_on_screen(temp_cord, self.block_size):
                    self.frame.frame.create_polygon(temp_cord[0] - self.block_size[0] / 2,
                                                    temp_cord[1] - self.block_size[1] / 2,

                                                    temp_cord[0] + self.block_size[0] / 2,
                                                    temp_cord[1] - self.block_size[1] / 2,

                                                    temp_cord[0] + self.block_size[0] / 2,
                                                    temp_cord[1] + self.block_size[1] / 2,

                                                    temp_cord[0] - self.block_size[0] / 2,
                                                    temp_cord[1] + self.block_size[1] / 2,
                                                    fill=block.color)
                else:

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


