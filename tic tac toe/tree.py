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
        self.leaf_node_count = 0


    def build_tree(self):
        root_node = self.root_node
        queue = [root_node]
        visited = [root_node]
        while queue != []:
            current_node = queue[0]
            if current_node.winner is None:
                open_spaces = self.check_for_open_spaces(current_node.state)
                print(open_spaces)
                for possible_move in open_spaces:
                    current_board_state = list(current_node.state)
                    player = current_node.player
                    print(current_board_state)
                    current_board_state[possible_move[0]][possible_move[1]] = player
                    print(current_board_state) #this is right
                    print(current_node.state) #this should still be the empty board but it's changing still
                    new_node = Node(current_board_state)
                    current_node.children.append(new_node)
                    print(current_node.children)
                    new_node.parent = current_node
                    if new_node not in visited:
                        queue.append(new_node)
                    visited.append(new_node)
            self.leaf_node_count += len(current_node.children)
            queue.remove(current_node)


    
    def check_for_open_spaces(self, state):
        open_spaces = []
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    open_spaces.append((i,j))
        return open_spaces

    
tree = TicTacToeTree()
tree.build_tree()
print(tree.leaf_node_count)
# leaf_node_count = 0
# root_node = tree.root_node
# queue = [root_node]
# visited = [root_node]
# while queue != []:
#     current_node = queue[0]
#     for child_node in current_node.children:
#         if child_node.children == []:
#             leaf_node_count += 1
#         if child_node not in visited:
#             queue.append(child_node)
#             visited.append(child_node)
#     queue.remove(current_node)
# print(leaf_node_count)