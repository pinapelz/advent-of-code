def find_mapping(seed, mapping):
    for rule in mapping:
        dest_start = rule[0]
        source_start = rule[1]
        length = rule[2]
        source_max = source_start + length
        if seed >= source_start and seed <= source_max:
            offset = seed - source_start
            return dest_start + offset
    return seed

with open("input.txt", "r") as f:
    content = [x.strip() for x in f.readlines() if x.strip() != ""]
    seeds = content[0]
    seeds = seeds.replace("seeds: ", "")
    seeds = list(map(int, seeds.split()))

    mappings = {}
    curr_map = ""
    for line in content[1:]:
        if "map:" in line:
            curr_map = line.strip()
        else:
            if curr_map in mappings:
                mappings[curr_map].append(tuple(map(int, line.split())))
            else:
                mappings[curr_map] = [tuple(map(int, line.split()))]
    results = []
    for seed in seeds:
        soil = find_mapping(seed, mappings["seed-to-soil map:"] )
        fertilizer = find_mapping(soil, mappings["soil-to-fertilizer map:"])
        water = find_mapping(fertilizer, mappings["fertilizer-to-water map:"])
        light = find_mapping(water, mappings["water-to-light map:"])
        temp = find_mapping(light, mappings["light-to-temperature map:"])
        humidity = find_mapping(temp, mappings["temperature-to-humidity map:"])
        location = find_mapping(humidity,mappings["humidity-to-location map:"])
        results.append(location)
    print(min(results))
