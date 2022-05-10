def random_strategy_function(state):
    board = [state[i:i+7] for i in range(0,42,7)]        
        
    columns = [[self.board[i][j] for i in range(6)] for j in range(7)]

        
    open_spaces = []
    # basically i need to go through each column, the first time a 0 approaches i need to add that ((i,j)) to open_spaces, then 
    # move on to the next column. If there are no 0's in a column, it's fine, just go to the next column



    return random.choices(open_spaces)[0]

















# going to make this a function before making it a class

# how do you call a class