import copy
class Node:
    def __init__(self, puzzle: list):
        self.puzzle: list = puzzle
        self.depth = 0
        self.children = []
        self.parent = None
        self.actions = {(-1, 0): 'Up', (1, 0): 'Down', (0, -1): 'Left', (0, 1): 'Right'}

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def get_depth(self):
        return self.depth

    def get_puzzle(self):
        return self.puzzle

    def find_index_from_value(self, num: str):
        index = self.puzzle.find(num)
        i = index // 3
        j = index - i * 3
        return i, j

    def find_index_from_co(self, i, j):
        index = i * 3 + j
        return index

    def get_possible_actions(self):
        i, j = self.find_index_from_value("0")
        action_list = self.actions.keys()
        possible_actions = []
        for action in action_list:
            if not ((i + action[0] > 2) or (i + action[0] < 0) or (j + action[1] > 2) or (j + action[1] < 0)):
                possible_actions.append(self.actions[action])
        return possible_actions

    def expand(self, possible_actions):
        new_puzzles = []
        i, j = self.find_index_from_value("0")
        index_of_blank = self.find_index_from_co(i, j)
        for action in possible_actions:
            puzzle_copy = copy.deepcopy(self.puzzle)
            if action == 'Up':
                index = self.find_index_from_co(i - 1, j)
                puzzle_copy[index], puzzle_copy[index_of_blank] = puzzle_copy[index_of_blank], puzzle_copy[index]
                new_puzzles.append(puzzle_copy)
            elif action == 'Down':
                index = self.find_index_from_co(i + 1, j)
                puzzle_copy[index], puzzle_copy[index_of_blank] = puzzle_copy[index_of_blank], puzzle_copy[index]
                new_puzzles.append(puzzle_copy)
            elif action == 'Left':
                index = self.find_index_from_co(i, j - 1)
                puzzle_copy[index], puzzle_copy[index_of_blank] = puzzle_copy[index_of_blank], puzzle_copy[index]
                new_puzzles.append(puzzle_copy)
            elif action == 'Right':
                index = self.find_index_from_co(i, j + 1)
                puzzle_copy[index], puzzle_copy[index_of_blank] = puzzle_copy[index_of_blank], puzzle_copy[index]
                new_puzzles.append(puzzle_copy)
            else:
                raise Exception('No such Action!!!')


