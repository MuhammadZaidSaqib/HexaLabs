
'''
Scenario: Smart Disaster-Response Drone Navigation
A city has been hit by an earthquake, and rescue teams are deploying autonomous drones to search for survivors. The city map contains:
•	Blocked roads (debris)
•	Safe zones
•	High-priority areas (schools, hospitals)
•	Low-priority areas (parking lots, empty grounds)
The drone must start from a base camp and reach the nearest high-priority area while avoiding blocked paths. Road distances vary.
Task:
1.	Represent the city as a graph / grid in Python.
2.	Use three different search algorithms to compute the path:
	BFS, Greedy Best-First, and A*
3.	Compare:
	Which algorithm gives the shortest path?
	Which is fastest?
	Which is best suited for a real rescue drone and why?
4.	Discuss how heuristics influence the performance of Greedy and A*.

'''
# python
import heapq
import time
from collections import deque


def build_sample_grid():
    # 10x10 sample fixed map: numbers >0 are movement costs, -1 blocked
    costs = [
        [1, 1, 2, 2, 5, 5, 1, 1, 1, 1],
        [1, -1, -1, 2, -1, 5, 1, -1, -1, 1],
        [1, 1, 2, 2, 1, 1, 1, 1, -1, 1],
        [5, 5, 5, 1, 1, -1, 3, 1, 1, 1],
        [1, -1, 1, 1, 1, 1, 3, -1, 1, 1],
        [1, 1, 1, -1, 5, 1, 1, 1, 1, 1],
        [2, 2, 1, 1, 1, -1, -1, 2, 2, 1],
        [1, 1, 1, 5, 1, 1, 1, 1, -1, 1],
        [1, -1, 1, 1, 1, 3, 1, 1, 1, 1],
        [1, 1, 1, 1, -1, 1, 1, 2, 1, 1],
    ]
    # blocked indicated by -1
    start = (0, 0)  # base camp
    targets = [(2, 9), (0, 9), (9, 6)]  # high-priority targets (row, col)
    return costs, start, targets

def in_bounds(pos, rows, cols):
    r, c = pos
    return 0 <= r < rows and 0 <= c < cols

def neighbors(pos, rows, cols):
    r, c = pos
    for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
        nr, nc = r+dr, c+dc
        if in_bounds((nr,nc), rows, cols):
            yield (nr, nc)

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def nearest_target_heuristic(pos, targets):
    return min(manhattan(pos, t) for t in targets)

def reconstruct_path(came_from, end):
    path = []
    cur = end
    while cur in came_from:
        path.append(cur)
        cur = came_from[cur]
    path.append(cur)
    path.reverse()
    return path

def path_cost(path, costs):
    return sum(costs[r][c] for r,c in path)

def bfs(costs, start, targets):
    rows, cols = len(costs), len(costs[0])
    q = deque([start])
    came_from = {}
    visited = set([start])
    nodes_expanded = 0
    start_time = time.perf_counter()
    found = None
    while q:
        cur = q.popleft()
        nodes_expanded += 1
        if cur in targets:
            found = cur
            break
        for n in neighbors(cur, rows, cols):
            if n in visited: continue
            if costs[n[0]][n[1]] == -1: continue
            visited.add(n)
            came_from[n] = cur
            q.append(n)
    elapsed = time.perf_counter() - start_time
    if found is None:
        return None, float('inf'), nodes_expanded, elapsed
    path = reconstruct_path(came_from, found)
    return path, path_cost(path, costs), nodes_expanded, elapsed

def greedy_best_first(costs, start, targets):
    rows, cols = len(costs), len(costs[0])
    heap = []
    heapq.heappush(heap, (nearest_target_heuristic(start, targets), start))
    came_from = {}
    visited = set()
    nodes_expanded = 0
    start_time = time.perf_counter()
    while heap:
        _, cur = heapq.heappop(heap)
        if cur in visited:
            continue
        visited.add(cur)
        nodes_expanded += 1
        if cur in targets:
            elapsed = time.perf_counter() - start_time
            path = reconstruct_path(came_from, cur)
            return path, path_cost(path, costs), nodes_expanded, elapsed
        for n in neighbors(cur, rows, cols):
            if n in visited: continue
            if costs[n[0]][n[1]] == -1: continue
            if n not in came_from:
                came_from[n] = cur
            heapq.heappush(heap, (nearest_target_heuristic(n, targets), n))
    elapsed = time.perf_counter() - start_time
    return None, float('inf'), nodes_expanded, elapsed

def a_star(costs, start, targets):
    rows, cols = len(costs), len(costs[0])
    open_heap = []
    start_h = nearest_target_heuristic(start, targets)
    heapq.heappush(open_heap, (start_h + costs[start[0]][start[1]], start))
    g_score = {start: costs[start[0]][start[1]]}  # cost includes starting cell
    came_from = {}
    nodes_expanded = 0
    start_time = time.perf_counter()
    closed = set()
    while open_heap:
        f, cur = heapq.heappop(open_heap)
        if cur in closed:
            continue
        closed.add(cur)
        nodes_expanded += 1
        if cur in targets:
            elapsed = time.perf_counter() - start_time
            path = reconstruct_path(came_from, cur)
            return path, path_cost(path, costs), nodes_expanded, elapsed
        for n in neighbors(cur, rows, cols):
            if costs[n[0]][n[1]] == -1: continue
            tentative_g = g_score[cur] + costs[n[0]][n[1]]
            if n in g_score and tentative_g >= g_score[n]:
                continue
            came_from[n] = cur
            g_score[n] = tentative_g
            h = nearest_target_heuristic(n, targets)
            heapq.heappush(open_heap, (tentative_g + h, n))
    elapsed = time.perf_counter() - start_time
    return None, float('inf'), nodes_expanded, elapsed

def run_comparison():
    costs, start, targets = build_sample_grid()
    # mark start cost as entry cost included; if you prefer zero for start adjust code above
    results = {}
    results['BFS'] = bfs(costs, start, targets)
    results['Greedy'] = greedy_best_first(costs, start, targets)
    results['A*'] = a_star(costs, start, targets)
    for name, (path, cost, expanded, t) in results.items():
        if path is None:
            print(f"{name}: No path")
            continue
        print(f"{name}: steps={len(path)-1}, cost={cost}, nodes_expanded={expanded}, time={t:.6f}s, path={path}")
    # simple comparison
    print("\nSummary:")
    # shortest by cost
    best_cost_alg = min((name for name in results if results[name][0]), key=lambda n: results[n][1])
    fastest_alg = min(results.keys(), key=lambda n: results[n][3])
    print(f"Shortest path (by cost): {best_cost_alg}")
    print(f"Fastest (runtime): {fastest_alg}")

if __name__ == "__main__":
    run_comparison()


#Description of Results and Discussion:
'''
This program models a smart disaster-response drone navigating a city after an earthquake by representing the city as a 10×10 grid 
where each cell has a movement cost and blocked roads are marked with -1. The drone starts from a base camp and must reach the closest
high-priority target such as a hospital or school while avoiding debris. Three different search algorithms are implemented: BFS, which
explores all nearby paths equally without considering distance cost; Greedy Best-First Search, which always moves toward the location
that appears closest to a target using a heuristic (Manhattan distance); and A*, which combines the actual cost already traveled with
the heuristic estimate to choose the most efficient route. Each algorithm records the path found, total travel cost, number of expanded
nodes, and execution time. In comparison, BFS usually finds the fewest steps but not necessarily the lowest-cost route because it ignores
road costs. Greedy is often the fastest because it focuses directly on the target, but it can choose poor routes if the heuristic is misleading.
A* typically produces the shortest path by cost while remaining efficient, making it the best choice for a real rescue drone where safety, energy use,
and speed are critical. The heuristic plays a major role in Greedy and A*: a good heuristic guides the search efficiently toward the goal, while a poor
one can slow the process or cause inefficient routing.
'''