class Player:
    def __init__(self, strategy):
        self.strategy = strategy
        self.player_number = None

    def choose_move(self, board): 
        return self.strategy(board)


# does the player class stay the same (as above)? Or is it how i did it below


class RandomPlayer:
    def __init__(self):
        self.player_num = None
    
    def choose_move(self, board):
        board = [state[i:i+7] for i in range(0,42,7)]
        
        
        columns = [[self.board[i][j] for i in range(6)] for j in range(7)]

        
        open_spaces = []
        # for i in range(len(board)):
        #     for j in range(len(board[i])):
        #         if board[i][j] == 0:
        #             open_spaces.append((i,j))
        return random.choices(open_spaces)[0]