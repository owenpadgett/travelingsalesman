import DistanceFormulas as df

#pns

def pathNorm(path):
    """Returns the non-cyclical path normalized, so that reversed paths are considered equivalent.
    Input: List of ordered pairs: List of cities visited.
    Output: List of ordered pairs: List of cities visited (normalized)."""
    rev = path[::-1]
    if path[0][0] > rev[0][0]:
        return rev
    elif path[0][0] == rev[0][0]:
        if path[0][1] > rev[0][1]:
            return rev
        else: return path
    else: return path

