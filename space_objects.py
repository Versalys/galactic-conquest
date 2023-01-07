'''
Defines various abstract classes for use.
'''

RED_MOTHER = (255, 0, 0)
BLUE_MOTHER = (0, 0, 255)
RED_NORMAL = (190, 0, 0)
BLUE_NORMAL = (0, 0, 255)
ASTEROID = (175, 180, 43)
ASTEROID_MIN = (150, 180, 230)

class SpaceObject(object):
    '''
    Masterclass for all game objects. Starships, asteroids, and motherships are
    derived from this class.
    '''
    def __init__(self, s_x, s_y, team):
        self.x = s_x
        self.y = s_y
        self.team = team

    def update_position(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y

    def get_drawable(self):
        raise NotImplementedError("Drawing is not implemented for SpaceObject")

    def get_name(self):
        raise NotImplementedError("Cannot get name for SpaceObject")

    def get_team(self):
        return self.team


class SpaceShip(SpaceObject):
    '''
    Defines the spaceship object. Is an abstract class for player controlled
    starships as well as the mothership: the objective of the game.
    '''

    def __init__(self, x, y, team, health):
        super().__init__(x,y, team)
        self.max_hp = health
        self.hp = health

    def get_hp():
        return self.hp

    def get_max_hp():
        return self.max_hp

    def damage(self, hp_lost):
        self.hp -= hp_lost
        if self.hp <= 0:
            return True
        return False
        

class MovableSpaceShip(SpaceShip):
    '''
    Defines the movable spaceship class
    Abstract of classes used for player controlled spaceships
    '''
    def __init__(self, x, y, team, health, orientation, movement):
        super().__init__(x, y, team, health)
        self.orientation = orientation
        self.max_mov = movement
        self.movement = movement

    def heal(heal):
        if self.hp + heal >= self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += heal

    def move_ship(self, direction):
        # 0 - up; 1 - right; 2 - down; 3 - up
        assert 0 <= direction <= 3
        if self.movement <= 0:
            return False
        self.movement -= 1
        if direction == 0:
            self.update_position(self.x, self.y-1)
        elif direction == 1:
            self.update_position(self.x+1, self.y)
        elif direction == 2:
            self.update_position(self.x, self.y+1)
        elif direction == 3:
            self.update_position(self.x-1, self.y)
        self.orientation = direction
        return True
        

class Asteroid(SpaceObject):
    def __init__(self, x, y, is_mineral, team="neither"):
        super().__init__(x,y, team)
        self.mineral = is_mineral
        self.team=team

    def make_mine(self, team):
        if self.team != 'neither':
            return False
        self.team = team
        return True

    def destroy_mine(self):
        self.team = 'neither'

    def get_drawable(self):
        return ASTEROID if not self.mineral else ASTEROID_MIN

class Mothership(SpaceShip):
    def __init__(self, x, y, team, health=2000):
        super().__init__(x, y, team, health)

    def get_drawable(self):
        if self.team == 'red':
            return RED_MOTHER
        if self.team == 'blue':
            return BLUE_MOTHER
        raise Exception("Tried to draw teamless mothership")

