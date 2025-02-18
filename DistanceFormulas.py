import math
import numpy as np
import CityGeneration as cg

def dist2(city1, city2=(0,0)):
    """Euclidean distance or l2 norm between two cities in R^2:
    Input: Ordered pair, with optional second ordered pair: If no second city specified, then distance to origin.
    Output: float: Distance between two cities."""
    return math.sqrt((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2)

def dist3(city1, city2=(0,0,0)):
    """Euclidean distance or l2 norm between two cities in R^3
    Input: Ordered triple, with optional second ordered triple: If no second city specified, then distance to origin.
    Output: float: Distance between two cities."""
    return math.sqrt((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2 + (city1[2]-city2[2])**2)

def path_dist2(path):
    """Returns the distance traveled over the length of a path.
    Input: List of ordered pairs: List of city coordinates, in order.
    Output: float: Distance along the path."""
    return sum(dist2(path[i], path[i + 1]) for i in range(len(path) - 1))

def dist_matrix2(city_list):
    """Returns a symmetric matrix representing the distance between each city.
    Input: List of ordered pairs: list of city coordinates.
    Output: 2D NumPy Array: Each entry is the distance between the row-th city and the column-th city."""
    n = len(city_list)
    dist_mat_temp = [[0.0 for _ in range(n)] for _ in range(n)]

    dist_matrix = np.array(dist_mat_temp)

    for i in range(n):
        for j in range (n):
            if i <= j:
                pass
            else:
                dist_matrix[i][j] = dist2(city_list[i], city_list[j])
    
    return np.add(dist_matrix, dist_matrix.transpose())
