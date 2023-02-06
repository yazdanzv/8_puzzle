import copy


class Node:
    puzzle: list

    def __init__(self, puzzle: list, parent: list, depth: int):
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



