'''
Defines the board class. Keeps track of all of the items in play and
provides an interface for interacting with them.
'''

'''
Defines the main board of GC.
'''

import pygame as pg
from mapgenerator import Generator
from space_objects import *

class Board:
    def __init__(self, x_bound, y_bound, display, turn, window_offset = (0,0)):
        self.objects = set()
        self.selected_ship = None

        self.turn = turn
        
        self.y_bound = y_bound
        self.x_bound = x_bound
        self.display = display
        win_size = display.get_size()
        self.tile_width = win_size[0] / self.x_bound
        self.tile_height = win_size[1] / self.y_bound
        self.window_offset = (0, 0) # should change this to be at a sensible point in the map. Like in the mid.

    def add_obj(self, obj):
        self.objects.add(obj)

    def tiles_to_pixels(self, coords):
        return coords[0]*self.tile_width + self.window_offset[0], \
            coords[1]*self.tile_height + self.window_offset[1]

    def pixels_to_tiles(self, coords):
        return (coords[0]-self.window_offset[0])//self.tile_width, \
            (coords[1]-self.window_offset[1])//self.tile_height

    """
    we are not going to be doing drawing in the classes for now.
    Instead, we will get the image, coordinates. We can scale in the board code
    """
    def draw(self, surface):
        # do decorative objects here
        # (stars, world bounds, non spaceobject stuff)
        for obj in self.objects:
            coords = obj.get_position()
            
            # get spaceship image here (color temp)
            color = obj.get_drawable()
            
            left, top = self.tiles_to_pixels(coords)
            
            pg.draw.rect(surface, color, pg.Rect(left, top, self.tile_width, self.tile_height),  0)

            # DRAW HUD

    def get_object_at_pixels(self, pixel):
        coords = self.pixels_to_tiles(pixel)
        for obj in self.objects:
            if obj.get_position() == coords:
                return obj
        return None

    def simple_generate_map(self, num_aster=-1, mineral_chance=.2, excl=set()):
        if num_aster == -1:
            num_aster = (self.x_bound*self.y_bound)//10
        generator = Generator()
        self.objects = generator.simple_generate_asteroids(self.x_bound, self.y_bound, num_aster,
                                                           mineral_chance, excl)

    def update_window_position(self, coords):
        self.window_offset = coords
        # print("updating offset with ", self.window_offset)

    def select_spaceship(self, ship):
        self.selected_ship = ship

    def change_turn(self):
        if self.turn == 'red':
            self.turn = 'blue'
        else:
            self.turn = 'red'

    def move_spaceship(self, direction):
        if not isinstance(self.selected_ship, MovableSpaceShip) or \
           self.selected_ship.get_team() != self.turn:
            return False
        assert 0 <= direction <= 3

        coords = self.selected_ship.get_position()
        if direction == 0: # technically inefficient. Doing this twice.
            coords = coords[0], coords[1]-1
        elif direction == 1:
            coords = coords[0]+1, coords[1]
        elif direction == 2:
            coords = coords[0], coords[1]+1
        elif direction == 3:
            coords = coords[0]-1, coords[1]
        for obj in self.objects:
            if obj.get_position() == coords:
                return False
        return self.selected_ship.move_ship(direction)
