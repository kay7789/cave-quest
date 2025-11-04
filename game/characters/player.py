from character import Character

class Player(Character):
    def __init__(self):
        self.health = 20
        self.strength = 3
        self.dexterity = 3
        self.armor = 0
        self.evasion = 0

    