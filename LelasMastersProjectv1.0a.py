import itertools
import random
import math
import matplotlib.pyplot as plt
import time


def generate_cities(num_cities, randomize=True, seed=42):
    """Generate city coordinates."""
    if not randomize:
        random.seed(seed)  # Ensure predictable placement
    return [(random.randint(0, 100), random.randint(0, 100)) for _ in range(num_cities)] 

def euclidean_distance(a, b):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def total_distance(path):
    """Calculate the total distance of a path."""
    return sum(euclidean_distance(path[i], path[i + 1]) for i in range(len(path) - 1))

def compute_travel_times(path, v0, m):
    """Compute travel times based on the given formula."""
    travel_times = []
    sum_t = 0
    for i in range(len(path) - 1):
        distance = euclidean_distance(path[i], path[i + 1])
        t_i = distance / (v0 - m * sum_t)
        travel_times.append(t_i)
        sum_t += t_i
    return sum(travel_times), travel_times

def normalize_path(path):
    """Normalize path to account for reverse equivalence."""
    # Normalize by comparing the path with its reverse and picking the lexicographically smaller one
    if path > path[::-1]:
        path = path[::-1]
    return path

def brute_force_tsp(cities):
    """Find the shortest path using brute force."""
    min_distance = float('inf')
    best_path = None
    
    for perm in itertools.permutations(cities):
        normalized_perm = normalize_path(perm)
        dist = total_distance(normalized_perm)
        if dist < min_distance:
            min_distance = dist
            best_path = normalized_perm
    
    return best_path, min_distance

def fastest_tsp(cities, v0, m):
    """Find the fastest path considering travel time."""
    min_time = float('inf')
    best_time_path = None
    
    for perm in itertools.permutations(cities):
        normalized_perm = normalize_path(perm)
        total_time, _ = compute_travel_times(normalized_perm, v0, m)
        if total_time < min_time:
            min_time = total_time
            best_time_path = normalized_perm
    
    return best_time_path, min_time

def plot_tsp(cities, best_path, fastest_path):
    """Plot the cities, shortest path, and fastest path."""
    x, y = zip(*cities)
    plt.scatter(x, y, c='red', marker='o', label='Cities')
    
    path_x, path_y = zip(*best_path)  # Shortest path
    plt.plot(path_x, path_y, 'b-', label='Shortest Path')
    
    fast_x, fast_y = zip(*fastest_path)  # Fastest path
    plt.plot(fast_x, fast_y, 'g--', label='Fastest Path')
    
    for i, (cx, cy) in enumerate(cities):
        plt.text(cx, cy, str(i), fontsize=12, ha='right')
    
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Traveling Salesman Problem')
    plt.legend()
    plt.show()

# Configurable parameters
NUM_CITIES = 4
RANDOMIZE_CITIES = True
SEED = 42
V0 = 10  # Initial velocity
M = 0.05  # Deceleration factor

# Generate cities
cities = generate_cities(NUM_CITIES, RANDOMIZE_CITIES, SEED)
    
# Solve for shortest path
best_path, best_distance = brute_force_tsp(cities)
best_time, _ = compute_travel_times(best_path, V0, M)  # Get time for shortest path
    
# Solve for fastest path
fastest_path, fastest_time = fastest_tsp(cities, V0, M)
fastest_distance = total_distance(fastest_path)  # Get distance for fastest path
    
print("Cities:", cities)
print("Shortest path:", best_path)
print("Shortest distance:", best_distance)
print("Shortest path travel time:", best_time)
print("Fastest path:", fastest_path)
print("Fastest travel time:", fastest_time)
print("Fastest path distance:", fastest_distance)
    
# Plot the result
plot_tsp(cities, best_path, fastest_path)