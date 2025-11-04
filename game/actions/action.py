import random

class Action():
    def __init__(self):
        self.name = "Action"
        self.max_cooldown = 3
        self.cooldown = 0
        self.damage_bonus = 1
        self.damage_range = (-1, 1)

    def is_usable(self):
        return self.cooldown == 0

    def activate(self, user, target):
        pass

    def find_damage_amount(self, user, target):
        return user.get_strength() + self.damage_bonus - target.get_armor() + random.randint(self.damage_range)