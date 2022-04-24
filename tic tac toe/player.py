class Player:
    def __init__(self, strategy):
        self.strategy = strategy
        self.player_number = None

    def choose_move(self, board): 
        return self.strategy(board)