from .combat_action import CombatAction

import random

class Enrage(CombatAction):
    def __init__(self):
        super().__init__()
        self.max_cooldown = 4
        self.cooldown = 2


    def activate(self, user, target=None) -> str:
        self.cooldown = self.max_cooldown
        user.end_of_turn_strength_bonus += 3
        return f"{user.name} gets angry, making them stronger next turn"