# Name : Muhammad Zaid Saqib
# Reg No : B24F1722CYS084
# Section : CYS Green
# Date : 03/10/2023
# Lab No :05


# Lab Practise
# Functions in Python

#Practise Task 1
# Function without parameters

'''
def greet():
    print("Hello, welcome to the Python programming world!")
greet()
'''

# Practise Task 2
# Function with parameters

'''
def multiply(x, y):
    print ("The product is:", x * y)
multiply(4, 5)
'''

# Practise Task 3
# Function with return value

'''
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 10)
print("The sum is:", result)
'''


# Practise Task 4
# Function with default parameters

'''
def power(base, exponent=2):
    return base ** exponent
print("5 squared is:", power(5))
print("2 to the power of 3 is:", power(2, 3))
print("4 to the power of 4 is:", power(4, 4))
'''

# Practise Task 5
# Detailed example
# Grade Calculation

'''
def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'
student_marks = input("Enter student marks separated by spaces: ").split()
student_marks = [int(mark) for mark in student_marks]

for marks in student_marks:
    grade = calculate_grade(marks)
    print(f"Marks: {marks}, Grade: {grade}")
'''

# Lab Task
# Functions

# Task 1
# Q Write a function to calculate the factorial of a number.

'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {num} is {factorial(num)}")
'''

# Task 2
# QWrite a function that takes a list as input and returns the maximum element.

'''
def find_maximum(lst):
    if not lst:
        return None
    max_element = lst[0]
    for num in lst:
        if num > max_element:
            max_element = num
    return max_element
numbers=input("Enter numbers separated by spaces: ").split()
numbers=[int(num) for num in numbers]
print(f"The maximum element in the list is: {find_maximum(numbers)}")
'''

# Task 3
# Q Write a function that checks if a number is prime or not.

'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number to check if it is prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
'''

# Task 4
# Q Create a function that reverses a string.

'''
def reverse_string(s):
    return s[::-1]
string = input("Enter a string to reverse: ")
print(f"The reversed string is: {reverse_string(string)}")
'''

# Lab Practice
# BFS in Python

'''
def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start_node = 'A'
print("BFS traversal starting from node", start_node)
bfs(graph, start_node)


# Output: A B C D E F
# Note: The output may vary based on the order of neighbors in the adjacency list.
'''

# Lab Task
# BFS in Python

# Task 1
# Q Implement BFS on a graph given by the user.

'''
def bfs(graph , start):
    visited = []
    queue = [start]
    visited.append(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

graph = {}
num_edges = int(input("Enter the number of edges in the graph: "))
for _ in range(num_edges):
    u, v = input("Enter edge (u v): ").split()
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)  # Undirected graph

start_node = input("Enter the starting node for BFS: ")
print("BFS traversal starting from node", start_node)
bfs(graph, start_node)
'''

#Lab Task 2
# Q Modify BFS to count the number of nodes in each level.

'''
def bfs_with_levels(graph, start):
    visited = set()
    queue = [(start, 0)]  # (node, level)
    visited.add(start)
    level_count = {}

    while queue:
        vertex, level = queue.pop(0)
        if level not in level_count:
            level_count[level] = 0
        level_count[level] += 1
        print(f"Node: {vertex}, Level: {level}")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))

    return level_count
graph = {}
num_edges = int(input("Enter the number of edges in the graph: "))
for _ in range(num_edges):
    u, v = input("Enter edge (u v): ").split()
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)  
start_node = input("Enter the starting node for BFS: ")
print("BFS traversal starting from node", start_node)
level_counts = bfs_with_levels(graph, start_node)
print("Number of nodes at each level:", level_counts)
'''


# Lab Task 3
# Q Write a BFS function that checks if there is a path between two given nodes.

'''
def bfs_path_exists(graph, start, goal):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        vertex = queue.pop(0)
        if vertex == goal:
            return True
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False
graph = {}
num_edges = int(input("Enter the number of edges in the graph: "))
for _ in range(num_edges):
    u, v = input("Enter edge (u v): ").split()
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)
start_node = input("Enter the starting node for BFS: ")
goal_node = input("Enter the goal node to check path existence: ")
if bfs_path_exists(graph, start_node, goal_node):
    print(f"There is a path from {start_node} to {goal_node}.")
else:
    print(f"There is no path from {start_node} to {goal_node}.")
'''


#Conculsion :
'''
In this lab, I explored the use of functions in Python and understood how they make programs more organized, reusable,
and easier to manage. I practiced writing functions with parameters, return values, and default arguments, which helped
me understand how data flows in and out of functions. By solving problems such as calculating factorials, finding the
maximum in a list, checking prime numbers, and reversing strings, I not only applied theoretical concepts but also 
developed confidence in breaking problems down into smaller, manageable steps.I also worked on graph-related problems 
using Breadth-First Search (BFS). This gave me practical exposure to building and traversing graphs, counting nodes at
different levels, and checking for paths between nodes. These tasks showed me how algorithms can be adapted to solve 
real-world problems in different ways.Overall, this lab strengthened my logical thinking, problem-solving abilities,
and coding style. I now feel more confident in using recursion, handling lists, and applying graph traversal techniques.
Most importantly, I understood how combining small functions and algorithms can create powerful solutions to complex problems.
'''





