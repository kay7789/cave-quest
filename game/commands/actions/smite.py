from .slash import Slash

import random

class Smite(Slash):
    def __init__(self):
        super().__init__()
        self.name = "smite"
        self.max_cooldown = 3
        self.cooldown = 0
        self.damage_bonus = 2
        self.damage_range = (-1, 2)
        self.accuracy = 1.2

    def damage_calculation(self, user, target):
        return user.get_strength() + user.magic_power + self.damage_bonus - target.armor + random.randint(self.damage_range[0], self.damage_range[1])