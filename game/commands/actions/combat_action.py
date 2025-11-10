from ..command import Command

import random

class CombatAction(Command):
    def __init__(self):
        super().__init__()
        self.max_cooldown = 3
        self.cooldown = 0
        self.damage_bonus = 1
        self.damage_range = (-1, 1)

    #checks if this action is off cooldown, returns result
    def is_usable(self):
        return self.cooldown == 0

    def activate(self, user, target) -> str:
        return ""
    
    def damage_calculation(self, user, target):
        damage_total = user.get_strength() + self.damage_bonus - target.armor + random.randint(self.damage_range[0], self.damage_range[1])
        return damage_total
    
    def reduce_cooldown(self, amount: int):
        self.cooldown -= amount
        if self.cooldown < 0:
            self.cooldown = 0