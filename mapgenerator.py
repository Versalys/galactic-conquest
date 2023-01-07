from space_objects import *
from spaceships import *
import random

class Generator:
    def randomize_coords(self, x_bound, y_bound):
        l = []
        for i in range(x_bound*y_bound):
            l.append((i % x_bound, i // y_bound))
        random.shuffle(l)
        return l

    def simple_generate_asteroids(self, x_bound, y_bound, num_aster, mineral_chance, excl=set()):
        coords = self.randomize_coords(x_bound, y_bound)
        i = 0 # how far we are in gen
        k = 0 # index in coord list
        gen = set()
        while i < num_aster and k < len(coords):
            if coords[k] in excl: # exlcuded tile from generation
                k += 1
                continue

            is_mineral = True if random.random() < mineral_chance else False
            
            gen.add(Asteroid(coords[k][0], coords[k][1], is_mineral))
            k += 1
            i += 1
        return gen
