
class Food:
    color = "#FFFF00"

    def __init__(self, position, amount, frame, world):
        self.world = world
        self.amount = amount
        self.position = position
        self.size = [2, 2]
        self.frame = frame

    def check_if_under(self, block_center, block_size, creature):


        if block_center[0] - block_size < self.position[0] < block_center[0] + block_size and \
                                        block_center[1] - block_size < self.position[1] < block_center[1] + block_size:
            creature.food += self.amount
            #print(block_center,self.position, "abc")
            if creature.food > creature.food_max:
                creature.food = creature.food_max
            creature.last_food = 0
            for i in range(len(self.world.new_food_list)):
                if self.world.new_food_list[i] == self:
                    self.world.new_food_list.pop(i)

                    break




    def draw(self):
        temp_cord = self.frame.coord_switch(self.position)
        if self.frame.position_on_screen(temp_cord, self.size):
            self.frame.frame.create_rectangle(temp_cord[0] - self.size[0] / 2, temp_cord[1] - self.size[1] / 2,
                                              temp_cord[0] + self.size[0] / 2, temp_cord[1] + self.size[1] / 2,
                                              fill=self.color)

