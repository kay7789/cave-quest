from .. import helper_functions
from ..commands.actions import combat_action
import math

class Character:
    def __init__(self, quest):
        self.name = "nameless"
        self.max_health = 10
        self.health = self.max_health
        self.strength = 3
        self.temp_strength = 0
        self.end_of_turn_strength_bonus = 0
        self.dexterity = 3
        self.armor = 0
        self.evasion = 0
        self.moves = {}
        self.quest = quest

    def on_turn_start(self):
        for move in self.moves.values():
            move.reduce_cooldown(1)
        self.use_moves()
        self.on_turn_end()

    def take_damage(self, damage):
        self.health -= damage

    def get_strength(self):
        return self.strength + self.temp_strength
    
    # sets evasion based on dexterity, and puts it through a function so it cant get too large
    # function is (x * 170) / (x + sqrt( x^2 + 2500 ))
    def get_evasion(self):
        self.evasion = ( 170 * self.dexterity ) / ( self.dexterity + math.sqrt( self.dexterity ** 2 + 2500 ) )
        return self.evasion
    
    def on_turn_end(self):
        self.temp_strength = 0
        self.temp_strength += self.end_of_turn_strength_bonus
        self.end_of_turn_strength_bonus = 0

    def is_alive(self):
        return self.health > 0