from .combat_action import CombatAction

import random

class PassTurn(CombatAction):
    def __init__(self):
        super().__init__()
        self.name = "pass"
        self.max_cooldown = 0
        self.cooldown = 0

    def activate(self, user, target=None) -> str:
        return f"{user.name} passes their turn"
        