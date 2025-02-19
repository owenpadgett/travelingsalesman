import CityGeneration as cg
import DistanceFormulas as df
import ConvexHull as ch
import matplotlib.pyplot as plt
import numpy as np

iterations = 1000
n = 5
v = 10
m = 0.05

def linear_piecewise(t):
    return v - m * t

# Two lists to track frequencies separately
same_path_counts = [0] * n  # When shortest and fastest paths are the same
diff_path_counts = [0] * n  # When shortest and fastest paths are different

for _ in range(iterations):
    cities = cg.generate_cities(n)
    hull_size = len(ch.get_convex_hull(cities))  # Number of sides in convex hull

    shortest_path = df.eff_brute_force_shortest_path(cities, df.dist_matrix2(cities))
    fastest_path = df.eff_brute_force_fastest_path(cities, df.dist_matrix2(cities), linear_piecewise)

    if shortest_path[0] == fastest_path[0]:
        same_path_counts[hull_size - 1] += 1
    else:
        diff_path_counts[hull_size - 1] += 1

# X-axis values (convex hull sizes)
x_values = np.arange(1, n + 1)

# Plot stacked bar chart
plt.bar(x_values, same_path_counts, color='skyblue', edgecolor='black', label="Same Paths")
plt.bar(x_values, diff_path_counts, color='salmon', edgecolor='black', bottom=same_path_counts, label="Different Paths")

# Labels and formatting
plt.xlabel("Number of Sides in Convex Hull")
plt.ylabel("Frequency of Occurrence")
plt.title("Shortest vs Fastest Path Distribution by Convex Hull Size")
plt.xticks(x_values)  # Ensure x-axis labels match convex hull sizes
plt.legend()  # Show the legend for color meanings
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

shortest_path = df.eff_brute_force_shortest_path(cities, df.dist_matrix2(cities))
fastest_path = df.eff_brute_force_fastest_path(cities, df.dist_matrix2(cities), linear_piecewise)

print(f"Shortest Path: {shortest_path}")
print(f"Fastest Path: {fastest_path}")
if shortest_path[0] == fastest_path[0]:
    print("The shortest and fastest paths are the same.")