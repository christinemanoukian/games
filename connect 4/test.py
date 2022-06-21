import sys
sys.path.append('connect 4')
from game import *
from random_player import *
from custom_player import *
from strategies import *



wins = {1: 0, 2: 0, 'ties': 0}
for i in range(1):
    player1 = CustomPlayer()
    player2 = CustomPlayer()
    game = Game(player1, player2, log=True)
    game.run()
    if type(game.winner) is int:
        wins[game.winner] += 1
    else:
        wins['ties'] += 1
print(wins)

