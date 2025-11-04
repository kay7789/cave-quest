from action import Action

import random

class Slash(Action):
    def __init__(self):
        self.name = "Slash"
        self.max_cooldown = 3
        self.cooldown = 0
        self.damage_bonus = 1
        self.damage_range = (-1, 1)

    #compares a random number against the targets evasion
    #if number is less then evasion, enemy evaded attack and end the function with a print to console
    #calculates damage total with user strength, damage bonus, target armor, and a random number
    #damages target
    #prints message
    def activate(self, user, target):
        if target.get_evasion() > random.randint(1, 100):
            print(f"{target} evaded the attack!")
            return
        damage_total = user.strength + self.damage_bonus - target.armor + random.randint(self.damage_range)
        target.take_damage(damage_total)
        print(f"{user.name} used {self.name} on {target.name} for {damage_total} damage!")
        