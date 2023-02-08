class Node:
    puzzle: list

    def __init__(self, puzzle: list, parent: list = None, depth: int = None):
        self.puzzle: list = puzzle
        self.depth = depth
        self.children: list = []
        self.parent = parent

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def get_depth(self):
        return self.depth

    def get_puzzle(self):
        return self.puzzle

    def __eq__(self, other):
        if self.puzzle == other.puzzle:
            return True
        else:
            return False

    def __str__(self):
        ans = ""
        for i in range(0, len(self.puzzle), 3):
            ans += (self.puzzle[i] + " " + self.puzzle[i+1] + " " + self.puzzle[i+2] + "\n")
        return ans




