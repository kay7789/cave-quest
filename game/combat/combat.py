import time

class Combat:
    def __init__(self, quest, enemy):
        self.quest = quest
        self.player = quest.player
        self.enemy = enemy

    #loop until the player or the enemy dies
    #run the player or enemy "on turn start" comand when it is their turn
    #wait one second after each turn
    #call combat ended on quest when the loop is broken
    def start_combat(self):
        while self.player.is_alive() and self.enemy.is_alive():
            self.player.on_turn_start()
            time.sleep(1.0)
            if self.player.is_alive() and self.enemy.is_alive():
                self.enemy.on_turn_start()
                time.sleep(1.0)
        self.quest.combat_ended()

    #print both the player and the enemies names and current health
    def print_combat(self):
        print(f"{self.enemy.name.upper()}")
        print(f"{self.enemy.health}/{self.enemy.max_health}") # enemy health bar
        print()
        print(f"{self.player.health}/{self.player.max_health}") # player health bar
        print(f"{self.player.name.upper()}")

