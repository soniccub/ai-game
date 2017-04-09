import blocks
import math
import random
import threading


class Creatures:

    def __init__(self, size, main, frame, screen_size):

        self.creatures_list = []
        self.size = size
        self.main = main
        self.frame = frame
        self.screen_size = screen_size


        self.start_creatures()
        print("creatures Created")

    def start_creatures(self, amount=5, blueprint=[], position_near=[]):
        if len(position_near) == 0:
            for i in range(amount):
                position = [(random.randrange(self.main.world.size[0]) - self.main.world.size[0]/2) * 7 / 10,
                            (random.randrange(self.main.world.size[1]) - self.main.world.size[1]/2) * 7 / 10]

                self.creature_creation(position)
        else:
            for i in range(amount):
                position = [random.randrange(30) + position_near[0],
                            random.randrange(30) + position_near[1]]
                self.creature_creation(position, blueprint, position_near, True)

    def tick(self):
        pop_list = []
        for i in self.creatures_list:

            i.tick()
            if (i.position[0] > self.main.world_size[0]/2 or i.position[0] <
                    -self.main.world_size[0]/2) or (i.position[1] > self.main.world_size[1]/2 or i.position[1] < -self.main.world_size[1]/2) or i.food < 0:
                pop_list.append(i)


        while len(pop_list) > 0:
            if len(self.creatures_list) == 0:
                break
                input()
            self.redo_id()
            self.creatures_list.pop(pop_list[0].id)
            pop_list.pop(0)

    def draw(self):
        for creature in self.creatures_list:
            creature.draw()

    def creature_creation(self, position, blueprint=[], position_near=[], copy=False):

        self.creatures_list.append(Creature(self.frame, position, self,len(self.creatures_list), blueprint, position_near, copy))

    def set_copy(self, original_creature, copy_position):


        copy_creature = None
        for i in range(len(self.creatures_list)):

            if self.creatures_list[i].position == copy_position:
                copy_creature = self.creatures_list[i]

        for i in range(len(original_creature.blocks)):
            if original_creature.blocks[i].type == "brain":
                original_creature.blocks[i].copy(copy_creature)
        copy_creature.blueprint.mutation()
        copy_creature.food = original_creature.food

    def print_stats(self):
        print("----------------------------------------------------------------------")
        print("CREATURES: ", len(self.creatures_list))
        average_age = 0
        for i in self.creatures_list:
            average_age += i.age

        average_age /= len(self.creatures_list)
        print("Average age is: ", average_age)

        species_list = []
        # [[amount, average food, average age, blueprint, id_list],[etc]]
        for i in self.creatures_list:

            is_in_list = False
            for ii in range(len(species_list)):

                if self.check_if_same(i, species_list[ii][2]):
                    is_in_list = True
                    species_list[ii][0] += 1
                    species_list[ii][1] += i.food
                    species_list[ii][2] += i.age
                    species_list[ii][4] += i.id

            if not is_in_list:
                species_list.append([1, i.food,i.blueprint.blocks,i.id])

        for i in range(len(species_list)):
            species_list[i][1] /= species_list[i][0]
            species_list[i][2] /= species_list[i][0]

            print("thing: ", i)
            print("amount: ", species_list[i][0])
            print("average_food: ", species_list[i][1])
            print("Average age: ", species_list[i][2])
            print("Blueprint: ", species_list[i][3])





        for i in range(len(self.creatures_list)):
            print("----")
            print("    Creature: ", i)
            self.creatures_list[i].printstats()

    def redo_id(self):
        for i in range(len(self.creatures_list)):
            self.creatures_list[i].id = i


    def check_if_same(self, creature1, blueprint):

        if len(creature1.blueprint.blocks) == len(blueprint.blocks):


            for i in creature1.blueprint.blocks:
                if i not in blueprint.blocks:
                    return False
            for i in blueprint.blocks:
                if i not in creature1.blueprint.blocks:
                    return False

        else:
            return False
        return True




class Creature:
    def __init__(self, frame, position, creatures, id, blueprint=[], position_near=[], copy=False):
        self.last_food = 0
        self.food = 0
        self.frame = frame
        self.position = position
        self.block_size = [3, 3]
        self.blocks = []
        self.power_move_ratio = 1
        self.turn_power_ratio = 1/30
        self.creatures = creatures
        self.direction = 90
        self.sensors = []

        self.id = id

        self.age = 0


        self.sense_detail = 10
        self.action_blocks = []
        self.blueprint = Blueprint(self, blueprint)
        self.blueprint.mutation()
        self.beingattacked = False
        self.last_attack_time = 10
        for i in self.blocks:
            if self.creatures.main.world.is_touching_object(i):
                self.creatures.start_creatures(1, self.blueprint, self.position)
                self.creatures.creatures_list.pop(id)
                self.creatures.redo_id()
                print("creature location is bad-retrying")
                break
        self.creature_creation()

    def activate(self, power_list):
        ### Each run of the neural network will return a list of "powers"
        ### The power is the strength of each activation in the list of possible activatible objects
        for i in range(len(self.active_block_list)):
            self.active_block_list[i].activate(power_list[i])

    def creature_creation(self):
        self.blocks = []
        for i in self.blueprint.blocks:

            coords = [i[1][0] * self.block_size[0] + self.position[0],
                      i[1][1] * self.block_size[1] + self.position[1]]
            self.direction = 0


            self.blocks.append(self.block_create(i[0], coords, i[1]))

        self.active_block_list = []
        for i in self.blocks:
            if i.activatable:
                self.active_block_list.append(i)

        for i in self.blocks:
            if i.type == "brain":
                i.create_brain()
        self.food = self.food_level_max()
        self.food_max = self.food_level_max()
        self.last_food = 0


    def block_create(self, block_str, coord, coord_on_creature):
        if block_str == "GenericBlock":
            new_block = blocks.bodyblock.GenericBlock(self, coord, coord_on_creature)

        elif block_str == "MoveBlock":

            new_block = blocks.bodyblock.MoveBlock(self, coord, coord_on_creature)
            self.action_blocks.append(new_block)

        elif block_str == "StorageBlock":

            new_block = blocks.bodyblock.StorageBlock(self, coord, coord_on_creature)


        elif block_str == "VineBlock":

            new_block = blocks.bodyblock.VineBlock(self, coord, coord_on_creature, self.blueprint.vineprint)


        elif block_str == "ReproductionBlock":

            new_block = blocks.bodyblock.ReproductionBlock(self, coord, coord_on_creature, self.blueprint.blocks)
            self.action_blocks.append(new_block)


        elif block_str == "BrainBlock":
            new_block = blocks.brainblock.BrainBlock(self, [coord[0], coord[1]], coord_on_creature, coord_on_creature[2])



        elif block_str == "GeneralSensor" or block_str == "CreatureSensor" or block_str == "ObstacleSensor" or block_str == "FoodSensor":
            new_block = blocks.sensors.Sensor(self, coord, coord_on_creature, block_str, self.sense_detail)
            self.sensors.append(new_block)
        elif block_str == "Creature_eat_block":
            new_block = blocks.bodyblock.Creature_eat_block(self, [coord[0], coord[1]], coord_on_creature, coord_on_creature[2])
        elif block_str == "GrowthBlock":
            new_block = blocks.bodyblock.GrowthBlock(self, [coord[0], coord[1]], coord_on_creature, coord_on_creature[2])


        elif block_str == "Leafblock":
            new_block = blocks.bodyblock.Leafblock(self, coord, coord_on_creature)


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
        #print(angle_measure(position), position, 999999)
        angle = angle_measure(position)
        angle %= 360
        angle -= 90
        self.direction %= 360
        #print(angle, "angle")
        if angle > 180:

            #print(((-360+angle)/180) * power * (self.turn_power_ratio * 20) , 10000000)
            return ((angle-360)/180) * power * (self.turn_power_ratio * 20)
        elif angle < 180:
            #print((angle / 180) * power * (self.turn_power_ratio * 20), 2000000000)
            return (angle / 180) * power * (self.turn_power_ratio * 20)

        return 0



    def direction_change(self, direction):
        direction_change = self.direction - direction
        self.direction += direction
        self.direction %= 360
        for block in self.blocks:
            block.last_direction = block.direction
            if block.type == "sensor":
                block.sense_direction += direction_change


            block.position[0] += math.cos((block.direction - self.direction) * math.pi/180) * self.block_size[0] * math.sqrt(block.coords[0]**2 + block.coords[1]**2)
            block.position[1] += math.sin((block.direction - self.direction) * math.pi/180) * self.block_size[1] * math.sqrt(block.coords[0]**2 + block.coords[1]**2)

            for i in range(len(block.x_edges)):

                block.x_edges[i] = math.cos(i * math.pi/2 + math.pi/4) * self.block_size[0] / math.sqrt(2) + self.position[0] \
                                    + math.cos((block.direction - self.direction) * math.pi/180) * self.block_size[0] * math.sqrt(block.coords[0]**2 + block.coords[1]**2)


                block.y_edges[i] = math.sin(i * math.pi / 2 + math.pi / 4) * self.block_size[1] / math.sqrt(2) + self.position[1] \
                    + math.sin((block.direction - self.direction) * math.pi/180) * self.block_size[1] * math.sqrt(block.coords[0]**2 + block.coords[1]**2)

    def block_edges_create(self):

        for block in self.blocks:
            if block.type == "brain" or block.type == "body" or block.type == "sensor":
                for i in range(4):

                    block.x_edges.append(math.cos(i * math.pi/2 + math.pi/4) * self.block_size[0] / math.sqrt(2) + self.position[0]
                        + math.cos((block.direction - self.direction) * math.pi/180) * self.block_size[0] * math.sqrt(block.coords[0]**2 + block.coords[1]**2))
                    block.y_edges.append(math.sin(i * math.pi / 2 + math.pi / 4) * self.block_size[1] / math.sqrt(2) + self.position[1]
                        + math.sin((block.direction - self.direction) * math.pi/180) * self.block_size[1] * math.sqrt(block.coords[0]**2 + block.coords[1]**2))

            #if block.type == "sensor":
             #   for i in range(3):

              #      if i == 0:

               #         block.x_edges.append(math.cos(self.direction) * self.block_size[0] / math.sqrt(2) + self.position[0]
                #            + math.cos((block.direction - self.direction) * math.pi/180) * self.block_size[0] * math.sqrt(block.coords[0]**2 + block.coords[1]**2))

                 #       block.y_edges.append(0 * self.block_size[1] / math.sqrt(2) + self.position[1] + math.sin(
                  #          (block.direction - self.direction) * math.pi / 180) * self.block_size[1] * math.sqrt(block.coords[0] ** 2 + block.coords[1] ** 2))

    def position_update(self, position_change):
        block_position_save = []
        for block in range(len(self.blocks)):
            block_position_save.append(list(self.blocks[block].position))
            self.blocks[block].position[0] += position_change[0]
            self.blocks[block].position[1] += position_change[1]


        old_position = list(self.position)
        self.position[0] += position_change[0]
        self.position[1] += position_change[1]

        for i in self.blocks:
            if self.creatures.main.world.is_touching_object(i):
                self.position = list(old_position)
                for block in range(len(self.blocks)):
                    self.blocks[block].position = list(block_position_save[block])



    def move(self, coords, power):
        self.direction_change(self.move_direction(coords, power))
        #print(power, coords)
        #print("LLLLL")

        self.position_update([math.cos(self.direction * math.pi / 180 - math.pi/2) * power * self.power_move_ratio / len(self.blocks),
                              math.sin(self.direction * math.pi / 180 + math.pi/2 ) * power * self.power_move_ratio / len(self.blocks)])



    def draw(self):

        for block in self.blocks:
            #print(block.type, block.coords)
            x_edges = []
            y_edges = []
            if True:
                for i in range(4):
                    x_edges.append(
                        math.cos(i * math.pi / 2 + math.pi / 4) * self.block_size[0] / math.sqrt(2) + self.position[0]
                        + math.cos((block.direction - self.direction) * math.pi / 180) * self.block_size[0] * math.sqrt(
                            block.coords[0] ** 2 + block.coords[1] ** 2))
                    y_edges.append(
                        math.sin(i * math.pi / 2 + math.pi / 4) * self.block_size[1] / math.sqrt(2) + self.position[1]
                        + math.sin((block.direction - self.direction) * math.pi / 180) * self.block_size[1] * math.sqrt(
                            block.coords[0] ** 2 + block.coords[1] ** 2))


                edge_list = []
                #print("-----------")
                #print(self.position)
                #print(block.position)
                #print(block.coords)
                #print(self.block_size)
                #print(x_edges,y_edges)
                for i in range(len(x_edges)):
                    edge_list.append(self.frame.coord_switch([x_edges[i], y_edges[i]]))

            else:
                edge_list = []
                for i in range(4):

                    block.x_edges.append(math.cos(i * math.pi/2 + math.pi/4) * self.block_size[0] / math.sqrt(2) + self.position[0]
                        + math.cos((block.direction - self.direction) * math.pi/180) * self.block_size[0] * math.sqrt(block.coords[0]**2 + block.coords[1]**2))
                    block.y_edges.append(math.sin(i * math.pi / 2 + math.pi / 4) * self.block_size[1] / math.sqrt(2) + self.position[1]
                        + math.sin((block.direction - self.direction) * math.pi/180) * self.block_size[1] * math.sqrt(block.coords[0]**2 + block.coords[1]**2))
                print("Object type not right for drawing object: ", block.type)
                break
            new_edge_list = []
            for i in edge_list:
                new_edge_list.append([i[0], i[1]])
            #print(block.direction, edge_list)

            self.frame.frame.create_polygon(new_edge_list, fill=block.color)

    def check_block_touching(self):
        input_list = []
        for block in self.blocks:
            if self.creatures.main.world.is_touching_object(block):
                input_list.append(1)
            else:
                input_list.append(0)
        return input_list

    def food_level_max(self):
        food_max = 0
        for block in self.blocks:
            food_max += block.food_storage
        return food_max

    def network_input(self):
        inputs = []
        inputs.append(self.food / self.food_level_max())
        touching_list = self.check_block_touching()
        for i in touching_list:
            inputs.append(i)

        return inputs

    def set_copy(self, copy):
        for i in self.blocks:
            if i.type == "brain":

                i.copy(copy, copy.blueprint.mutation())

    def reproduce(self):
        self.creatures.start_creatures(1, self.blueprint, self.position)

    def tick(self):

        self.last_food += 1
        if self.food > 0:
            for i in self.blocks:
                if i.type == "brain":
                    i.input(self.network_input())
                i.upkeep()
        self.last_attack_time+=1
        if self.last_attack_time > 9:
            self.beingattacked = False
        self.age +=1
        if self.food > self.food_level_max():
            self.food = self.food_level_max()

    def printstats(self):
        print("Age: ", self.age)
        print("Food: ",self.food/self.food_level_max())
        print("Position: ",self.position)
        print("blueprint: ",self.blueprint.blocks)
        for i in self.blueprint.blocks:
            if i == "GrowthBlock":
                print("Growth Blueprint", i.blueprint_growth)




class Blueprint:

    def __init__(self, creature, old_print=[]):

        ### blueprint of creature
        ### Creature is blocks within blueprint/ if growth or vine block can grow into these blocks
        self.name_list = ["GenericBlock", "MoveBlock", "StorageBlock", "ReproductionBlock",
                          "GeneralSensor", "CreatureSensor", "ObstacleSensor","FoodSensor", "GrowthBlock", "Leafblock"]
        self.center = [0, 0]
        self.creature = creature

        if type(old_print) == list:

            ### This creates a new blueprint from scratch, reserved for new creatures when creating world

            self.create_print()
        else:

            self.blocks = old_print.blocks

        self.vineprint = list(self.blocks)

    def create_print(self):
        self.blocks = []

        self.blocks.append(["GeneralSensor", [-1, 1]])
        self.blocks.append(["GeneralSensor", [1, 1]])


        self.blocks.append(["MoveBlock", [-1, -1]])
        self.blocks.append(["MoveBlock", [1, -1]])

        self.blocks.append(["BrainBlock", [0, 0, 1]])
        self.blocks.append(["ReproductionBlock", [0, -1]])

        self.blocks.append(["GenericBlock", [-1, 0]])
        self.blocks.append(["GenericBlock", [1, 0]])
        self.blocks.append(["GenericBlock", [0, 1]])



    def new_block(self, coords):
        print("new_block")
        block = random.choice(self.name_list)
        if block == "GrowthBlock":
            growth_block_list = []
            growth_edge_list = []
            for i in range(random.randrange(4)):
                open_edges = self.edges_open()
                newer_block = random.choice(self.name_list)
                while newer_block == "GrowthBlock" or newer_block == "VineBlock":
                    print("loop3")
                    newer_block = random.choice(self.name_list)
                edge = random.choice(open_edges)
                counter = 0
                while counter < 10 and edge not in growth_edge_list:
                    edge = random.choice(open_edges)
                    counter += 1
                    print("loop4")
                if counter < 10:
                    growth_edge_list.append(edge)
                    growth_block_list.append([newer_block, edge])
            coords.append(growth_block_list)


        self.blocks.append([block, coords])

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

    def mutation(self):
        block_to_pop = False
        new_block = False

        for i in range(len(self.blocks)):
            mutation = random.randrange(100)
            if mutation > 97:
                print("Mutation of Creature:", self.creature.id)
                if self.blocks[i][0] != "brain":
                    new_block = self.blocks[i][1]
                    block_to_pop = i
                    break
            elif self.blocks[i][0] == "GrowthBlock" and random.randrange(100) > 97:
                if random.randrange(100) > 50:
                    growth_edge_list = []
                    for ii in self.creature.blocks[i][1][2]:
                        growth_edge_list.append(self.blocks[i][1][2][ii][1])
                    for i in range(random.randrange(4)):
                        open_edges = self.edges_open()
                        newer_block = random.choice(self.name_list)
                        while newer_block == "GrowthBlock" or newer_block == "VineBlock":
                            newer_block = random.choice(self.name_list)
                        edge = random.choice(open_edges)
                        counter = 0
                        while counter < 10 or not edge in growth_edge_list:
                            edge = random.choice(open_edges)
                            counter += 1
                            print("loop")
                        if counter < 10:
                            growth_edge_list.append(edge)
                            self.blocks[i][1][2].append([newer_block, edge])
                            break
                else:
                    self.blocks[i][1][2].pop(random.randrange(len(self.blocks[i][1][2])))
                    break
            elif mutation < 2:
                self.blocks.pop(random.randrange(len(self.blocks)))
                break
        real_edge = self.edges_open()
        for i in real_edge:
            if random.randrange(2000) > 1998:
                self.new_block(i)
        if block_to_pop:
            self.blocks.pop(block_to_pop)
        if new_block:
            self.new_block(new_block)

    def blueprint_add(self, block_list):
        for i in block_list:
            self.blocks.append(i)

    def edges_open(self):
        outside_edge = []
        for i in self.blocks:
            outside_edge.append([i[1][0] - 1, i[1][1] - 1])
            outside_edge.append([i[1][0] - 1, i[1][1] + 1])
            outside_edge.append([i[1][0] + 1, i[1][1] - 1])
            outside_edge.append([i[1][0] + 1, i[1][1] + 1])
        real_edge = []
        for ii in outside_edge:
            for i in self.blocks:
                if not i[1] == ii:
                    real_edge.append(ii)
        return real_edge


def angle_measure(coords):
    if coords[0] == 0:
        if coords[1] > 0:
            direction = 90
        else:
            direction = 270

    elif coords[1] == 0:
        if coords[0] > 0:
            direction = 0
        else:
            direction = 180
    else:
        direction = abs(math.atan(coords[1] / coords[0]) * 180 / math.pi)
        if coords[0] < 0:
            if coords[1] < 0:

                direction += 180
            else:
                direction += 90

        elif coords[1] < 0:
            direction += 270
    return direction