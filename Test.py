from Node import Node
from Expandation import Expand

test_node1 = Node(['1', '2', '0', '4', '5', '3', '7', '8', '6'], None, None)
test_node2 = Node(['1', '2', '0', '4', '5', '3', '7', '8', '6'], None, None)
start_node = Node(['0', '2', '3', '1', '4', '5', '7', '8', '6'], None, 0)
goal_node = Node(['1', '2', '3', '4', '5', '6', '7', '8', '0'], None, None)
agent = Expand(start_node, goal_node)
agent.solve()
# print(agent.h_manhattan(test_node))
# print(test_node1 == start_node)