# Name: Muhammad Zaid Saqib
# Reg No : B24F1722CYS084
# Section : CYS Green
# Date : 03/10/2025
# Lab No :06


# Lab Practise
'''
'''

# Practise 1
# DFS Itrative

'''
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()  # Pop a node from the stack.
        if node not in visited:
            print(node)
            visited.add(node)
            # Add all unvisited neighbors to the stack.
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    return visited

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': []
}
print("DFS Iterative Traversal starting from node 'A':")
dfs_iterative(graph, 'A')
'''

# Practise 2
# Depth Fist Search Recursive

'''
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited
# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': []
}
print("DFS Recursive Traversal starting from node 'A':")
dfs_recursive(graph, 'A')
'''

# Practise 3
# Depth Limited Search (DLS)

'''
def dls(graph, start, goal, depth, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    if start == goal:
        return True

    if depth > 0:
        for neighbor in graph[start]:
            if neighbor not in visited:
                if dls(graph, neighbor, goal, depth - 1, visited):
                    return True
    return False


# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': []
}

start_node = 'A'
goal_node = 'C'
depth_limit = 2

if dls(graph, start_node, goal_node, depth_limit):
    print(f"Goal node '{goal_node}' found within depth limit {depth_limit}.")
else:
    print(f"Goal node '{goal_node}' not found within depth limit {depth_limit}.")
'''
# Lab Task

#### Task 1: Write Python programs to traverse a graph using DFS.
#Implement DFS iteratively using a stack and print the order of visited nodes.
#Implement DFS recursively and print the order of visited nodes.

'''
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()  # Pop a node from the stack.
        if node not in visited:
            print(node)
            visited.add(node)
            # Add all unvisited neighbors to the stack.
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    return visited
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': []
}
print("DFS Iterative Traversal starting from node 'A':")
dfs_iterative(graph, 'A')
print("\nDFS Recursive Traversal starting from node 'A':")
dfs_recursive(graph, 'A')
'''


# Task 02: Use DFS to find all possible paths from a source node to a destination node.
# Write an iterative DFS function to return all paths using a stack.
'''
def dfs_all_paths(graph, start, goal):
    stack = [(start, [start])]
    paths = []

    while stack:
        (node, path) = stack.pop()
        for neighbor in graph[node]:
            if neighbor not in path:  # Avoid cycles
                if neighbor == goal:
                    paths.append(path + [neighbor])
                else:
                    stack.append((neighbor, path + [neighbor]))
    return paths

graph = {
    'A': ['B', 'C'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': []
}
start_node = input ("Enter the start node: ")
goal_node =  input ("Enter the goal node: ")
all_paths = dfs_all_paths(graph, start_node, goal_node)
print(f"All paths from '{start_node}' to '{goal_node}': {all_paths}")
'''

# Task 03: Use DFS to check whether a path exists between a start node and a goal node.
#Implement this using recursive DFS.
#For Example:
# Input:
# Start node: 'A'
# Goal node: 'F'

'''
def dfs_path_exists(graph, start, goal, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    if start == goal:
        return True

    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs_path_exists(graph, neighbor, goal, visited):
                return True
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': []
}
start_node = input ("Enter the start node: ")
goal_node = input ("Enter the goal node: ")
if dfs_path_exists(graph, start_node, goal_node):
    print(f"Path exists from '{start_node}' to '{goal_node}'.")
else:
    print(f"Path does not exist from '{start_node}' to '{goal_node}'.")
'''


#Conculsion
'''
In this lab, I learned how Depth First Search (DFS) works and how it can be implemented in different ways.
I practiced writing DFS both iteratively using a stack and recursively, which helped me understand how nodes are explored
deeply before moving to the next branch. I also applied DFS to find all possible paths between two nodes and to check if 
a path exists between a start and goal node.This lab improved my logical thinking and problem-solving skills, as
I had to carefully manage visited nodes to avoid infinite loops. Overall, this exercise gave me a clearer understanding
of graph traversal techniques and how they can be used in real-world applications like pathfinding, network analysis, 
and search algorithms.
'''





