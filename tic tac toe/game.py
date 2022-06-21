import random

class Game:
    def __init__(self, player1, player2, seed=False, log=False):
        self.p1 = player1
        self.p2 = player2
        self.board = [[0 for j in range(3)] for i in range(3)]
        self.p1.player_number = 1
        self.p2.player_number = 2
        self.winner = None
        self.log = log
        if seed:
            random.seed(seed)

    def reverse_board_order(self, board):
        reversed_board = []
        for row in board:
            reversed_board.insert(0, row)
        return reversed_board
    
    def print_board(self):
        board = self.reverse_board_order(self.board)
        print(board)
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
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != 0:
            self.winner = self.board[0][0]
        if self.board[1][0] == self.board[1][1] == self.board[1][2] != 0:
            self.winner = self.board[1][0]
        if self.board[2][0] == self.board[2][1] == self.board[2][2] != 0:
            self.winner = self.board[2][0]
        if self.board[0][0] == self.board[1][0] == self.board[2][0] != 0:
            self.winner = self.board[0][0]
        if self.board[0][1] == self.board[1][1] == self.board[2][1] != 0:
            self.winner = self.board[0][1]
        if self.board[0][2] == self.board[1][2] == self.board[2][2] != 0:
            self.winner = self.board[0][2]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            self.winner = self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            self.winner = self.board[0][2]
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
                    print(self.winner)
                    print('wins')
                return self.winner
            self.move(self.p2)
            self.check_winner()
            if self.winner is not None:
                if self.log:
                    print(self.winner)
                    print('wins')
                return self.winner
        return self.winner

    def flatten_list(self, board):
        return [item for sublist in board for item in sublist]