""" Contains the GameTree and GameNode classes """
import copy

class GameTree():
    """ Tree of GameNodes """
    def __init__(self, root):
        self.root = root

    def build_tree(self):
        """ Builds out the whole tree """
        print(f"Building the tree")

        if self.root is None:
            print(f"You done gone fucked up.  Set root before building")
            return
        self.root.build_subtree()

class GameNode():
    """ A node in the game tree """

    def __init__(self, board, parent=None):
        self.parent = parent
        self.children = []
        self.board = board

    def add_child(self, child):
        self.children.append(child)

    def get_successors(self):
        return self.children

    def evaluate(self):
        pass

    def build_subtree(self):
        """ Builds out the subtree from a given node """

        """ Add immediate children """
        for c in self.board.possible_moves():
            new_board = copy.deepcopy(self.board)
            new_board = new_board.place_piece(c)
            child = GameNode(new_board, self)
            self.add_child(child)

        """ Build subtree for each child """
        for s in self.get_successors():
            s.build_subtree()
