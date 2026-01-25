# Name: Muhammad Zaid Saqib
# Reg No : B24F1722CYS084
# Section : CYS Green
# Date : 10/10/2025
# Lab No :08


# Lab Practise
'''
'''


# Uniform Cost Search (UCS)
# Practise 1

'''
import heapq
def ucs(graph, start, goal):
    # Priority queue to store (cost, node, path)
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return cost, path

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))

    return float("inf"), []
# Example graph represented as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_node = 'A'
goal_node = 'D'
cost, path = ucs(graph, start_node, goal_node)
print(f"Uniform Cost Search from {start_node} to {goal_node}:")
print(f"Cost: {cost}, Path: {' -> '.join(path)}")
'''

#lab Task
#Task 1: Implement Uniform Cost Search (UCS) on a basic weighted graph in Python to find the least-cost path between two nodes.

'''
import heapq
def ucs(graph, start, goal):
    # Priority queue to store (cost, node, path)
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return cost, path

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))

    return float("inf"), []
# Example graph represented as an adjacency list
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 5, 'B': 1, 'D': 2},
    'D': {'B': 4, 'C': 2}
}
start_node = 'A'
goal_node = 'D'
cost, path = ucs(graph, start_node, goal_node)
print(f"Uniform Cost Search from {start_node} to {goal_node}:")
print(f"Cost: {cost}, Path: {' -> '.join(path)}")
'''

# Task 2
#Apply UCS on a real-world city map with road distances to determine the shortest route between two cities using a priority queue.

'''
import heapq
def ucs(graph, start, goal):
    # Priority queue to store (cost, node, path)
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return cost, path

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))

    return float("inf"), []
# Example city map represented as an adjacency list with road distances
city_map = {
    'CityA': {'CityB': 10, 'CityC': 15},
    'CityB': {'CityA': 10, 'CityC': 5, 'CityD': 20},
    'CityC': {'CityA': 15, 'CityB': 5, 'CityD': 10},
    'CityD': {'CityB': 20, 'CityC': 10}
}
start_city = 'CityA'
goal_city = 'CityD'
cost, path = ucs(city_map, start_city, goal_city)
print(f"Uniform Cost Search from {start_city} to {goal_city}:")
print(f"Cost: {cost}, Path: {' -> '.join(path)}")
'''

# Task 3
# Task 3: Using the following weighted graph, apply UCS to find the least-cost path from node A to J, showing priority queue
# updates and explaining how UCS selects the optimal path at each step:
# A → B (2), A → C (4), A → D (7)
# B → E (5), B → F (3)
# C → F (2), C → G (6)
# D → G (3), D → H (8)
# E → I (4)
# F → I (6), F → J (8)
# G → J (5)
# H → J (4)
# I → J (3)

'''
import heapq
def ucs(graph, start, goal):
    # Priority queue to store (cost, node, path)
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return cost, path

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))

    return float("inf"), []
# Given weighted graph represented as an adjacency list
graph = {
    'A': {'B': 2, 'C': 4, 'D': 7},
    'B': {'E': 5, 'F': 3},
    'C': {'F': 2, 'G': 6},
    'D': {'G': 3, 'H': 8},
    'E': {'I': 4},
    'F': {'I': 6, 'J': 8},
    'G': {'J': 5},
    'H': {'J': 4},
    'I': {'J': 3}
}
start_node = 'A'
goal_node = 'J'
cost, path = ucs(graph, start_node, goal_node)
print(f"Uniform Cost Search from {start_node} to {goal_node}:")
print(f"Cost: {cost}, Path: {' -> '.join(path)}")
'''

# Explanation of UCS Steps:
'''1. Start at node A with cost 0. Add neighbors B (cost 2), C (cost 4), and D (cost 7) to the priority queue.
2. Pop B (cost 2) from the queue. Add neighbors E (cost 7) and F (cost 5) to the queue.
3. Pop F (cost 5) from the queue. Add neighbors I (cost 11) and J (cost 13) to the queue.
4. Pop C (cost 4) from the queue. Add neighbors F (cost 6) and G (cost 10) to the queue.
5. Pop D (cost 7) from the queue. Add neighbors G (cost 10) and H (cost 15) to the queue.
6. Pop E (cost 7) from the queue. Add neighbor I (cost 11) to the queue.
7. Pop G (cost 10) from the queue. Add neighbor J (cost 15) to the queue.
8. Pop I (cost 11) from the queue. Add neighbor J (cost 14) to the queue.
9. Finally, pop J (cost 13) from the queue, reaching the goal node with the least cost path A -> B -> F -> J with a total cost of 13.
'''


#Concuslion
'''
In this lab, I successfully implemented and applied the Uniform Cost Search (UCS) algorithm across three different tasks 
to understand its working and effectiveness in finding the least-cost path in weighted graphs.
In Task 1, I implemented UCS on a simple weighted graph to find the shortest path between two nodes. This helped me understand
how UCS uses a priority queue to always expand the lowest-cost node first.
In Task 2, I applied UCS to a real-world scenario by simulating a city map with road distances. This demonstrated how UCS can 
efficiently find the shortest route between two cities, just like GPS navigation systems.
In Task 3, I applied UCS on a complex weighted graph and manually traced the priority queue updates step by step. This deepened
my understanding of how UCS expands paths in increasing order of cost and guarantees the optimal path once the goal node is reached.
Overall, through these tasks, I learned how UCS ensures optimal solutions in pathfinding problems by exploring nodes in order of 
cumulative cost rather than depth or heuristic estimation. It is a practical algorithm widely used in network routing, AI search problems,
and real-world navigation systems.
'''








