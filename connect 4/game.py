import random
import sys
sys.path.append('tic tac toe')
from player import *
from strategies import *

class Game:
    def __init__(self, player1, player2, seed=False, log=False):
        self.p1 = player1
        self.p2 = player2
        self.board = [[0 for j in range(7)] for i in range(6)]
        self.p1.player_number = 1
        self.p2.player_number = 2
        self.winner = None
        self.log = log
        if seed:
            random.seed(seed)
    
    def print_board(self):
        print("\n-------")
        for row in self.board:
            for element in row[:-1]:
                print(element, end="  ")
            print(row[-1])
        print("-------")

    def move(self, player):
        if self.log:
            print(f'Fetching move from player {player.player_number}')
        
        x = player.choose_move(self.flatten_list(self.board.copy()))
        if type(x) != tuple:
            i,j = x//3, x%3
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
        rows = len(board)
        columns = len(board[0])

        # check horizontal spaces
        for y in range(rows):
            for x in range(columns - 3):
                if board[x][y] == 0 and board[x+1][y] == 0 and board[x+2][y] == 0 and board[x+3][y] == 0:
                    self.winner = board[x][y]

        # check vertical spaces
        for x in range(columns):
            for y in range(rows - 3):
                if board[x][y] == 0 and board[x][y+1] == 0 and board[x][y+2] == 0 and board[x][y+3] == 0:
                    self.winner = board[x][y]

        # check diagonal spaces
        for x in range(columns - 3):
            for y in range(3, rows):
                if board[x][y] == 0 and board[x+1][y-1] == 0 and board[x+2][y-2] == 0 and board[x+3][y-3] == 0:
                    self.winner = board[x][y]

        for x in range(columns - 3):
            for y in range(rows - 3):
                if board[x][y] == 0 and board[x+1][y+1] == 0 and board[x+2][y+2] == 0 and board[x+3][y+3] == 0:
                    self.winner = board[x][y]


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



game = Game(player1=Player(random_strategy_function), player2=Player(random_strategy_function), seed=False, log=False)
game.print_board()
print(game.check_for_open_spaces())