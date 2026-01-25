# Name: Muhammad Zaid Saqib
# Reg No : B24F1722CYS084
# Section : CYS Green
# Date : 27/11/2025
# Lab No :12

# Lab Practise
'''
'''


#lab practice
'''
# Map Coloring using Backtracking

# List of states in Australia
states = ['Western Australia', 'Northern Territory', 'South Australia', 
          'Queensland', 'New South Wales', 'Victoria', 'Tasmania']

# Available colors
colors = ['Red', 'Green', 'Blue']

# Neighboring states
neighbors = {
    'Western Australia': ['Northern Territory', 'South Australia'],
    'Northern Territory': ['Western Australia', 'South Australia', 'Queensland'],
    'South Australia': ['Western Australia', 'Northern Territory', 'Queensland', 'New South Wales', 'Victoria'],
    'Queensland': ['Northern Territory', 'South Australia', 'New South Wales'],
    'New South Wales': ['Queensland', 'South Australia', 'Victoria'],
    'Victoria': ['South Australia', 'New South Wales'],
    'Tasmania': []
}

# Dictionary to store the color assignment for each state
assignment = {}

# Function to check if a color can be assigned to a state
def is_valid(state, color):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking function to assign colors to states
def backtrack(index=0):
    if index == len(states):
        return True  # All states are assigned successfully

    state = states[index]

    for color in colors:
        if is_valid(state, color):
            assignment[state] = color
            if backtrack(index + 1):
                return True
            assignment.pop(state)  # Backtrack if color assignment doesn't lead to a solution

    return False

# Solve the map coloring problem
if backtrack():
    print("Solution:", assignment)
else:
    print("No solution found")
'''

# practice 2
'''
import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G = nx.Graph()
for state in states:
    G.add_node(state)
for state, neighbors_list in neighbors.items():
    for neighbor in neighbors_list:
        G.add_edge(state, neighbor)

# Custom positions for a better layout (roughly geographic)
pos = {
    'Western Australia': (-3, 0),
    'Northern Territory': (0, 2),
    'South Australia': (0, -1),
    'Queensland': (3, 2),
    'New South Wales': (4, 0),
    'Victoria': (3, -2),
    'Tasmania': (4, -3)  # Placed close to Victoria
}

# Draw the graph
plt.figure(figsize=(10,6))
node_colors = [assignment[state] for state in G.nodes()]
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=3000, font_size=10, font_weight='bold')
plt.title("Map Coloring of Australia States (Custom Layout)", fontsize=16)
plt.show()
'''
# Lab Tasks


#Task 1:
#CSP SOLVER USING BACKTRACKING TO ASSIGN COLORS:

'''
from copy import deepcopy

graph = {
    "California": ["Oregon", "Nevada", "Arizona"],
    "Oregon": ["California", "Nevada"],
    "Nevada": ["California", "Oregon", "Arizona"],
    "Arizona": ["California", "Nevada"]
}

colors = ["Red", "Green", "Blue"]

def is_consistent(var, color, assignment, graph):
    for neighbor in graph[var]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def select_unassigned_var(assignment, domains):

    unassigned = [v for v in domains if v not in assignment]
    return min(unassigned, key=lambda v: len(domains[v]))

def backtrack(assignment, domains, graph):
    if len(assignment) == len(domains):
        return assignment
    var = select_unassigned_var(assignment, domains)
    for color in domains[var]:
        if is_consistent(var, color, assignment, graph):
            assignment[var] = color

            new_domains = deepcopy(domains)
            new_domains[var] = [color]
            for neighbor in graph[var]:
                if color in new_domains[neighbor]:
                    new_domains[neighbor] = [c for c in new_domains[neighbor] if c != color]

            if any(len(new_domains[n]) == 0 and n not in assignment for n in graph[var]):
                del assignment[var]
                continue
            result = backtrack(assignment, new_domains, graph)
            if result:
                return result
            del assignment[var]
    return None

def solve_map_coloring(graph, colors):
    domains = {var: list(colors) for var in graph}
    solution = backtrack({}, domains, graph)
    return solution

if __name__ == "__main__":
    solution = solve_map_coloring(graph, colors)
    if solution:
        print("Solution found:")
        for region, color in sorted(solution.items()):
            print(f"{region}: {color}")
    else:
        print("No solution found with given colors.")
'''
#Task 2:
#CSP BASED SCHEDULER FOR 10 EMPLOYEES AND 5 SHIFTS:
'''
from copy import deepcopy
from collections import defaultdict


employees = {
    "E1": {"skills": {"cashier", "stock"}, "avail": {"S1", "S2", "S4"}, "history": 5},
    "E2": {"skills": {"cashier"}, "avail": {"S1", "S3", "S5"}, "history": 3},
    "E3": {"skills": {"security"}, "avail": {"S2", "S3", "S4", "S5"}, "history": 2},
    "E4": {"skills": {"stock", "security"}, "avail": {"S1", "S4", "S5"}, "history": 6},
    "E5": {"skills": {"cashier", "security"}, "avail": {"S1", "S2", "S3"}, "history": 1},
    "E6": {"skills": {"stock"}, "avail": {"S3", "S4"}, "history": 4},
    "E7": {"skills": {"cashier"}, "avail": {"S2", "S5"}, "history": 2},
    "E8": {"skills": {"stock", "cashier"}, "avail": {"S1", "S3", "S4", "S5"}, "history": 0},
    "E9": {"skills": {"security"}, "avail": {"S1", "S2"}, "history": 3},
    "E10": {"skills": {"cashier", "stock"}, "avail": {"S4", "S5"}, "history": 2},
}


shifts = ["S1", "S2", "S3", "S4", "S5"]
requirements = {
    "S1": {"cashier"},
    "S2": {"stock"},
    "S3": {"security"},
    "S4": {"stock"},
    "S5": {"cashier"},
}

def initial_domains(employees, shifts, requirements, max_shifts_per_employee, current_assignment=None):
    current_assignment = current_assignment or {}
    domains = {}
    for s in shifts:
        possible = []
        req = requirements.get(s, set())
        for e, info in employees.items():
            if s in info["avail"] and req.issubset(info["skills"]):
                # if already assigned counts towards max
                assigned_count = sum(1 for a in current_assignment.values() if a == e)
                if assigned_count < max_shifts_per_employee:
                    possible.append(e)
        domains[s] = possible
    return domains

def select_unassigned_var(assignment, domains):
    unassigned = [s for s in domains if s not in assignment]
    # MRV: fewest remaining values; tie-break with shift order
    return min(unassigned, key=lambda v: (len(domains[v]), v))

def is_consistent(assignment, shift_index_map, shift, employee, max_shifts_per_employee):
    # check non-consecutive: neighbor shifts
    idx = shift_index_map[shift]
    for neigh_idx in (idx - 1, idx + 1):
        if 0 <= neigh_idx < len(shift_index_map):
            neigh_shift = list(shift_index_map.keys())[list(shift_index_map.values()).index(neigh_idx)]
            if assignment.get(neigh_shift) == employee:
                return False
    # check max shifts per employee
    assigned_count = sum(1 for v in assignment.values() if v == employee)
    if assigned_count >= max_shifts_per_employee:
        return False
    return True

def order_domain_values(domain, employees, history):
    # prefer employees with lower historical load for workload balance
    return sorted(domain, key=lambda e: (history.get(e, 0), e))

def forward_check(domains, shift, employee, shift_idx_map, max_shifts_per_employee, assignment):
    new_domains = deepcopy(domains)
    # assign shift to single employee
    new_domains[shift] = [employee]
    # reduce neighbors: remove same employee from adjacent shifts (non-consecutive)
    idx = shift_idx_map[shift]
    for neigh_idx in (idx - 1, idx + 1):
        if 0 <= neigh_idx < len(shift_idx_map):
            neigh_shift = list(shift_idx_map.keys())[list(shift_idx_map.values()).index(neigh_idx)]
            if employee in new_domains[neigh_shift]:
                new_domains[neigh_shift] = [c for c in new_domains[neigh_shift] if c != employee]
    # enforce max_shifts: if assigning this employee reaches max, remove from all remaining domains
    assigned_count = sum(1 for v in assignment.values() if v == employee) + 1
    if assigned_count >= max_shifts_per_employee:
        for s in new_domains:
            if s not in assignment and s != shift:
                if employee in new_domains[s]:
                    new_domains[s] = [c for c in new_domains[s] if c != employee]
    return new_domains

def backtrack(assignment, domains, employees, shifts, requirements, shift_idx_map, max_shifts_per_employee, history):
    if len(assignment) == len(shifts):
        return assignment
    var = select_unassigned_var(assignment, domains)
    ordered_vals = order_domain_values(domains[var], employees, history)
    for e in ordered_vals:
        if is_consistent(assignment, shift_idx_map, var, e, max_shifts_per_employee):
            assignment[var] = e
            new_domains = forward_check(domains, var, e, shift_idx_map, max_shifts_per_employee, assignment)
            # fail early if any unassigned shift has empty domain
            if any(len(new_domains[s]) == 0 and s not in assignment for s in new_domains):
                del assignment[var]
                continue
            result = backtrack(assignment, new_domains, employees, shifts, requirements, shift_idx_map, max_shifts_per_employee, history)
            if result:
                return result
            del assignment[var]
    return None

def solve_schedule(employees, shifts, requirements, max_shifts_per_employee=2, history=None):
    history = history or {e: info.get("history", 0) for e, info in employees.items()}
    shift_idx_map = {s: i for i, s in enumerate(shifts)}
    domains = initial_domains(employees, shifts, requirements, max_shifts_per_employee)
    # quick impossibility check
    if any(len(domains[s]) == 0 for s in domains):
        return None
    return backtrack({}, domains, employees, shifts, requirements, shift_idx_map, max_shifts_per_employee, history)

if __name__ == "__main__":
    max_per_employee = 2  # allow up to 2 shifts per employee (non-consecutive enforced)
    solution = solve_schedule(employees, shifts, requirements, max_per_employee)
    if solution:
        print("Schedule:")
        for s in shifts:
            print(f"{s}: {solution[s]}")
    else:
        print("No feasible schedule found with current constraints.")
'''
#Task 3:
#CSP SOLVER FOR JOB ASSIGNMENT BASED ON SKILLS AND PREFERENCES:
'''
from copy import deepcopy


employees = {
    "Ali": {
        "skills": {"dev", "qa"},
        "avail": {"Backend", "API", "Testing"},
        "prefs": ["Backend", "API", "Testing"]
    },
    "Bilal": {
        "skills": {"dev"},
        "avail": {"Backend", "Frontend"},
        "prefs": ["Frontend", "Backend"]
    },
    "Qasim": {
        "skills": {"frontend", "design"},
        "avail": {"Frontend", "UI"},
        "prefs": ["UI", "Frontend"]
    },
    "Daud": {
        "skills": {"dev", "api"},
        "avail": {"API", "Backend"},
        "prefs": ["API", "Backend"]
    },
    "Maaz": {
        "skills": {"qa"},
        "avail": {"Testing", "QA"},
        "prefs": ["Testing", "QA"]
    },
    "Aleena": {
        "skills": {"design", "frontend"},
        "avail": {"UI", "Frontend"},
        "prefs": ["UI", "Frontend"]
    },
}


jobs = {
    "Backend": {"req": {"dev"}},
    "Frontend": {"req": {"frontend"}},
    "API": {"req": {"api", "dev"}},
    "UI": {"req": {"design"}},
    "Testing": {"req": {"qa"}},
    "QA": {"req": {"qa"}},
}

def initial_domains(jobs, employees):
    domains = {}
    for job, info in jobs.items():
        req = info.get("req", set())
        possible = []
        for e, einfo in employees.items():
            if job in einfo["avail"] and req.issubset(einfo["skills"]):
                possible.append(e)
        domains[job] = possible
    return domains

def select_unassigned_var(assignment, domains):
    unassigned = [j for j in domains if j not in assignment]

    return min(unassigned, key=lambda j: (len(domains[j]), j))

def order_domain_values(job, domain, employees):

    def score(e):
        prefs = employees[e].get("prefs", [])
        try:
            return prefs.index(job)
        except ValueError:
            return len(prefs) + 1
    return sorted(domain, key=lambda e: (score(e), e))

def forward_check(domains, job, employee, assignment):
    new_domains = deepcopy(domains)

    new_domains[job] = [employee]

    for j in new_domains:
        if j != job and employee in new_domains[j]:
            new_domains[j] = [e for e in new_domains[j] if e != employee]

    for j, dom in new_domains.items():
        if j not in assignment and len(dom) == 0:
            return None
    return new_domains

def backtrack(assignment, domains):
    if len(assignment) == len(domains):
        return assignment
    var = select_unassigned_var(assignment, domains)
    ordered = order_domain_values(var, domains[var], employees)
    for e in ordered:
        if e in assignment.values():
            continue
        assignment[var] = e
        new_domains = forward_check(domains, var, e, assignment)
        if new_domains is not None:
            result = backtrack(assignment, new_domains)
            if result:
                return result
        del assignment[var]
    return None

def solve_job_assignment(jobs, employees):
    domains = initial_domains(jobs, employees)

    if any(len(domains[j]) == 0 for j in domains):
        return None
    return backtrack({}, domains)

if __name__ == "__main__":
    solution = solve_job_assignment(jobs, employees)
    if solution:
        print("Job -> Employee assignment:")
        for job in sorted(solution):
            print(f"{job}: {solution[job]}")

        emp_to_job = {e: j for j, e in solution.items()}
        print("\nEmployee -> Job:")
        for e in sorted(employees):
            print(f"{e}: {emp_to_job.get(e, 'Unassigned')}")
    else:
        print("No feasible assignment found with current constraints.")
'''
#Conclusion:
'''
In this lab, we applied CSP techniques to three different real-world problems: map coloring, employee scheduling,
and job assignment. First, we used Backtracking to color a country’s regions so that no adjacent areas shared the
same color. Then, we designed a Backtracking + AC-3 scheduling system to assign employees to shifts while
satisfying availability, skills, and fairness constraints. Finally, we built a CSP job-assignment solver to match
employees to roles based on compatibility and restrictions, strengthening our understanding of constraint reasoning
and AI problem-solving.
'''
