class Combat:
    def __init__(self, quest, enemy):
        self.quest = quest
        self.player = quest.player
        self.enemy = enemy

    def start_combat(self):
        while self.player.is_alive() and self.enemy.is_alive():
            self.player.on_turn_start()
            self.enemy.on_turn_start()

