from .combat_action import CombatAction

import random

class Slash(CombatAction):
    def __init__(self):
        super().__init__()
        self.name = "slash"
        self.max_cooldown = 0
        self.cooldown = 0
        self.damage_bonus = 1
        self.damage_range = (-1, 1)
        self.accuracy = 1

    #compares a random number against the targets evasion
    #if number is less then evasion, enemy evaded attack and end the function with a print to console
    #calculates damage total with user strength, damage bonus, target armor, and a random number
    #damages target
    #returns message
    def activate(self, user, target) -> str:
        self.cooldown = self.max_cooldown
        if target.get_evasion() > random.randint(1, 100) * self.accuracy:
            return f"{user.name} used {self.name} on {target.name}, but {target.name} dodged the attack!"
        damage_total = self.damage_calculation(user, target)
        target.take_damage(damage_total)
        return f"{user.name} used {self.name} on {target.name} for {damage_total} damage!"

    def damage_calculation(self, user, target):
        return max(user.get_strength() + self.damage_bonus - target.armor + random.randint(self.damage_range[0], self.damage_range[1]), 0)