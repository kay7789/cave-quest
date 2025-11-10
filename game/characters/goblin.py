from .enemy import Enemy
from ..commands.actions import club, pass_turn, enrage

class Goblin(Enemy):
    def __init__(self, quest):
        super().__init__(quest)
        self.name = "goblin"
        self.max_health = 10
        self.health = self.max_health
        self.strength = 2
        self.dexterity = 4
        self.armor = 0
        self.moves = {"enrage": enrage.Enrage(), "slash": club.Club(), "pass": pass_turn.PassTurn()}
        self.quest = quest