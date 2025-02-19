import math
import numpy as np
import CityGeneration as cg
import itertools
import PathTools as pt

#pns

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

def depr_path_dist2(path):
    """Returns the distance traveled over the length of a path.
    Input: List of ordered pairs: List of city coordinates, in order.
    Output: float: Distance along the path."""
    return sum(dist2(path[i], path[i + 1]) for i in range(len(path) - 1))

def eff_path_dist2(path, dist_matrix):
    """Returns the distance traveled over the length of a path.
    Input: List of tuples (index: int, tuples (ordered pair of coordinates)): Named list of cities.
    Output: float: Distance along the path."""
    sum = 0
    for i in range(len(path)-1):
        sum += dist_matrix[i][i+1]
    return sum

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

def eff_brute_force_shortest_path(city_list, dist_matrix):
    """Find the shortest path using brute force.
    Input: List of ordererd pairs: List of city coordinates.
    Output: tuple (list of ordered pairs, float)."""
    min_distance = float('inf')
    best_path = None
    for perm in itertools.permutations(city_list):
        dist = eff_path_dist2(perm, dist_matrix)
        if dist < min_distance:
            min_distance = dist
            best_path = pt.pathNorm(perm)
    
    return best_path, min_distance

def _shortest_path(city_list):
        """Find the shortest path using brute force."""
        min_distance = float('inf')
        best_path = None
    
        for perm in itertools.permutations(city_list):
            normalized_perm = perm
            dist = depr_path_dist2(normalized_perm)
            if dist < min_distance:
                min_distance = dist
                best_path = normalized_perm
    
        return best_path, min_distance

def centroid2(city_list):
    """Finds the 'centroid' or center of mass of all the cities.
    Input: List of ordered pairs: List of city coordinates.
    Output: Ordered pair: Coordinates of the centroid."""
    ctr = (0,0)
    for i in city_list:
        ctr[0] += i[0]
        ctr[1] += i[1]
    return ctr/len(city_list)