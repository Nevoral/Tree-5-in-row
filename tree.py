
class board:
    def __init__(self, board, score):
        self.board = board
        self.score = score
    
    def get_board(self):
        return self.board

    def get_score(self):
        return self.score

class branch:
    def __init__(self):
        self.results = []

    def add_board(self):
        self.results.append(board)

    def delete_board(self, i):
        self.results.pop(i)

    def get_len(self):
        return len(self.results)

    def get_board(self, i):
        return self.results[i].get_board()

    def get_score(self, i):
        return self.results[i].get_score()

class level:
    def __init__(self):
        self.layers = []

    def get_numb_branch(self):
        return len(self.layers)

    def add_branch(self):
        self.layers.append(branch)
    
    def delete_branch(self, i):
        self.layers.pop(i)
    
    def get_branch(self, i):
        return self.layers[i]

class tree:
    def __init__(self):
        self.tree = []
    
    def get_numb_level(self):
        return len(self.tree)

    def add_level(self):
        self.tree.append(level)
    
    def delete_level(self, i):
        self.tree.pop(i)
    
    def get_level(self, i):
        return self.tree[i]