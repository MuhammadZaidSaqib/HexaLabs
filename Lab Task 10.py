# Name: Muhammad Zaid Saqib
# Reg No : B24F1722CYS084
# Section : CYS Green
# Date : 14/11/2025
# Lab No :10

# Lab Practise
'''
'''


#lab practice

#practice 1
#Python Implementation
#Hill Climbing (Simple Optimization Problem)
'''
# Objective function: f(x) = -x^2 + 6x - 5
def fitness(x):
    return -x**2 + 6*x - 5

# Generate neighbor
def get_neighbor(x):
    step = random.uniform(-1, 1)
    return x + step

# Hill climbing algorithm
def hill_climbing(iterations=1000):
    current_x = random.uniform(0, 6)
    current_fitness = fitness(current_x)

    for i in range(iterations):
        neighbor = get_neighbor(current_x)
        neighbor_fitness = fitness(neighbor)

        if neighbor_fitness > current_fitness:
            current_x, current_fitness = neighbor, neighbor_fitness

    return current_x, current_fitness

best_x, best_fit = hill_climbing()
print(f"Best Solution: x = {best_x:.3f}, f(x) = {best_fit:.3f}")

'''
#practice 2
''''
import random
import matplotlib.pyplot as plt


# Profit function: f(x) = -x^2 + 6x - 5
def profit(x):
    return -x ** 2 + 6 * x - 5


# Generate neighbor: small change in production
def get_neighbor(x, step_size=1):
    step = random.uniform(-step_size, step_size)
    return x + step


# Hill climbing algorithm
def hill_climbing(iterations=50, min_x=0, max_x=6):
    # Start with a random production quantity
    current_x = random.uniform(min_x, max_x)
    current_profit = profit(current_x)

    # Store the path for plotting
    path_x = [current_x]
    path_profit = [current_profit]

    for i in range(iterations):
        neighbor = get_neighbor(current_x)
        # Ensure neighbor stays within realistic bounds
        neighbor = max(min_x, min(max_x, neighbor))
        neighbor_profit = profit(neighbor)

        if neighbor_profit > current_profit:
            current_x, current_profit = neighbor, neighbor_profit

        # Save current state for plotting
        path_x.append(current_x)
        path_profit.append(current_profit)

    return current_x, current_profit, path_x, path_profit


# Run hill climbing
best_x, best_profit, path_x, path_profit = hill_climbing()

print(f"Optimal production: {best_x:.2f} hundreds of bottles")
print(f"Maximum profit: ${best_profit * 100:.2f}")

# Plotting profit curve and hill climbing path
x_values = [i * 0.01 for i in range(0, 601)]
y_values = [profit(x) for x in x_values]

plt.plot(x_values, y_values, label="Profit curve")
plt.plot(path_x, path_profit, 'ro-', label="Hill climbing path")
plt.xlabel("Production quantity (hundreds of bottles)")
plt.ylabel("Profit (hundreds of $)")
plt.title("Hill Climbing Optimization for Juice Production")
plt.legend()
plt.grid(True)
plt.show()

'''

# Practice Task 3
#Genetic Algorithm
#Based on natural selection and genetic evolution.
#Maintains a population of solutions.
#Uses selection, crossover, and mutation to evolve better solutions.

'''
import random

def fitness(x):
    return x**2 - 4*x + 4

def create_population(size):
    return [random.uniform(-10, 10) for _ in range(size)]

def crossover(p1, p2):
    return (p1 + p2) / 2

def mutate(x, rate=0.1):
    return x + random.uniform(-rate, rate)

def genetic_algorithm(generations=50, pop_size=10):
    population = create_population(pop_size)

    for _ in range(generations):
        population.sort(key=fitness)
        next_gen = population[:2]  # elitism

        while len(next_gen) < pop_size:
            p1, p2 = random.sample(population[:5], 2)
            child = crossover(p1, p2)
            child = mutate(child)
            next_gen.append(child)
        
        population = next_gen

    best = min(population, key=fitness)
    return best, fitness(best)

best_x, best_fit = genetic_algorithm()
print(f"Best solution: x = {best_x:

'''

# Lab Task
#Task 01: Implement the Hill Climbing algorithm in Python to find the optimal solution for maximizing the function
#f(x)=xsin(x)+cos(2x).

'''
import random
import math
# Objective function: f(x) = x*sin(x) + cos(2x)
def fitness(x):
    return x * math.sin(x) + math.cos(2 * x)
# Generate neighbor
def get_neighbor(x):
    step = random.uniform(-1, 1)
    return x + step
# Hill climbing algorithm
def hill_climbing(iterations=1000):
    current_x = random.uniform(-10, 10)
    current_fitness = fitness(current_x)
    for i in range(iterations):
        neighbor = get_neighbor(current_x)
        neighbor_fitness = fitness(neighbor)
        if neighbor_fitness > current_fitness:
            current_x, current_fitness = neighbor, neighbor_fitness
    return current_x, current_fitness
best_x, best_fit = hill_climbing()
print(f"Best Solution: x = {best_x:.3f}, f(x) = {best_fit:.3f}")
'''

#Task 02: Use Hill Climbing to help a robot climb a hill (2D surface) and find the highest point on the terrain represented by a mathematical function.
#f(x,y)=sin(x)⋅cos(y)

'''
import random
import math
# Objective function: f(x, y) = sin(x) * cos(y)
def fitness(x, y):
    return math.sin(x) * math.cos(y)
# Generate neighbor
def get_neighbor(x, y):
    step_x = random.uniform(-0.5, 0.5)
    step_y = random.uniform(-0.5, 0.5)
    return x + step_x, y + step_y
# Hill climbing algorithm
def hill_climbing(iterations=1000):
    current_x = random.uniform(-10, 10)
    current_y = random.uniform(-10, 10)
    current_fitness = fitness(current_x, current_y)
    for i in range(iterations):
        neighbor_x, neighbor_y = get_neighbor(current_x, current_y)
        neighbor_fitness = fitness(neighbor_x, neighbor_y)
        if neighbor_fitness > current_fitness:
            current_x, current_y, current_fitness = neighbor_x, neighbor_y, neighbor_fitness
    return current_x, current_y, current_fitness
best_x, best_y, best_fit = hill_climbing()
print(f"Best Position: x = {best_x:.3f}, y = {best_y:.3f}, f(x,y) = {best_fit:.3f}")

'''

#Task 03: Implement a Genetic Algorithm in Python to find the best solution for minimizing the function
#f(x) = x**2 - 10x + 25

'''
import random
def fitness(x):
    return x**2 - 10*x + 25
def create_population(size):
    return [random.uniform(-10, 10) for _ in range(size)]
def crossover(p1, p2):
    return (p1 + p2) / 2
def mutate(x, rate=0.1):
    return x + random.uniform(-rate, rate)
def genetic_algorithm(generations=50, pop_size=10):
    population = create_population(pop_size)
    for _ in range(generations):
        population.sort(key=fitness)
        next_gen = population[:2]  # elitism
        while len(next_gen) < pop_size:
            p1, p2 = random.sample(population[:5], 2)
            child = crossover(p1, p2)
            child = mutate(child)
            next_gen.append(child)
        population = next_gen
    best = min(population, key=fitness)
    return best, fitness(best)
best_x, best_fit = genetic_algorithm()
print(f"Best solution: x = {best_x:.3f}, f(x) = {best_fit:.3f}")
'''


#Task 04: Use a Genetic Algorithm to generate the best combination of ingredients for making a healthy fruit smoothie
# based on taste and nutrition score.
'''
import random
# Ingredient class
class Ingredient:
    def __init__(self, name, taste, nutrition):
        self.name = name
        self.taste = taste
        self.nutrition = nutrition
# Fitness function: combines taste and nutrition
def fitness(smoothie):
    total_taste = sum(ing.taste for ing in smoothie)
    total_nutrition = sum(ing.nutrition for ing in smoothie)
    return total_taste + total_nutrition
# Create initial population
def create_population(ingredients, size, smoothie_size):
    population = []
    for _ in range(size):
        smoothie = random.sample(ingredients, smoothie_size)
        population.append(smoothie)
    return population
# Crossover between two smoothies
def crossover(s1, s2):
    point = random.randint(1, len(s1) - 1)
    child = s1[:point] + s2[point:]
    return list({ing.name: ing for ing in child}.values())  # Remove duplicates
# Mutate a smoothie by replacing an ingredient
def mutate(smoothie, ingredients, mutation_rate=0.1):
    if random.random() < mutation_rate:
        idx = random.randint(0, len(smoothie) - 1)
        new_ing = random.choice(ingredients)
        smoothie[idx] = new_ing
    return smoothie
# Genetic Algorithm
def genetic_algorithm(ingredients, generations=50, pop_size=10, smoothie_size=3):
    population = create_population(ingredients, pop_size, smoothie_size)
    for _ in range(generations):
        population.sort(key=fitness, reverse=True)
        next_gen = population[:2]  # elitism
        while len(next_gen) < pop_size:
            p1, p2 = random.sample(population[:5], 2)
            child = crossover(p1, p2)
            child = mutate(child, ingredients)
            next_gen.append(child)
        population = next_gen
    best_smoothie = max(population, key=fitness)
    return best_smoothie, fitness(best_smoothie)
# Define ingredients
ingredients = [
    Ingredient("Banana", taste=8, nutrition=7),
    Ingredient("Strawberry", taste=9, nutrition=8),
    Ingredient("Spinach", taste=5, nutrition=10),
    Ingredient("Almond Milk", taste=7, nutrition=6),
    Ingredient("Chia Seeds", taste=6, nutrition=9),
    Ingredient("Mango", taste=9, nutrition=7),
    Ingredient("Kale", taste=4, nutrition=10),
]
# Run Genetic Algorithm
best_smoothie, best_score = genetic_algorithm(ingredients)
print("Best Smoothie Combination:")
for ing in best_smoothie:
    print(f"- {ing.name} (Taste: {ing.taste}, Nutrition: {ing.nutrition})")
print(f"Total Score (Taste + Nutrition): {best_score}")
'''


#conculsion:
'''
This lab demonstrated how optimization algorithms like Hill Climbing and Genetic Algorithms can be used to solve both mathematical 
and practical problems. Hill Climbing showed how a solution can be improved step-by-step by exploring nearby values, while Genetic
 Algorithms used selection, crossover, and mutation to evolve stronger solutions over generations. Through tasks involving function 
 maximization, terrain climbing, equation minimization, and smoothie optimization, we gained a clear understanding of how these 
 techniques work and how they can be applied in real-world scenarios.
'''