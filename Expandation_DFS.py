from Node import Node
import copy


class Expand_DFS:

    def __init__(self, node: Node, goal: Node):
        self.start_node: Node = node
        self.actions = {(-1, 0): 'Up', (1, 0): 'Down', (0, -1): 'Left', (0, 1): 'Right'}
        self.queue = []
        self.goal = goal

    def find_index(self, node: Node, num: str):
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

    def find_next(self):
        next_node: Node = self.queue[0]
        for node in self.queue:
            if next_node.depth < node.depth:
                next_node = node
        return next_node

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
        i, j = self.find_index(node, "0")
        index_of_blank = self.find_index_from_co(node, i, j)
        for action in possible_actions:
            puzzle_copy = copy.deepcopy(node.puzzle)
            if action == 'Up':
                index = self.find_index_from_co(node, i - 1, j)
                puzzle_copy[index], puzzle_copy[index_of_blank] = puzzle_copy[index_of_blank], puzzle_copy[index]
                new_puzzles.append(puzzle_copy)
            elif action == 'Down':
                index = self.find_index_from_co(node, i + 1, j)
                puzzle_copy[index], puzzle_copy[index_of_blank] = puzzle_copy[index_of_blank], puzzle_copy[index]
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
        return new_puzzles

    @staticmethod
    def find_children_puzzle_list(node: Node):
        children_puzzles = []
        for child in node.children:
            if child.puzzle not in children_puzzles:
                child_puzzle = copy.deepcopy(child.puzzle)
                children_puzzles.append(child_puzzle)
        return children_puzzles

    def find_queue_puzzle_list(self):
        queue_puzzle_list = []
        for object in self.queue:
            object_puzzle_copy = copy.deepcopy(object.puzzle)
            if object_puzzle_copy not in queue_puzzle_list:
                queue_puzzle_list.append(object_puzzle_copy)
        return queue_puzzle_list

    def find_children(self, node: Node):
        possible_actions = self.get_possible_action(node)
        children_puzzles = self.find_children_puzzles(node, possible_actions)
        for child_puzzle in children_puzzles:
            child = Node(child_puzzle, node, node.depth + 1)
            children_puzzles = self.find_children_puzzle_list(node)
            if child.puzzle not in children_puzzles:
                child_copy = copy.deepcopy(child)
                node.children.append(child_copy)

    def update_queue(self, node):
        self.find_children(node)
        queue_list = self.find_queue_puzzle_list()
        len1 = len(self.queue)
        for child in node.children:
            if child.puzzle not in queue_list:
                self.queue.append(child)

    @staticmethod
    def show_path(node: Node):
        node_temp = node
        ans = [node_temp]
        while node_temp.parent is not None:
            ans.append(node_temp.parent)
            node_temp = node_temp.parent
        ans.reverse()
        for i in ans:
            print(i)

    def solve(self):
        self.find_children(self.start_node)
        self.update_queue(self.start_node)
        max_node: Node = self.find_next()
        while True:
            print("queue")
            for j in self.queue:
                print(j.puzzle)
                print(j.depth)
            if max_node == self.goal:
                self.show_path(max_node)
                break
            else:
                self.queue.remove(max_node)
                self.find_children(max_node)
                self.update_queue(max_node)
                max_node: Node = self.find_next()
