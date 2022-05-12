import sys
sys.path.append('tic tac toe')


class Node:
    def __init__(self, state):
        self.state = state
        self.player = 1 if sum(i.count(1) for i in self.state) == sum(i.count(2) for i in self.state) else 2
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
        count = 0
        for row in self.state:
            for space in row:
                if space == 0:
                    count += 1
        if count == 0:
            return 'tie'
        else:
            return None



class TicTacToeTree:
    def __init__(self):
        self.root_node = Node([[0 for j in range(3)] for i in range(3)])
        self.nodes = {'000000000': self.root_node}
        self.leaf_nodes = []
 

    def build_tree(self):
        root_node = self.root_node
        outcomes = {1: 0, 2: 0, 'tie': 0}
        queue = [root_node]
        while queue != []:
            current_node = queue[0]
            if current_node.winner is None:
                open_spaces = self.check_for_open_spaces(current_node.state)
                for possible_move in open_spaces:
                    current_board_state = self.copy_board_state(current_node.state)
                    current_board_state[possible_move[0]][possible_move[1]] = current_node.player
                    new_node = Node(current_board_state) 
                    if self.check_if_state_exists(current_board_state) == False:
                        new_node_state = self.board_to_string(new_node.state)
                        current_node.children.append(new_node)
                        new_node.parent = current_node
                        self.nodes[new_node_state] = new_node
                    queue.append(new_node)
            else:
                outcomes[current_node.winner] += 1
                self.leaf_nodes.append(current_node)
            queue.remove(current_node) 
        print(outcomes)

        

    def check_if_state_exists(self, state):
        if state in self.nodes.values():
            return True
        else:
            return False

    
    def board_to_string(self, state):
        state = [[str(i) for i in row] for row in state]

        return ''.join([''.join(row) for row in state])



    def copy_board_state(self, state):
        return [list(sublist) for sublist in state]


    
    def check_for_open_spaces(self, state):
        open_spaces = []
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    open_spaces.append((i,j))
        return open_spaces

    
tree = TicTacToeTree()
tree.build_tree()
leaf_nodes = len(tree.leaf_nodes)
print(leaf_nodes)
print(len(tree.nodes))