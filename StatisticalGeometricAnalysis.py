import CityGeneration as cg
import DistanceFormulas as df
import ConvexHull as ch
import matplotlib.pyplot as plt

iterations=1000
n=4
v=10
m=0.05

def linear_piecewise(t):
    return v-m*t

plotValues=[0]*n

for i in range(iterations):
    cities=cg.generate_cities(n)
    shortestPath=df.eff_brute_force_shortest_path(cities, df.dist_matrix2(cities))
    fastestPath=df.eff_brute_force_fastest_path(cities, df.dist_matrix2(cities),linear_piecewise())

    if shortestPath[0]!=fastestPath[0]:
        polygon=len(ch.get_convex_hull(cities))
        plotValues[polygon-1]+=1

x_values = list(range(1, n + 1))  # Polygon side numbers (1 to n)
y_values = plotValues  # Accumulated values

plt.bar(x_values, y_values, color='skyblue', edgecolor='black')  # Create bar chart
plt.xlabel("Number of Sides in Convex Hull")
plt.ylabel("Frequency of Occurrence")
plt.title("Distribution of Convex Hull Side Counts")
plt.xticks(x_values)  # Ensure x-axis labels match side numbers
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines for readability
plt.show()  # Display the graph

