from action import Action

import random

class Slash(Action):
    def __init__(self):
        self.name = "Slash"
        self.max_cooldown = 3
        self.cooldown = 0
        self.damage_bonus = 1
        self.damage_range = (-1, 1)

    def activate(self, user, target):
        if target.get_evasion() > random.randint(1, 100):
            print(f"{target} evaded the attack!")
            return
        damage_total = user.strength + self.damage_bonus - target.armor + random.randint(self.damage_range)
        target.take_damage(damage_total)
        print(f"{user.name} used {self.name} on {target.name} for {damage_total} damage!")
        