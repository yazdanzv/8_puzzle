from Node import Node
import copy


class Expand:

    def __init__(self, node: Node, goal: Node):
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
            i, j = self.find_index(node, str(k))
            x, y = self.find_index(self.goal, str(k))
            h += abs(i - x) + abs(j - y)

        return h

    def h_miss_place(self, node: Node):
        h = 0

        for k in range(len(node.puzzle)):
            i, j = self.find_index(node, str(k))
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

    @staticmethod
    def find_index(node: Node, num: str):
        index = node.puzzle.index(num)
        i = index // 3
        j = index - i * 3
        return i, j

    @staticmethod
    def find_index_from_co(node: Node, i, j):
        index = i * 3 + j
        return index

    def find_max(self):
        max = self.f(self.queue[0])
        max_node = self.queue[0]
        for node in self.queue:
            if max < self.f(node):
                max = self.f(node)
                max_node = node
        return max_node

    def get_possible_action(self, node: Node):
        i, j = self.find_index(node, "0")
        action_list = self.actions.keys()
        possible_actions = []
        for action in action_list:
            if not ((i + action[0] > 2) or (i + action[0] < 0) or (j + action[1] > 2) or (j + action[1] < 0)):
                possible_actions.append(self.actions[action])
        return possible_actions

    def find_children_puzzles(self, node: Node, possible_actions):
        new_puzzles = []
        print('possible actions')
        print(possible_actions)
        i, j = self.find_index(node, "0")
        index_of_blank = self.find_index_from_co(node, i, j)
        for action in possible_actions:
            puzzle_copy = copy.deepcopy(node.puzzle)
            print('puzzle copy')
            print(puzzle_copy)
            if action == 'Up':
                index = self.find_index_from_co(node, i - 1, j)
                puzzle_copy[index], puzzle_copy[index_of_blank] = puzzle_copy[index_of_blank], puzzle_copy[index]
                new_puzzles.append(puzzle_copy)
            elif action == 'Down':
                print('down')
                index = self.find_index_from_co(node, i + 1, j)
                print('index')
                print(index)
                puzzle_copy[index], puzzle_copy[index_of_blank] = puzzle_copy[index_of_blank], puzzle_copy[index]
                print('new puzzle copy')
                print(puzzle_copy)
                new_puzzles.append(puzzle_copy)
            elif action == 'Left':
                index = self.find_index_from_co(node, i, j - 1)
                puzzle_copy[index], puzzle_copy[index_of_blank] = puzzle_copy[index_of_blank], puzzle_copy[index]
                new_puzzles.append(puzzle_copy)
            elif action == 'Right':
                index = self.find_index_from_co(node, i, j + 1)
                puzzle_copy[index], puzzle_copy[index_of_blank] = puzzle_copy[index_of_blank], puzzle_copy[index]
                new_puzzles.append(puzzle_copy)
            else:
                raise Exception('No such Action!!!')
        print('new puzzles list')
        print(new_puzzles)
        return new_puzzles

    def find_children(self, node: Node):
        possible_actions = self.get_possible_action(node)
        children_puzzles = self.find_children_puzzles(node, possible_actions)
        for child_puzzle in children_puzzles:
            child = Node(child_puzzle, node, node.depth + 1)
            node.children.append(child)  # Not sure

    def update_queue(self, node):
        self.find_children(node)
        self.queue.extend(node.children)
        print('queue')
        

    @staticmethod
    def show_path(node: Node):
        node_copy = copy.deepcopy(node)
        ans = [node_copy]
        while node.parent is not None:
            ans.append(node_copy.parent)
            node_copy = copy.deepcopy(node_copy.parent)
        ans = ans.reverse()
        for i in ans:
            print(i)

    def solve(self):
        print('start')
        self.find_children(self.start_node)
        print('here')
        print(self.start_node.children)
        self.update_queue(self.start_node)
        print('here 2 ')
        max_node: Node = self.find_max()
        print("max node :")
        print(max_node)
        self.queue.remove(max_node)
        while True:
            print('while started')
            print(max_node.puzzle)
            print()
            print(self.goal.puzzle)
            if max_node.puzzle == self.goal.puzzle:
                self.show_path(max_node)
                break
            else:
                print('else entered')
                self.find_children(max_node)
                self.update_queue(max_node)
                max_node: Node = self.find_max()
                self.update_queue(max_node)
