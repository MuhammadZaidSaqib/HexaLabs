import heapq

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
    'S': 10,
    'A': 8,
    'B': 7,
    'C': 6,
    'D': 4,
    'E': 3,
    'F': 2,
    'G': 1,
    'H': 0
}

def astar(graph, start, goal, heuristic):
    open_heap = []
    g_score = {node: float('inf') for node in graph}
    came_from = {}
    g_score[start] = 0
    # heap entry: (f_score, g_score, node)
    heapq.heappush(open_heap, (heuristic[start], 0, start))

    closed = set()
    while open_heap:
        f, g, current = heapq.heappop(open_heap)
        if current == goal:
            # reconstruct path
            path = []
            node = current
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
            tentative_g = g_score[current] + cost
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic.get(neighbor, float('inf'))
                heapq.heappush(open_heap, (f_score, tentative_g, neighbor))

    return None, float('inf')

if __name__ == "__main__":
    path, cost = astar(graph, 'S', 'H', heuristic)
    if path:
        print("Path found:", path)
        print("Total cost:", cost)
    else:
        print("No path found from 'S' to 'H'.")
