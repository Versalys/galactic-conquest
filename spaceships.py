from space_objects import *

### SPACESHIP CONSTANTS ###
CRUISER_HP = 1000
CRUISER_MOV = 100

class Miner(MovableSpaceShip):
    pass

class Cloaker(MovableSpaceShip):
    pass

class Warship(MovableSpaceShip):
    pass

class Artillery(MovableSpaceShip):
    pass

class Cruiser(MovableSpaceShip):
    def __init__(self, x, y, team, orientation):
        super().__init__(x, y, team, CRUISER_HP, orientation, CRUISER_MOV)

    def get_drawable(self):
        if self.team == 'red':
            return RED_NORMAL
        if self.team == 'blue':
            return BLUE_NORMAL
        raise Exception("Tried to draw teamless starship")

class Harrasser(MovableSpaceShip):
    pass

class Sentinel(MovableSpaceShip):
    pass

class FlagShip(MovableSpaceShip): # may be sentinel??
    pass
