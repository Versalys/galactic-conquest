from space_objects import *

class HUD:
    def __init__(self):
        self.clicked_obj = None
    
    def draw(self, coords, width, height):
        if isinstance(self.clicked_obj, SpaceShip):
            hp = self.clicked_obj.get_hp()
            max_hp = self.clicked_obj.get_max_hp()
            bar_percent = hp/max_hp
            name = self.clicked_obj.get_name()
            
    def update_clicked_obj(self, obj):
        self.clicked_obj = obj
