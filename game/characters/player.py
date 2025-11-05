from character import Character
from actions import slash

class Player(Character):
    def __init__(self, quest):
        self.name = "Joe"
        self.health = 20
        self.strength = 3
        self.dexterity = 3
        self.armor = 0 
        self.moves = [slash.Slash()]
        self.quest = quest

    def on_turn_start(self):
        print("your turn! (type \"help\" to see list of commands)")
        self.input_prompt()

    def input_prompt(self):
        while input(self.check_command()) is False:
            print("type \"help\" to see list of commands")

    def check_command(self, input:str):
        input = input.lower()
        for move in self.moves:
            if move.name == input:
                if not move.is_usable():
                    print(f"{move.name} is on cooldown for {move.cooldown} turns!")
                    return False
                move.activate(self, )
                return True