import itertools
import DistanceFormulas as df

#pns

class TravelingSalesmanBase():
    def __init__(self, city_list):
        """Initializes a Traveling Salesman problem instance.
        city_list: tuple of ordered pairs (tuples): coordinates of each city in the TS problem"""
        self.raw_city_list = city_list
        self.named_city_list = self._name_cities()
        self._len = len(city_list)
        self.shortest_dist = self._shortest_dist()
    
    def __len__(self):
        """Returns the number of cities in the TS problem."""
        return self._len

    def _name_cities(self):
        name_list = []
        idx = 0
        for i in self.raw_city_list:
            name_list.append((idx, i))
            idx += 1

    def _shortest_path(self):
        """Find the shortest path using brute force."""
        min_distance = float('inf')
        best_path = None
    
        for perm in itertools.permutations(self.city_list):
            normalized_perm = perm
            dist = df.path_dist2(normalized_perm)
            if dist < min_distance:
                min_distance = dist
                best_path = normalized_perm
    
        return best_path, min_distance