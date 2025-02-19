import DistanceFormulas as df
import time

#pns

city_list = ((1, 150), 
             (2, 145),
             (5, 109),
             (10, 104),
             (13, 78),
             (26, 73),
             (29, 55),
             (58, 50),
             (61, 38),
             (122, 33),
             (125, 25)
             )

name_list = []
idx = 0
for i in city_list:
    name_list.append((idx, i))
    idx += 1

timeOld = -time.time()
oldResult = df._shortest_path(city_list)
timeOld += time.time()

dist_matrix = df.dist_matrix2(city_list)
timeNew = -time.time()
newResult = df.eff_brute_force_shortest_path(city_list, dist_matrix)
timeNew += time.time()

print(timeOld)
print(oldResult[1])
print(timeNew)
print(newResult[1])