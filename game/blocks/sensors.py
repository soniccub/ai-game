### Types of sensors each creature has
import math


class Sensor:
    activatable = False
    type = "sensor"

    def __init__(self, creature, position, coords, type, sense_detail):
        self.y_edges = []
        self.x_edges = []
        self.sense_detail = sense_detail  ### Every level gives one extra neuron to the brain for that eye range of 1-10
        self.creature = creature
        self.world = self.creature.creatures.main.world
        self.coords = coords
        self.position = position
        self.sense_direction = angle_measure(
            coords) + self.creature.direction  ## So that it can do the object sense thing in the right direction
        self.direction = angle_measure(coords)  ### for the drawing
        self.food_storage = 25

        self.sensortype = type
        self.type_set(self.sensortype)
        self.max_sense_distance = 10 * sense_detail

    def sense(self):
        object_list = []
        object_list.append(self.world_object_sense())

        return object_list

    def world_object_sense(self):
        object_angles = []
        objects_seen = []

        direction_facing = self.sense_direction
        if self.sensor.world_object_see:
            objects_around = self.world.space_near([self.creature.position[0] + math.cos(
                direction_facing * math.pi / 180) * math.sqrt(self.coords[0] ** 2 + self.coords[1] ** 2),
                                                self.creature.position[1] + math.sin(
                                                    direction_facing * math.pi / 180) * math.sqrt(
                                                    self.coords[0] ** 2 + self.coords[1] ** 2)])

            for i in objects_around:
            ### Takes the corner angles given by world.space_near and puts them into a list
                object_angles.append([angle_measure([i[1], i[0]]),
                                  angle_measure([i[3], i[2]]),
                                  angle_measure([i[5], i[4]]),
                                  angle_measure([i[7], i[6]]),
                                  i[8],
                                  i[9]])

        for i in object_angles:

            for ii in i:

                if type(ii) == float or type(ii) == int:
                    objects_seen.append([ii, i[5]])

        if self.sensor.food_see:
            food_around = self.world.food_around([self.creature.position[0] + math.cos(
                direction_facing * math.pi / 180) * math.sqrt(self.coords[0] ** 2 + self.coords[1] ** 2),
                                                    self.creature.position[1] + math.sin(
                                                    direction_facing * math.pi / 180) * math.sqrt(
                                                    self.coords[0] ** 2 + self.coords[1] ** 2)])
            for i in food_around:
                objects_seen.append([angle_measure([i[0], i[1]]), [i[0], i[1]]])
        if self.sensor.creature_see:
            for i in self.creature.creatures.creatures_list:
                objects_seen.append([angle_measure([-i.position[0]+self.creature.position[0],-i.position[1]-self.creature.position[1]]),
                                     [-i.position[0]+self.creature.position[0],-i.position[1]-self.creature.position[1]]])





        return objects_seen

    def type_set(self, sensortype):

        if sensortype == "GeneralSensor":
            self.sensor = GeneralSensor
        elif sensortype == "CreatureSensor":
            self.sensor = CreatureSensor
        elif sensortype == "ObstacleSensor":
            self.sensor = ObstacleSensor
        elif sensortype == "FoodSensor":
            self.sensor = FoodSensor

        else:
            self.sensor = GeneralSensor
            print("sensor name not correct", self)

        self.color = self.sensor.color

    def upkeep(self):
        self.creature.food -= 2


class GeneralSensor:
    color = "#0000FF"
    world_object_see = True
    creature_see = True
    food_see = True
    type = "Sensor"

    def __init__(self):
        pass

    def objects_to_input(self, objects_seen):
        pass


class CreatureSensor:
    color = "#FF0000"
    world_object_see = False
    creature_see = True
    food_see = False
    type = "Sensor"

    def __init__(self):
        pass


class ObstacleSensor:
    color = "#00FF00"
    world_object_see = True
    creature_see = True
    food_see = False
    type = "Sensor"

    def __init__(self):
        pass


class FoodSensor:
    color = "#FFA500"
    world_object_see = False
    creature_see = False
    food_see = True
    type = "Sensor"

    def __init__(self):
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
    if direction < 0:
        direction += 360

    return direction
