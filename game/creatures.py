class Creatures:


    def __init__(self, size, main, frame, screen_size):
        return
        self.creatures_list = []
        self.size = size
        self.main = main
        self.frame = frame


        self.creature_create()
    def creature_create(self):
        ### For every set of 20 spaces
        for i in range(-self.size[0]/2, self.size[0]/2, 20):
            for ii in range(-self.size[1]/2, self.size[1]/2, 20):
                pass

    def generation(self):
        pass


    def tick(self):
        pass

    def draw(self):
        pass