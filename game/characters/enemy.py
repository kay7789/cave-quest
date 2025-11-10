from .character import Character

class Enemy(Character):
    def __init__(self, quest):
        super().__init__(quest)

    def use_moves(self):
        for move in self.moves.values():
            if move.is_usable():
                self.quest.add_event(move.activate(self, self.quest.player))
                return