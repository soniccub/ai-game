### This is the world for the game
import random
from world_objects import *



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
        return
        print(0)
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












