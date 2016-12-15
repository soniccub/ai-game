
import random
### This is the tree object

### It produces food over time

### blocks way, adds protection



class Tree:
    possible_color = ["#00ff00",
"#00e500",
"#00cc00",
"#00b200",
"#009900",
"#007f00",
"#006600",
"#004c00",
"#003300",
"#001900",
"#000000",
]

    def __init__(self,position, frame):

        self.position = position
        self.food = 10
        self.size = [10, 10]
        self.frame = frame
        self.draw_set()

    def tick(self):



        if self.food < 100:
            self.food += 0.1

    def space_taken(self, position):
        if (position[0] > self.size[0] + self.position[0] and position[1] > self.size[1] + self.position[1]) or \
                (position[0] > -self.size[0] + self.position[0] and position[1] > -self.size[1] + self.position[1] ) :
            return True

        return False

    def draw_set(self):
        self.color = random.choice(self.possible_color)

    def draw(self):
        temp_cord = self.frame.coord_switch(self.position)
        #print(temp_cord)
        if self.frame.position_on_screen(temp_cord, self.size):


            self.frame.frame.create_rectangle(temp_cord[0] - self.size[0] / 2, temp_cord[1] - self.size[1] / 2,
                                              temp_cord[0] + self.size[0] / 2, temp_cord[1] + self.size[1] / 2,
                                              fill=self.color)








