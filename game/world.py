### This is the world for the game
import random
from world_objects import *
import math



class World:
    def __init__(self,main, size, food_amount, obstacles_amount, canvas,screen_size, food_richnes=100):
        self.possible_objects = 2
        self.frame = canvas
        ### Size of the world
        self.size = size
        self.screen_size = screen_size
        ### food is split into three amounts

        ### [food already in enviorment, food that can be made from eviorment, food from obstacles]

        self.food_amount = food_amount
        ### The amount of obsticles 100 is 100% as in they cover everything
        self.obstacles_amount = obstacles_amount
        self.objects = []
        #self.objects.append(tree.Tree([100, 100], self.frame))
        self.creatures = []
        self.objects_positions = []
        self.build_world()



    def build_world(self):
        ### Builds the world
        ### Gens food obs
        ### [x,y,x,y]
        self.limits = [self.size[0]/2, self.size[1]/2, self.size[0]/2, self.size[1]/2]

        self.set_position(self.obstacles_amount)

    def set_position(self, amount):

        for positionX in range(-int(self.size[0]/2), int(self.size[0]/2), 10):
            for positionY in range(-int(self.size[1]/2), int(self.size[1]/2), 10):
                if random.randrange(100) > 100-amount:
                    self.spawn_object(positionX, positionY)

        for i in range(-int(self.size[0]/2), int(self.size[0]/2), 10):
            self.objects.append(tree.Tree([i, int(self.size[1] / 2)], self.frame))
            self.objects.append(tree.Tree([i, int(-self.size[1] / 2)], self.frame))

        for i in range(-int(self.size[0] / 2), int(self.size[0] / 2), 10):
            self.objects.append(tree.Tree([int(self.size[0] / 2), i], self.frame))
            self.objects.append(tree.Tree([int(-self.size[0] / 2), i], self.frame))


    def spawn_object(self,x ,y):
        rand = random.randrange(self.possible_objects)
        if rand == 0:
            object = tree.Tree([x, y], self.frame)
            self.objects.append(object)
        if rand == 1:
            object = rock.Rock([x, y], self.frame)
            self.objects.append(object)

        self.objects_positions.append([x, y, object])


    def spawn_food(self, x, y):
        pass
    def spawn_creature(self, x, y):
        pass


    def draw_objects(self):

        for i in self.objects:
            i.draw()

    def tick(self):

        pass

    def draw(self):
        draw_object_info = []
        for i in self.objects:
            ### [position,size,color]
            draw_object_info.append(i.draw())

    def space_near(self, creature_position):
        object_position_corners = []
        for i in range(self.objects):
            object_position_corners.append([self.objects[i].position[0] - creature_position[0] - self.objects[i].size[0] / 2,
                                            self.objects[i].position[1] - creature_position[1] - self.objects[i].size[1] / 2,
                                            ### Bottom Left corner

                                            self.objects[i].position[0] - creature_position[0] - self.objects[i].size[0] / 2,
                                            self.objects[i].position[1] - creature_position[1] + self.objects[i].size[1] / 2,
                                            ### Top Left Corner



                                            self.objects[i].position[0] - creature_position[0] + self.objects[i].size[0] / 2,
                                            self.objects[i].position[1] - creature_position[1] + self.objects[i].size[1] / 2,
                                            ### Top Right corner
                                            self.objects[i].position[0] - creature_position[0] + self.objects[i].size[0] / 2,
                                            self.objects[i].position[1] - creature_position[1] - self.objects[i].size[1] / 2,
                                            ### Bottom Right Corner

                                            self.objects[i],
                                            [self.objects[i].position[0] - creature_position[0],
                                             self.objects[i].position[1] - creature_position[1]]])
                                            ### Object that it adds to objects it can see and its center position



        return object_position_corners ### The bottom left and top right corners for positions






def vector_to_angle(self, position):
    if position[0] == 0:
        if position[1] > 0:
            direction = 90
        else:
            direction = 270

    elif position[1] == 0:
        if position[0] > 0:
            direction = 0
        else:
            direction = 180
    else:
        direction = math.atan(position[1] / position[0]) * 180 / math.pi
        if position[0] < 0:
            direction += 180


    return direction
