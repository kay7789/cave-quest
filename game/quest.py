from characters import player, goblin
from combat.combat import Combat

class Quest:
    def __init__(self):
        self.player = player.Player(self)
        self.combat

    def create_combat(self):
        self.combat = Combat(self, goblin.Goblin())
        self.combat.start_combat()