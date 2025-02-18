import random
import numpy as np

def generate_cities(num_cities, randomize=True, seed=42):
    """Generate city coordinates."""
    if not randomize:
        random.seed(seed)  # Ensure predictable placement
    return [(random.randint(0, 100), random.randint(0, 100)) for _ in range(num_cities)]

def generate_cities_specific(num_cities, range=((0, 10),(0, 10)), seed=None):
    """Generate city coordinates. 
    num_cities: integer: number of cities desired
    range: tuple of ((xmin, xmax)(ymin, ymax)): defines bounds that cities can generate in
    seed if specified"""
    if seed:
        random.seed(seed)  # Ensure predictable placement
    return [(random.randint(range[0][0], range[0][0]), random.randint(range[1][0], range[1][1])) for _ in range(num_cities)]


def generate_arrowhead():
    tipPoint = (random.randint(0, 100), random.randint(0, 100))
    corner1 = (random.randint(0, tipPoint[0]), random.randint(0, tipPoint[1]))
    corner2 = (random.randint(tipPoint[0], 100), random.randint(0, tipPoint[1]))

    # Define the vectors AB and AC
    AB = np.array(corner1) - np.array(tipPoint)
    AC = np.array(corner2) - np.array(tipPoint)

    # Generate two random uniform variables
    u1 = np.random.uniform(0, 1)
    u2 = np.random.uniform(0, 1)

    # Swap u2 with 1 - u2 if u1 + u2 > 1 to ensure the point lies inside the triangle
    if u1 + u2 > 1:
        u1 = 1 - u1
        u2 = 1 - u2

    # Compute the random point as a linear combination of the vectors
    insidePoint = tuple(tipPoint + u1 * AB + u2 * AC)


    return [tipPoint,corner1,corner2,insidePoint]


    
