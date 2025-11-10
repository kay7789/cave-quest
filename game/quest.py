from .characters import player, goblin
from .combat.combat import Combat
from . import helper_functions

class Quest:
    def __init__(self):
        self.player = player.Player(self)
        self.combat: Combat = None
        self.events = []

    #add the input text to the event list
    #remove the first item in the event list if its length is above 3
    #call print_screen()
    def add_event(self, text:str):
        self.events.append(text)
        if len(self.events) > 3:
            self.events.pop(0)
        self.print_screen()

    #clear the console
    #check if there is a current combat, if so, tells combat object to print its screen
    #loop over each item in the event list, printing each one
    def print_screen(self):
        helper_functions.clear_console()
        if self.combat is not None:
            self.combat.print_combat()
        for line in self.events:
            print(line)

    #defines a new combat object, using this Quest object and a Goblin object as perameters. (goblin object is temporary, it will later be a different enemy for each combat)
    #starts the combat
    def create_combat(self):
        self.combat = Combat(self, goblin.Goblin(self))
        self.combat.start_combat()

    #called when the combat ends
    #add "combat ended" to the event list
    def combat_ended(self):
        self.add_event("combat ended")