### Types of sensors each creature has
import math




class Sensor:

    def __init__(self, creature, coords, direction, type):

        self.creature = creature
        self.world = self.creature.creatures.main.world
        self.coords = coords
        self.direction = direction

    def sense(self):
        direction_facing = self.direction + self.creature.direction

        objects_around = self.world.space_near([self.creature.position[0] + math.cos(
            direction_facing * math.pi / 180) * math.sqrt(self.coords[0] ** 2 + self.coords[1] ** 2),
                                                self.creature.position[1] + math.sin(
                                                    direction_facing * math.pi / 180) * math.sqrt(
                                                    self.coords[0] ** 2 + self.coords[1] ** 2)])

        object_angles = []
        for i in objects_around:
            ### Takes the corner angles given by world.space_near and puts them into a list
            object_angles.append([angle_measure([i[1], i[0]]),
                                  angle_measure([i[3], i[2]]),
                                  angle_measure([i[5], i[4]]),
                                  angle_measure([i[7], i[6]]),
                                  i[8],
                                  i[9]
                                  ])
        objects_seen = []
        for i in object_angles:
            for ii in i:
                if ii - self.direction < 180 and ii - self.direction > 0:
                    self.objects_seen.append(i[5], i[6], angle_measure([i[6][1], i[6][0]])), i[9]

class GeneralSensor:
    def __init__(self, creature, coords, direction):
        pass





class CreatureSensor:
    def __init__(self, creature):
        pass


class ObstacleSensor:
    def __init__(self, creature):
        pass

class FoodSensor:
    def __init__(self, creature):
        pass




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
        direction = math.atan(coords[1] / coords[0]) * 180 / math.pi
        if coords[0] < 0:
            direction += 180


    return direction
