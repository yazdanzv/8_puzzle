from Node import Node
from Expandation import Expand

start_node = Node(['1', '2', '3', '0', '7', '6', '5', '4', '8'], None, 0)
goal_node = Node(['1', '2', '3', '4', '5', '6', '7', '8', '0'], None, None)
agent = Expand(start_node, goal_node)
agent.solve()
