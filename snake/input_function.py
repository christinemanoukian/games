def input_function(snake):
    move = input()
    while move not in ['w','a','s','d']:
        print('move not valid')
        move = input()
    return move 