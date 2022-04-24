from random import randrange
import random

def ben(board):
    move = 0
    if board[2] == board[6] != 0 and board[4] == 0:
        move = 4
    elif board[2] == board[4] != 0 and board[6] == 0:
        move = 6
    elif board[0] == board[1] != 0 and board[2] == 0:
        move = 2
    elif board[4] == board[6] != 0 and board[2] == 0:
        move = 2
    elif board[4] == board[8] != 0 and board[0] == 0:
        move = 0
    elif board[0] == board[2] != 0 and board[1] == 0:
        move = 1
    elif board[1] == board[2] != 0 and board[0] == 0:
        move = 0
    elif board[3] == board[4] != 0 and board[5] == 0:
        move = 5
    elif board[3] == board[5] != 0 and board[4] == 0:
        move = 4
    elif board[4] == board[5] != 0 and board[3] == 0:
        move = 3
    elif board[6] == board[7] != 0 and board[8] == 0:
        move = 8
    elif board[6] == board[8] != 0 and board[7] == 0:
        move = 7
    elif board[7] == board[8] != 0 and board[6] == 0:
        move = 6
    elif board[0] == board[3] != 0 and board[6] == 0:
        move = 6
    elif board[0] == board[6] != 0 and board[3] == 0:
        move = 3
    elif board[3] == board[6] != 0 and board[0] == 0:
        move = 0
    elif board[1] == board[4] != 0 and board[7] == 0:
        move = 7
    elif board[1] == board[7] != 0 and board[4] == 0:
        move = 4
    elif board[4] == board[7] != 0 and board[1] == 0:
        move = 1
    elif board[2] == board[5] != 0 and board[8] == 0:
        move = 8
    elif board[2] == board[8] != 0 and board[5] == 0:
        move = 5
    elif board[5] == board[8] != 0 and board[2] == 0:
        move = 2
    elif board[0] == board[4] != 0 and board[8] == 0:
        move = 8
    elif board[0] == board[8] != 0 and board[4] == 0:
        move = 4
    elif board[4] == 0:
        move = 4
    elif board[0] == 0:
        move = 0
    elif board[2] == 0:
        move = 2
    elif board[5] == 0:
        move = 5
    elif board[1] == 0:
        move = 1
    elif board[6] == 0:
        move = 6
    elif board[8] == 0:
        move = 8
    return move


def is_board_empty(board): 
     return board.count(board[0]) == len(board)

def is_move_possible(board): 
     possible = []
     for i in range(len(board)): 
          if board[i] != 0: 
               possible.append(i)
     return possible


def celeste(board):
     possible = is_move_possible(board)
     empty = is_board_empty(board)
     move = 0

    #4
     if board[0] != 0 and board[1] != board[2] != 0: 
          move = random.choice(possible)
     elif board[3] != 0 and board[4] !=0 and board[5] != 0: 
          move = random.choice(possible)

     elif board[6] != 0 and board[7] != 0 and board[8] != 0: 
          move = random.choice(possible)

     elif board[0] != 0 and board[3] != 0 and board[6] != 0: 
          move = random.choice(possible)

     elif board[1] != 0 and board[4] != 0 and board[7] != 0: 
          move = random.choice(possible)

     elif board[2] != 0 and board[5] != 0 and board[8] != 0: 
          move = random.choice(possible)

     elif board[0] != 0 and board[4] != 0 and board[8] != 0: 
          move = random.choice(possible)

     elif board[2] != 0 and board[4] != 0 and board[6] != 0: 
          move = random.choice(possible)

     elif board[3] == board[5] != 0 and board[4] == 0:
          move = 4
     elif board[1] == board[7] != 0 and board[4] == 0:
          move = 4
     elif board[2] == board[6] != 0 and board[4] == 0: 
          move = 4
     #0
     elif board[1] == board[2] != 0 and board[0] == 0: 
          move = 0 
     elif board[3] == board[6] != 0 and board[0] == 0: 
          move = 0 
     elif board[4] == board[8] != 0 and board[0] == 0: 
          move = 0 
     elif board[4] == board[6] != 0 and board[0] == 0: 
          move = 0 
     #2
     elif board[0] == board[1] != 0 and board[2] == 0:
          move = 2
     elif board[5] == board[8] != 0 and board[2] == 0: 
          move = 2
     #6
     elif board[7] == board[8] != 0 and board[6] == 0: 
          move = 6
     elif board[0] == board[3] != 0 and board[6] == 0:
          move = 6
     elif board[2] == board[4] != 0 and board[6] == 0: 
          move = 6
     #8
     elif board[6] == board[7] != 0 and board[8] == 0:
          move = 8
     elif board[2] == board[5] != 0 and board[8] == 0:
          move = 8
     elif board[0] == board[4] != 0 and board[8] == 0: 
          move = 8
     #1
     elif board[0] == board[2] != 0 and board[1] == 0:
          move = 1
     elif board[4] == board[7] != 0 and board[1] == 0: 
          move = 1
     #3
     elif board[4] == board[5] != 0 and board[3] == 0:
          move = 3
     elif board[0] == board[6] != 0 and board[3] == 0: 
          move = 3
     #5
     elif board[3] == board[4] != 0 and board[5] == 0:
          move = 5
     elif board[2] == board[8] != 0 and board[5] == 0: 
          move = 5
     #7
     elif board[6] == board[8] != 0 and board[7] == 0:
          move = 7
     elif board[4] == board[1] != 0 and board[7] == 0: 
          move = 7
     
     elif board[4] == 0: 
          move = 4
     elif board[0] == 0: 
          move = 0
     elif board[2] == 0: 
          move = 2
     elif board[6] == 0: 
          move = 6
     elif board[8] == 0: 
          move = 8
     elif board[1] == 0: 
          move = 1
     elif board[3] == 0: 
          move = 3
     elif board[5] == 0: 
          move = 5
     elif board[7] == 0: 
          move = 7
     return move
    

def elias(board):

    player_number = 2

    if board == [0 for _ in range(9)]:
        player_number = 1
    

    for j in range(3):
        i = 3 * j
        if board[j] == board[j + 3] != 0 and board[j + 6] == 0:  # columns
            return j + 6
        elif board[j] == board[j + 6] != 0 and board[j + 3] == 0:
            return j + 3
        elif board[j + 3] == board[j + 6] != 0 and board[j] == 0:
            return j
        elif board[i] == board[i + 1] != 0 and board[i + 2] == 0:  # rows
            return i + 2
        elif board[i] == board[i + 2] != 0 and board[i + 1] == 0:
            return i + 1
        elif board[i + 1] == board[i + 2] != 0 and board[i] == 0:
            return i

    if board[0] == board[4] != 0 and board[8] == 0:  # diagonal
        return 8
    elif board[4] == board[8] != 0 and board[0] == 0:
        return 0
    elif board[0] == board[8] != 0 and board[4] == 0:
        return 4
    elif board[2] == board[4] != 0 and board[6] == 0:  # anti-diagonal
        return 6
    elif board[2] == board[6] != 0 and board[4] == 0:
        return 4
    elif board[4] == board[6] != 0 and board[2] == 0:
        return 2

    if player_number == 1:

        if board == [0 for _ in range(9)]:
            return 4
        if board[0] == 0:
            return 0
        elif board[2] == 0:
            return 2
        elif board[6] == 0:
            return 6
        elif board[8] == 0:
            return 8

    if player_number == 2:

        if board[4] == 0:
            return 4
        elif board[1] == 0:
            return 1
        elif board[3] == 0:
            return 3
        elif board[5] == 0:
            return 5
        elif board[7] == 0:
            return 7



    random_move = random.randrange(0, 9)
    while board[random_move] != 0:
        random_move = random.randrange(0, 9)
    return random_move


def is_end_copy(board):
    for i in range(0,3):
        if board[3*i + 0] == board[3*i + 1] == board[3*i + 2] != 0:
            return "Player " + str(board[3*i + 0])
        if board[0 + i] == board[3 + i] == board[6 + i] != 0:
            return "Player " + str(board[0+i])

    if board[0] == board[4] == board[8] != 0:
        return "Player " + str(board[0])
    if board[2] == board[4] == board[6] != 0:
        return "Player " + str(board[2])

    if 0 not in board:
        return 'Tie'
    return False

def possible_moves(board):
    empty_spaces = []
    for i in range(0,len(board)):
        if board[i] == 0:
            empty_spaces.append(i)
    return empty_spaces
    
def is_almost_end(board):
    empty_spaces = possible_moves(board)
    p_one = []
    p_two = []
    ends = [p_one,p_two]
    #player 1's turn
    for b in range(1,3):
        for i in empty_spaces:
            tboard = list(board)
            tboard[i] = b
            if is_end_copy(tboard) not in ['Tie',False]:
                ends[b-1].append(i)
    return ends


def jeff(board):
    corners = [0,2,6,8]
    edges = [1,3,5,7]
    middle = [4]
    p_turn = 1 if len(possible_moves(board))%2 == 1 else 2
    if p_turn == 1:
        if len(possible_moves(board)) == 9:
            return 8 #takes corner
    if p_turn == 2 and len(possible_moves(board)) == 8:
        if board[4] == 0:
            return 4
        else:
            return 8
    '''-------------- set = 1 ended ----------------'''
    if p_turn == 1 and len(possible_moves(board)) == 9 - 2:
        i = board.index(p_turn+1)
        if i in middle:
            return 0
        elif i in corners:
            if i + board.index(1) == 8:
                return 2
            else:
                return 8 - i
        elif i in edges:
            return 4
            
    if p_turn == 2 and len(possible_moves(board)) == 9 - 3:
        if len(is_almost_end(board)[0]) == 0:
            for i in possible_moves(board):
                if i in corners:
                    return i
    '''-------------- set = 2 ended ----------------'''
    #print(p_turn)
    if p_turn == 1:
        if len(is_almost_end(board)[0]) != 0:
            return is_almost_end(board)[0][0]
        elif len(is_almost_end(board)[1]) != 0:
            return is_almost_end(board)[1][0]
        for corner in corners:
            if board[corner] == 0:
                return corner
        else:
            return possible_moves(board)[0]
    if p_turn == 2:
        if len(is_almost_end(board)[1]) != 0:
            return is_almost_end(board)[1][0]
        elif len(is_almost_end(board)[0]) != 0:
            return is_almost_end(board)[0][0]
        for corner in corners:
            if board[corner] == 0:
                return corner
        else:
            return possible_moves(board)[0]