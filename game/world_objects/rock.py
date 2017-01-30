import random


### Rock
### Does nothing just like ur mom
### Just blocks the way

class Rock:
    possible_color = ["#f4a460", "#db9356", "#c3834c", "#aa7243", "#926239", "#7a5230",
                      "#614126", "#49311c", "#302013", "#181009", "#000000"]
    ### Colors from light brown to black for possible colors of the rock

    def __init__(self, position, frame):

        self.position = position
        self.food = 1
        self.size = [random.randrange(20), random.randrange(20)]
        self.frame = frame
        self.draw_set()

    def tick(self):
        pass

    def space_taken(self, position):
        if (position[0] > self.size[0] + self.position[0] and position[1] > self.size[1] + self.position[1]) or \
                (position[0] > - self.size[0] + self.position[0] and position[1] > -self.size[1] + self.position[1]):
            return True

        return False


    def draw_set(self):
        self.color = random.choice(self.possible_color)


    def draw(self):
            temp_cord = self.frame.coord_switch(self.position)
            if self.frame.position_on_screen(temp_cord, self.size):


                self.frame.frame.create_rectangle(temp_cord[0]-self.size[0]/2, temp_cord[1]-self.size[1]/2, temp_cord[0]+self.size[0]/2, temp_cord[1] + self.size[1]/2, fill=self.color)






