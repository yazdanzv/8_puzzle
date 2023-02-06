from Node import Node


class Expand:

    def __init__(self, node: Node, goal: list):
        self.start_node: Node = node
        self.actions = {(-1, 0): 'Up', (1, 0): 'Down', (0, -1): 'Left', (0, 1): 'Right'}
        self.queue = []
        self.goal = goal

    def find_index(self, node: Node, num: str) -> object:
        index = node.puzzle.find(num)
        i = index // 3
        j = index - i * 3
        return i, j

    def h_manhattan(self, node: Node):
        h = 0

        for k in range(len(node.puzzle)):
            i, j = self.find_index(node.puzzle, str(k))
            x, y = self.find_index(self.goal, str(k))
            h += abs(i - x) + abs(j - y)

        return h

    def h_miss_place(self, node: Node):
        h = 0

        for k in range(len(node.puzzle)):
            i, j = self.find_index(node.puzzle, str(k))
            x, y = self.find_index(self.goal, str(k))
            if i != x and j != y:
                h += 1

        return h

    def g(self, node: Node):
        return node.depth

    def f(self, node: Node):
        g = self.g(node)
        h = self.h_manhattan(node)
        f = g + h
        return f

    def find_index(self,node: Node, num: str):
        index = node.puzzle.find(num)
        i = index // 3
        j = index - i * 3
        return i, j

    def find_max(self):
        max = self.f(self.queue[0])
        max_node = self.queue[0]
        for node in self.queue:
            if max < self.f(node):
                max = self.f(node)
                max_node = node
        return max, max_node

    def get_possible_action(self, node: Node):
        i, j = self.find_index("0")
        action_list = self.actions.keys()
        possible_actions = []
        for action in action_list:
            if not ((i + action[0] > 2) or (i + action[0] < 0) or (j + action[1] > 2) or (j + action[1] < 0)):
                possible_actions.append(self.actions[action])
        return possible_actions

    def expand(self):
        pass
