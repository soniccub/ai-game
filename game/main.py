### This is the main game file
import threading
#import gc
#gc.enable()
pause = False
import datetime

from tkinter import *
import world
import creatures
import tkinter_handler
import pickle

class Main:

    def __init__(self, filename="not yet saved",size=[1900, 1080]):
        self.size = size
        self.root = Tk()
        self.root.bind()
        self.filename = filename



        self.world_size = [1800, 900]


        self.gameframe = GameFrame(self, self.root)
        self.world = world.World(self, self.world_size, 0, 1.5, self.gameframe, self.size)
        self.creatures = creatures.Creatures(self.world_size, self, self.gameframe, self.size)





        self.brain_size_food_ratio = 0.25







    def tick(self, stopped):
        if not stopped:
            self.world_update()


            self.creature_update()

        self.draw_update()







    def world_update(self):
        self.world.tick()

    def creature_update(self):
        self.creatures.tick()

    def draw_update(self):
        self.creatures.draw()
        self.world.draw_objects()
    def print_stats(self):
        print("Age: ", self.gameframe.counter)
        print("Size: ", self.world_size)

        self.world.print_stats()
        self.creatures.print_stats()




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
        self.main.root.bind('<l>', load)
        self.main.root.bind('<s>', save)
        self.main.root.bind('<p>', print_stats)





        last_time = 0

        self.counter = 0
        while True:
            last_time = datetime.datetime.now()
            self.frame.delete("all")
            self.main.tick(True)
            self.root.update_idletasks()
            self.root.update()
            if self.counter < 1000000:

                self.counter += 1
                self.main.tick(False)

            else:
                self.main.tick(True)
            new_time = datetime.datetime.now()
            change = new_time-last_time
            print(change.total_seconds(), self.counter)



    def position_on_screen(self, position, size):
        return tkinter_handler.if_on_screen(position, size, self.center_screen_position, self.size)

    def coord_switch(self, position):
        return tkinter_handler.coord_switch(position, self.center_screen_position, self.size)








start = input()
if start == "0":
    main = Main()
else:
    main = pickle.load(open(str(start),"rb"))
    main.filename = start


def leftKey(event):
    global main

    main.gameframe.center_screen_position[0] -= 100


def rightKey(event):
    global main

    main.gameframe.center_screen_position[0] += 100


def upKey(event):

    main.gameframe.center_screen_position[1] -= 100


def downKey(event):
    main.gameframe.center_screen_position[1] += 100

def save(event):
    try:
        save = int(input())
        if save == 0:
            pass
        else:

            pickle.dump(main, open(str(save), "wb"))
    except:
        pass


def load(event):
    try:
        loadvalue = int(input())
        if loadvalue == 0:
            pass
        else:

            main = pickle.load(open(str(loadvalue), "rb"))
            main.filename = loadvalue
    except:
        pass


def print_stats(event):
    print("File name: ", main.filename)
    main.print_stats()


main.gameframe.start()