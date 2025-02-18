import random

def generate_cities(num_cities, randomize=True, seed=42):
    """Generate city coordinates."""
    if not randomize:
        random.seed(seed)  # Ensure predictable placement
    return [(random.randint(0, 100), random.randint(0, 100)) for _ in range(num_cities)]

def generate_cities_specific(num_cities, range=((0, 10),(0, 10)), seed=None):
    """Generate city coordinates. num_cities: integer, range=tuple of ((xmin, xmax)(ymin, ymax)), seed if specified"""
    if seed:
        random.seed(seed)  # Ensure predictable placement
    return [(random.randint(range[0][0], range[0][0]), random.randint(range[1][0], range[1][1])) for _ in range(num_cities)]