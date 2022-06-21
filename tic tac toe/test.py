import sys
sys.path.append('tic tac toe')
from game import *
from player import *
from strategies import *
from class_strategies import *


wins = {1: 0, 2: 0, 'ties': 0}
for i in range(1):
    player1 = Player(custom_strategy_function)
    player2 = Player(custom_strategy_function)
    game = Game(player1, player2, log=True)
    game.run()

    if type(game.winner) is int:
        wins[game.winner] += 1
    else:
        wins['ties'] += 1
print(wins)