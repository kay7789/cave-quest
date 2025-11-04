from game import helper_functions
from ..actions import action

print(action)

class Character():
    def __init__(self):
        self.health = 10
        self.strength = 3
        self.dexterity = 3
        self.armor = 0
        self.evasion = 0

    def get_health(self):
        return self.health
    
    def take_damage(self, damage):
        self.health -= damage

    def get_strength(self):
        return self.strength
    
    def get_armor(self):
        return self.armor
    
    def get_dexterity(self):
        return self.dexterity
    
    # sets evasion based on dextarity, and puts it through an ease function so it cant get too high
    def get_evasion(self):
        self.evasion = helper_functions.ease_out_circ(self.dexterity * 5)
        return self.evasion