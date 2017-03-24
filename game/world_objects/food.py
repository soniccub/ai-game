
class Food:
    color = "#FFFF00"
    def __init__(self, position, amount,frame):
        self.amount = amount
        self.position = position
        self.size = [2, 2]
        self.frame = frame
    def check_if_under(self, block_center, block_size, creature):

        if block_center[0] - block_size/2 < self.position[0] < block_center[0] + block_size/2 and \
                                        block_center[1] - block_size/2 < self.position[1] < block_center[1] + block_size/2:
            creature.food += self.amount
            if creature.food > creature.food_max:
                creature.food = creature.food_max

    def draw(self):
        temp_cord = self.frame.coord_switch(self.position)
        if self.frame.position_on_screen(temp_cord, self.size):
            self.frame.frame.create_rectangle(temp_cord[0] - self.size[0] / 2, temp_cord[1] - self.size[1] / 2,
                                              temp_cord[0] + self.size[0] / 2, temp_cord[1] + self.size[1] / 2,
                                              fill=self.color)

