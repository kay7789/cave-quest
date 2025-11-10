from .slash import Slash

import random

class Club(Slash):
    def __init__(self):
        super().__init__()
        self.name = "club"
        self.max_cooldown = 0
        self.cooldown = 0
        self.damage_bonus = 0
        self.damage_range = (-1, 1)
        self.accuracy = 0.9

    def damage_calculation(self, user, target):
        return user.get_strength() + self.damage_bonus - target.armor + random.randint(self.damage_range[0], self.damage_range[1])