# Name: Muhammad Zaid Saqib
# Reg No : B24F1722CYS084
# Section : CYS Green
# Date : 03/10/2025
# Lab No :07


# Lab Practise
'''
'''



# Practise 1
# Depth-Limited Search (DLS)
'''
def dls(graph, node, goal, limit):
    if node == goal:
        return True

    if limit <= 0:
        return False

    # Recursively visit each neighbor
    for neighbor in graph.get(node, []):
        if dls(graph, neighbor, goal, limit - 1):
            return True

    return False  # Return False if goal not found at this level


# Iterative Deepening Search (IDS)
def ids(graph, start, goal):
    depth = 0
    while True:
        print(f"Searching at depth: {depth}")
        if dls(graph, start, goal, depth):
            print(f"Goal '{goal}' found at depth {depth}")
            break
        depth += 1


# Example graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Run IDS
ids(graph, 'A', 'G')
'''

# Practise 2
# Greedy Best-First Search using List in Python
'''
def greedy_best_first_search(graph, start, goal, heuristic):
    open_list = [start]       # Nodes to explore
    visited = []              # Already explored nodes
    path = []                 # To store traversal path

    while open_list:
        # Find node with minimum heuristic value
        current = min(open_list, key=lambda node: heuristic[node])
        open_list.remove(current)
        path.append(current)
        print("Visiting:", current)

        # Check if goal is reached
        if current == goal:
            print("Goal Reached!")
            return path

        visited.append(current)

        # Explore neighbors
        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in open_list:
                open_list.append(neighbor)

    print("Goal Not Found")
    return path


# Define Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Define Heuristic Values (Estimated distance to goal 'G')
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 1,
    'F': 3,
    'G': 0
}

# Run the algorithm
path = greedy_best_first_search(graph, 'A', 'G', heuristic)
print("\nFinal Path:", path)
'''



#Lab Task

# Task 01: Implement Greedy Best-First Search on your own graph and test it with different heuristic values.

'''
def greedy_best_first_search(graph, start, goal, heuristic):
    open_list = [start]       # Nodes to explore
    visited = []              # Already explored nodes
    path = []                 # To store traversal path

    while open_list:
        # Find node with minimum heuristic value
        current = min(open_list, key=lambda node: heuristic[node])
        open_list.remove(current)
        path.append(current)
        print("Visiting:", current)

        # Check if goal is reached
        if current == goal:
            print("Goal Reached!")
            return path

        visited.append(current)

        # Explore neighbors
        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in open_list:
                open_list.append(neighbor)

    print("Goal Not Found")
    return path
# Define Graph
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': ['G'],
    'G': []
}
# Define Heuristic Values (Estimated distance to goal 'G')
heuristic = {
    'S': 6,
    'A': 4,
    'B': 2,
    'C': 5,
    'D': 2,
    'E': 3,
    'F': 1,
    'G': 0
}
# Run the algorithm
path = greedy_best_first_search(graph, 'S', 'G', heuristic)
print("\nFinal Path:", path)
'''

# Task 02: Modify IDS to show the path explored and depth of success clearly.

'''
def dls(graph, node, goal, limit, path):
    path.append(node)

    if node == goal:
        return True

    if limit <= 0:
        path.pop()
        return False

    for neighbor in graph.get(node, []):
        if dls(graph, neighbor, goal, limit - 1, path):
            return True

    path.pop()
    return False
def ids(graph, start, goal):
    depth = 0
    while True:
        path = []
        print(f"Searching at depth: {depth}")
        if dls(graph, start, goal, depth, path):
            print(f"Goal '{goal}' found at depth {depth}")
            print("Path:", " -> ".join(path))
            break
        depth += 1
# Example graph representation
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': ['G'],
    'G': []
}
# Run IDS
ids(graph, 'S', 'G')


# Task 03: Change heuristic values to see how the path and performance change.

# Define Heuristic Values (Estimated distance to goal 'G')
heuristic_variation = {
    'S': 5,
    'A': 3,
    'B': 4,
    'C': 6,
    'D': 2,
    'E': 5,
    'F': 1,
    'G': 0
}
# Run the algorithm with modified heuristic
path_variation = greedy_best_first_search(graph, 'S', 'G', heuristic_variation)
print("\nFinal Path with Modified Heuristic:", path_variation) 

'''

# Task 04: Modify your IDS implementation to count and display the total number of iterations and depth levels explored
# before reaching the goal node.

'''
def ids_with_count(graph, start, goal):
    depth = 0
    total_iterations = 0
    while True:
        path = []
        print(f"Searching at depth: {depth}")
        total_iterations += 1
        if dls(graph, start, goal, depth, path):
            print(f"Goal '{goal}' found at depth {depth}")
            print("Path:", " -> ".join(path))
            print("Total Iterations:", total_iterations)
            print("Total Depth Levels Explored:", depth + 1)
            break
        depth += 1
# Run IDS with count
ids_with_count(graph, 'S', 'G')

'''


# Conclusion:
'''
In this lab, I learned how different informed and uninformed search algorithms work, including Depth-Limited Search (DLS),
Iterative Deepening Search (IDS), and Greedy Best-First Search. By implementing these algorithms, I understood how IDS 
explores nodes level by level and provides the exact depth at which the goal is found, while Greedy Best-First Search uses 
heuristic values to guide the search more efficiently. I also observed how changing the heuristic values affects the path
selection and performance. Additionally, modifying IDS to display the path and count iterations gave a clearer understanding 
of its working and efficiency. Overall, this lab improved my grasp of search strategies in Artificial Intelligence and
how they can be applied to problem-solving.'''