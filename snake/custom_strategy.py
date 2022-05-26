def custom_strategy(board, snake):
    number_of_turns = 0
    if number_of_turns < 6:
        if snake[-1] == (4,3) or snake[-1] == (3,3) or snake[-1] == (2,3):
            number_of_turns += 1
            return 'w'
        if snake[-1] == (1,3) or snake[-1] == (1,2) or snake[-1] == (1,1):
            number_of_turns += 1
            return 'a'
    for i in range(1,9):
        if snake[-1] == (i,0):
            number_of_turns += 1
            return 's'
    if number_of_turns == 14:
        number_of_turns += 1
        return 'd'
    for i in range(1,9):
        if snake[-1] == (i,1):
            number_of_turns += 1
            return 'w'
    









    move = input()
    while move not in ['w','a','s','d']:
        print('move not valid')
        move = input()
    return move