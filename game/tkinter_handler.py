
### This handles many tkinter drawing interactions interactions
### Will take in set of coords, screen size and world cord system to determine if on screen


def if_on_screen(position, object_size, center_screen_position, screen_size):
    x = [position[0] + object_size[0] + center_screen_position[0],
         position[0] - object_size[0] + center_screen_position[0]]

    y = [position[1] + object_size[1] + center_screen_position[1],
         position[1] - object_size[1] + center_screen_position[1]]

    x_edge = [center_screen_position[0] + screen_size[0], center_screen_position[0] - screen_size[0]]
    y_edge = [center_screen_position[1] + screen_size[1], center_screen_position[1] - screen_size[1]]
    ### Takes the extreme edges

    if (x[0] < x_edge[0] and x[1] > x_edge[1]) and (y[0] < y_edge[0] and y[1] > y_edge[1]):
        return True
    ### Checks if the extreme edges are within the x and y boundries
    return False



### For coords written in relation to the world, not the screen
def coord_switch(coords, screen_position, screen_size):

    new_coords = [(coords[0] + screen_position[0]) + screen_size[0]/2,
                  screen_size[1]-(coords[1] - screen_position[1]) - screen_size[1]/2]


    return new_coords



