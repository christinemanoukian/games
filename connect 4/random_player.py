import random

class RandomPlayer:
    def __init__(self):
        self.player_num = None

    def choose_move(self, state):
        board = [state[i:i+7] for i in range(0,42,7)]  
        columns = get_columns(board)

        
            
        open_spaces = []
        for column in columns:
            index_of_zero = get_index_of_zero(column)
            if index_of_zero is not False:
                open_spaces.append((column.index(0), columns.index(column)))
                # (how high it is (the row), which column)

        return random.choices(open_spaces)[0]


def get_index_of_zero(column):
    zeroes = 0
    for num in column:
        if num == 0:
            zeroes += 1
            return column.index(0)
            break
    if zeroes == 0:
        return False


def get_columns(board):
    columns = [[board[i][j] for i in range(6)] for j in range(7)]
    for column in columns:
        column = reversed(column)
    return columns
