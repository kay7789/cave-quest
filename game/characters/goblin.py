from enemy import Enemy
from actions import slash

class Goblin(Enemy):
    def __init__(self):
        self.health = 6
        self.strength = 1
        self.dexterity = 5
        self.armor = 0
        self.moves = [slash.Slash()]

    def on_turn_start(self):
        pass