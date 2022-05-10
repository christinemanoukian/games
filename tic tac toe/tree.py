import sys
sys.path.append('tic tac toe')


class Node:
    def __init__(self, state):
        self.state = state
        self.player = 1 if self.state.count(1) == self.state.count(2) else 2
        self.winner = self.check_winner()
        self.parent = None
        self.children = []

    def check_winner(self):
        if self.state[0][0] == self.state[0][1] == self.state[0][2] != 0:
            return self.state[0][0]
        if self.state[1][0] == self.state[1][1] == self.state[1][2] != 0:
            return self.state[1][0]
        if self.state[2][0] == self.state[2][1] == self.state[2][2] != 0:
            return self.state[2][0]
        if self.state[0][0] == self.state[1][0] == self.state[2][0] != 0:
            return self.state[0][0]
        if self.state[0][1] == self.state[1][1] == self.state[2][1] != 0:
            return self.state[0][1]
        if self.state[0][2] == self.state[1][2] == self.state[2][2] != 0:
            return self.state[0][2]
        if self.state[0][0] == self.state[1][1] == self.state[2][2] != 0:
            return self.state[0][0]
        if self.state[0][2] == self.state[1][1] == self.state[2][0] != 0:
            return self.state[0][2]
        elif self.state.count(0) == 0:
                return 'tie'
        else:
            return None


class TicTacToeTree:
    def __init__(self):
        self.root_node = Node([[0 for j in range(3)] for i in range(3)])


    def build_tree(self):
        root_node = self.root_node
        queue = [root_node]
        visited = [root_node]
        while queue != []:
            current_node = queue[0]
            if current_node.winner is None:
                current_board_state = current_node.state
                player = current_node.player
                open_spaces = current_board_state.check_for_open_spaces()
                for possible_move in open_spaces:
                    new_current_board_state = list(current_board_state)
                    new_current_board_state[possible_move] = player
                    new_node = Node(new_current_board_state)
                    current_node.children.append(new_node)
                    new_node.parent = current_node
                    if new_node not in visited:
                        queue.append(new_node)
                    visited.append(new_node)
                queue.remove(queue[0])



    
    def check_for_open_spaces(self):
        open_spaces = []
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] == 0:
                    open_spaces.append((i,j))
        return open_spaces

    
tree = TicTacToeTree()
tree.build_tree()
