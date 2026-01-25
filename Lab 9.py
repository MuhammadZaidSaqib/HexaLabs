# Name: Muhammad Zaid Saqib
# Reg No : B24F1722CYS084
# Section : CYS Green
# Date : 04/11/2025
# Lab No :09

# Lab Practise
'''
'''

'''
import heapq
def a_star(graph, start, goal, heuristic):
    open_heap = [(heuristic[start], start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    closed = set()

    while open_heap:
        _, current = heapq.heappop(open_heap)
        if current == goal:
            path = []
            node = current
            while node in came_from:
                path.append(node)
                node = came_from[node]
            path.append(start)
            path.reverse()
            return path, g_score[current]

        if current in closed:
            continue
        closed.add(current)

        for neighbor, cost in graph[current].items():
            tentative = g_score[current] + cost
            if tentative < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative
                came_from[neighbor] = current
                f = tentative + heuristic.get(neighbor, 0)
                heapq.heappush(open_heap, (f, neighbor))

    return None, float('inf')

# Example graph and heuristic
graph = {
    'S': {'A': 2, 'B': 5},
    'A': {'C': 4, 'D': 7},
    'B': {'D': 3, 'E': 6},
    'C': {'F': 5},
    'D': {'F': 2, 'G': 3},
    'E': {'G': 1},
    'F': {'H': 3},
    'G': {'H': 2},
    'H': {}
}

heuristic = {
    'S': 10, 'A': 8, 'B': 7, 'C': 6,
    'D': 4, 'E': 3, 'F': 2, 'G': 1, 'H': 0
}

path, cost = a_star(graph, 'S', 'F ', heuristic)
print("Optimal path from S to H:", path)
print("Total cost:", cost)
'''

#Lab Task
# Task 1
#A delivery driver from a warehouse in I-9 needs to find the most efficient route to deliver a package to a customer in F-6
# using the A* algorithm. The following graph represents the city’s road network with travel costs between areas:
#Goal: Use the A* algorithm to find the shortest delivery route from I-9 (warehouse) to F-6 (customer) and display
# the final path and total cost.

'''
import heapq
def a_star(graph, start, goal, heuristic):
    open_heap = [(heuristic[start], start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    closed = set()

    while open_heap:
        _, current = heapq.heappop(open_heap)
        if current == goal:
            # Reconstruct path
            path = [current]
            while path[-1] in came_from:
                path.append(came_from[path[-1]])
            path.reverse()
            return path, g_score[goal]

        if current in closed:
            continue
        closed.add(current)

        for neighbor, cost in graph[current].items():
            tentative = g_score[current] + cost
            if tentative < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative
                came_from[neighbor] = current
                f = tentative + heuristic.get(neighbor, 0)
                heapq.heappush(open_heap, (f, neighbor))

    return None, float('inf')

graph = {
    'I-9': {'G-10': 6, 'I-8': 2},
    'G-10': {'G-9': 3, 'F-8': 5},
    'I-8': {'G-8': 4, 'H-9': 3},
    'G-9': {'F-8': 4, 'F-7': 2},
    'H-9': {'G-9': 5, 'G-8': 2},
    'G-8': {'F-8': 3, 'F-7': 4},
    'F-8': {'F-7': 3, 'F-6': 4},
    'F-7': {'F-6': 2},
    'F-6': {}
}

heuristic = {
    'I-9': 10,
    'G-10': 8,
    'I-8': 9,
    'G-9': 6,
    'H-9': 7,
    'G-8': 5,
    'F-8': 4,
    'F-7': 2,
    'F-6': 0
}

path, cost = a_star(graph, 'I-9', 'F-6', heuristic)
print("Optimal path from I-9 to F-6:", path)
print("Total cost:", cost)
'''

# Task 2
#Task 02: Modify the A* algorithm to display all visited nodes and the total path cost for a weighted graph.

'''
import heapq
def a_star_with_visited(graph, start, goal, heuristic):
    open_heap = [(heuristic[start], start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    closed = set()
    visited_nodes = []

    while open_heap:
        _, current = heapq.heappop(open_heap)
        visited_nodes.append(current)

        if current == goal:
            path = [current]
            while path[-1] in came_from:
                path.append(came_from[path[-1]])
            path.reverse()
            return path, g_score[goal], visited_nodes

        if current in closed:
            continue
        closed.add(current)

        for neighbor, cost in graph[current].items():
            tentative = g_score[current] + cost
            if tentative < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative
                came_from[neighbor] = current
                f = tentative + heuristic.get(neighbor, 0)
                heapq.heappush(open_heap, (f, neighbor))

    return None, float('inf'), visited_nodes

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0
}
path, cost, visited = a_star_with_visited(graph, 'A', 'D', heuristic)
print("Optimal path from A to D:", path)
print("Total cost:", cost)
print("Visited nodes:", visited)

'''

# Task 3
# A food delivery company in Islamabad uses Artificial Intelligence (AI) to optimize its delivery routes.
# The AI system applies the A* search algorithm — a form of heuristic search in AI — to find the fastest route for riders.
#In this scenario, a delivery rider must travel from G-11 to F-8, and the city’s road network is represented as a weighted graph
# (where edge weights show travel time in minutes)

'''
import heapq
def a_star(graph, start, goal, heuristic):
    open_heap = [(heuristic[start], start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    closed = set()

    while open_heap:
        _, current = heapq.heappop(open_heap)
        if current == goal:
            path = []
            node = goal
            while node in came_from:
                path.append(node)
                node = came_from[node]
            path.append(start)
            path.reverse()
            return path, g_score[goal]

        if current in closed:
            continue
        closed.add(current)

        for neighbor, cost in graph[current].items():
            tentative = g_score[current] + cost
            if tentative < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative
                heapq.heappush(open_heap, (tentative + heuristic.get(neighbor, 0), neighbor))

    return None, float('inf')

graph = {
    'G-11': {'G-10': 4, 'F-11': 5},
    'G-10': {'F-10': 3, 'F-9': 6},
    'F-11': {'F-10': 2, 'E-11': 4},
    'F-10': {'F-9': 2, 'F-8': 5},
    'F-9':  {'F-8': 3},
    'E-11': {'F-10': 3},
    'F-8':  {}
}

heuristic = {
    'G-11': 10,
    'G-10': 8,
    'F-11': 7,
    'F-10': 5,
    'F-9':  3,
    'E-11': 6,
    'F-8':  0
}

path, cost = a_star(graph, 'G-11', 'F-8', heuristic)
print("Optimal path from `G-11` to `F-8`:", path)
print("Total travel time (minutes):", cost)
'''

# Conclusion :
'''
In this lab, I implemented and explored the A* (A-Star) search algorithm to find the most efficient path between nodes in 
different real-world scenarios. Through the practical tasks, I learned how the algorithm combines both the actual cost (g-score)
and the heuristic estimate (h-score) to determine the optimal route.
In Task 1, I applied the A* algorithm to find the shortest delivery route from I-9 to F-6, representing a realistic delivery problem in Islamabad.
In Task 2, I modified the algorithm to display all visited nodes and the total path cost, which helped me understand how A* explores nodes 
and evaluates potential paths.
In Task 3, I simulated a food delivery system using A* to calculate the fastest travel route from G-11 to F-8, demonstrating
how AI can optimize real-world logistics.
Overall, this lab enhanced my understanding of heuristic-based search, graph traversal, and path optimization. I learned how 
A* efficiently balances exploration and cost estimation, making it one of the most effective algorithms in artificial intelligence 
and route planning applications.
'''