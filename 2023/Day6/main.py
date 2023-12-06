def calculate_ways(time, distance):
    ways_to_win = []
    for hold_time in range(time):
        speed = hold_time  
        travel_time = time - hold_time 
        distance_traveled = speed * travel_time
        if distance_traveled > distance:
            ways_to_win.append(hold_time)
    return len(ways_to_win)

times = ["VALUES"]
distances = ["DISTANCES"]

result = 1
for i in range(len(times)):
    ways = calculate_ways(time=times[i], distance=distances[i])
    result *= ways
print(result)


single_time = int("".join(map(str, times))) 
single_distance = int("".join(map(str, distances))) 
single_race_ways = calculate_ways(single_time, single_distance)
print(single_race_ways)
