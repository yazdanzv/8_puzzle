from Node import Node
from Expandation_AStar import Expand_AStar
from Expandation_UCS import Expand_UCS
from Expandation_BFS import Expand_BFS
from Expandation_DFS import Expand_DFS

test_node1 = Node(['1', '2', '0', '4', '5', '3', '7', '8', '6'], None, 0)
test_node2 = Node(['1', '2', '0', '4', '5', '3', '7', '8', '6'], None, None)
start_node = Node(['1', '2', '3', '0', '7', '6', '5', '4', '8'], None, 0)
goal_node = Node(['1', '2', '3', '4', '5', '6', '7', '8', '0'], None, None)
# agent = Expand_AStar(start_node, goal_node)
# agent.solve()
# print(agent.h_manhattan(test_node))
# print(test_node1 == start_node)
# agent = Expand_UCS(start_node, goal_node)
# agent.solve()
# agent = Expand_BFS(start_node, goal_node)
# agent.solve()
agent = Expand_DFS(test_node1, goal_node)
agent.solve()
