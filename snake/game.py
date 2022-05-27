import random
from input_function import *
from custom_strategy import *

class Game:
    def __init__(self, strat):
        self.strat = strat
        self.board = [[' ' for i in range(0,10)] for i in range(0,10)]
        self.snake = [(4,1),(4,2),(4,3)]
        self.score = 3
        self.berry_location = None
        self.number_of_turns = 0
    


    def place_random_berry(self):
        open_spaces = []
        for i in range(0,10):
            for j in range(0,10):
                if self.board[i][j] == ' ':
                    open_spaces.append((i,j))
        self.berry_location = random.choices(open_spaces)[0]
    


    def is_end(self):
        if len(list(set(self.snake))) != len(self.snake):
            return True
        elif self.snake[-1][1] not in range(10):
            return True
        elif self.snake[-1][0] not in range(10):
            return True
        else:
            return False
    


    def make_move(self):
        return self.strat(self.snake)
    


    def run(self):
        self.place_random_berry()
        active_game = True
        while active_game == True:
            for i in range(0,10):
                for j in range(0,10):
                    self.board[i][j] = ' '
            self.board[self.berry_location[0]][self.berry_location[1]] = 'b'
            for segment in self.snake:
                self.board[segment[0]][segment[1]] = 'O'
            self.board[self.snake[-1][0]][self.snake[-1][1]] = 'e'
            for spot in self.board:
                print(spot)
            print('------------------------------')
            player_move = self.make_move()
            board_move = None
            if player_move == 'w':
                board_move = (self.snake[-1][0] - 1, self.snake[-1][1])
                self.number_of_turns += 1
            elif player_move == 's':
                board_move = (self.snake[-1][0] + 1, self.snake[-1][1])
                self.number_of_turns += 1
            elif player_move == 'a':
                board_move = (self.snake[-1][0], self.snake[-1][1] - 1)
                self.number_of_turns += 1
            elif player_move == 'd':
                board_move = (self.snake[-1][0], self.snake[-1][1] + 1)
                self.number_of_turns += 1
            self.snake.append(board_move)
            if self.is_end() == True:
                active_game == False
                return 'score: ' + str(self.score - 3) + ', number of turns: ' + str(self.number_of_turns)
            if self.berry_location in self.snake:
                self.score += 1
                if self.score == 100:
                    active_game == False
                if self.score != 100:
                    self.place_random_berry()
            self.snake = self.snake[-self.score:]


a = Game(custom_strategy)
print(a.run())