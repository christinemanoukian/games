import random
import sys
sys.path.append('tic tac toe')
from player import *
from strategies import *

class Game:
    def __init__(self, player1, player2, seed=False, log=False):
        self.p1 = player1
        self.p2 = player2
        self.board = list(reversed([[0 for j in range(7)] for i in range(6)]))
        self.p1.player_number = 1
        self.p2.player_number = 2
        self.winner = None
        self.log = log
        if seed:
            random.seed(seed)

    
    def print_board(self):
        board = reversed(self.board)
        print("\n-------")
        for row in board:
            for element in row[:-1]:
                print(element, end="  ")
            print(row[-1])
        print("-------")

    def move(self, player):
        if self.log:
            print(f'Fetching move from player {player.player_number}')
        
        x = player.choose_move(self.flatten_list(self.board.copy()))
        if type(x) != tuple:
            i,j = x//7, x%7
        else:
            i,j = x

        if self.log:
            print(f'Updating board: player {player.player_number} moves into coordinates {i},{j}')

            
        open_spaces = self.check_for_open_spaces()
        if (i,j) in open_spaces:
            self.board[i][j] = player.player_number


        if self.log:
            self.print_board()


    def check_for_open_spaces(self):
        open_spaces = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    open_spaces.append((i,j))
        if self.log:
            print(f'Checking open spaces: {open_spaces}')
        return open_spaces


    def check_winner(self):
        board = self.board.copy()


        # Check horizontal locations for win
        for c in range(4):
            for r in range(6):
                if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] != 0:
                    self.winner = board[r][c]

        # Check vertical locations for win
        for c in range(7):
            for r in range(3):
                if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c] != 0:
                    self.winner = board[r][c]

        # Check positively sloped diaganols
        for c in range(4):
            for r in range(3):
                if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3] != 0:
                    self.winner = board[r][c]

        # Check negatively sloped diaganols
        for c in range(4):
            for r in range(3, 6):
                if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3] != 0:
                    self.winner = board[r][c]





        else:
            open_spaces = self.check_for_open_spaces()
            if open_spaces == []:
                self.winner = 'tie'
 


    def run(self):
        while self.winner is None:
            self.move(self.p1)
            self.check_winner()
            if self.winner is not None:
                if self.log:
                    print(self.winner, 'wins')
                return self.winner
            self.move(self.p2)
            self.check_winner()
            if self.winner is not None:
                if self.log:
                    print(self.winner, 'wins')
                return self.winner
        return self.winner

    def flatten_list(self, board):
        return [item for sublist in board for item in sublist]



# game = Game(player1=Player(random_strategy_function), player2=Player(random_strategy_function), seed=False, log=False)
# game.print_board()
# print(game.check_for_open_spaces())
