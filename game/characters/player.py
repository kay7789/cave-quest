from .character import Character
from ..commands.actions import slash, pass_turn, smite

class Player(Character):
    def __init__(self, quest):
        super().__init__(quest)
        self.name = "Joe"
        self.max_health = 20
        self.health = self.max_health
        self.strength = 3
        self.dexterity = 20
        self.magic_power = 1
        self.armor = 0
        self.moves = {"slash": slash.Slash(), "smite": smite.Smite(), "pass": pass_turn.PassTurn()}

    #print quest screen
    #define a variable that tracks if the command was successfully used, set it to false
    #loop until a command was successfully used.
    #print command prompt
    #call command_used function with user input, set the return value to the command used variable
    #after the loop, print quest screen
    def use_moves(self):
        self.quest.print_screen()
        command_used = False
        while command_used is False:
            print("your turn! (type \"help\" to see list of commands)")
            command_used = self.check_command(input())
        self.quest.print_screen()

    def check_command(self, input:str) -> bool:
        input = input.lower()
        if input == "help":
            pass #print command description
        #check if command is a move
        for move in self.moves.values():
            if move.name == input:
                #make sure player is in combat
                if self.quest.combat is None:
                    print("You are not in combat!")
                    return False
                #make sure the selected move is off cooldown
                if not move.is_usable():
                    print(f"{move.name} is on cooldown for {move.cooldown} turns!")
                    return False
                #write to the quest events the string that activating the move returns
                self.quest.add_event(move.activate(self, self.quest.combat.enemy))
                return True
        return False