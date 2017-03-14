### This is the main game file

#import gc
#gc.enable()
from datetime import datetime

from tkinter import *
import world
import creatures
import tkinter_handler

class Main:

    def __init__(self, size=[1100, 850]):
        self.size = size
        self.root = Tk()
        self.root.bind()




        self.world_size = [800, 800]


        self.gameframe = GameFrame(self, self.root)
        self.world = world.World(self, self.world_size, 0, 1.5, self.gameframe, self.size)
        self.creatures = creatures.Creatures(self.world_size, self, self.gameframe, self.size)





        self.brain_size_food_ratio = 0.25







    def tick(self):

        self.world_update()
        self.creature_update()
        self.draw_update()





    def world_update(self):
        self.world.tick()

    def creature_update(self):
        self.creatures.tick()

    def draw_update(self):
        self.creatures.draw()
        self.world.draw()




class GameFrame:
    def __init__(self, main, root):
        self.main = main
        self.size = main.size
        self.root = root
        self.center_screen_position = [0, 0]

        self.frame = Canvas(self.root, width=self.size[0], height=self.size[1])


        self.frame.pack()



    def start(self):
        self.main.root.bind('<Left>', leftKey)
        self.main.root.bind('<Right>', rightKey)
        self.main.root.bind('<Up>', upKey)
        self.main.root.bind('<Down>', downKey)
        last_time = 0
        while True:
            last_time = datetime.now()

            self.frame.delete("all")
            self.main.tick()
            self.root.update_idletasks()
            self.root.update()
            print(((abs(datetime.now().microsecond-last_time.microsecond))/1000000.0))
            for i in self.main.creatures.creatures_list:
                #print(i.food/i.food_level_max(), "food")
                pass


    def position_on_screen(self, position, size):
        return tkinter_handler.if_on_screen(position, size, self.center_screen_position, self.size)

    def coord_switch(self, position):
        return tkinter_handler.coord_switch(position, self.center_screen_position, self.size)

    def draw_shape(self, points):
        points = []







main = Main()

def leftKey(event):

    main.gameframe.center_screen_position[0] -= 100
    main.creatures.creatures_list[0].direction_change(10)

def rightKey(event):

    main.gameframe.center_screen_position[0] += 100




def upKey(event):

    main.gameframe.center_screen_position[1] -= 100


def downKey(event):
    main.gameframe.center_screen_position[1] += 100

main.gameframe.start()
