def dest(source, mapping_rules):
    for destination_start, source_start, length in mapping_rules:
        if source_start <= source < source_start + length:
            offset = source - source_start
            return destination_start + offset
    return source

with open("input.txt", 'r') as file:
    content = file.readlines()
seeds_line = content[0]
seeds = list(map(int, seeds_line.split(':')[1].split()))
mapping_sections = {'seed-to-soil': [], 'soil-to-fertilizer': [], 'fertilizer-to-water': [],
                    'water-to-light': [], 'light-to-temperature': [], 'temperature-to-humidity': [],
                    'humidity-to-location': []}

current_section = {}
for line in content:
    if 'map:' in line:
        current_section = line.split()[0]
    elif current_section:
        mapping_sections[current_section].append(line)
for key in mapping_sections:
    mapping_sections[key] = [tuple(map(int, line.split())) for line in mapping_sections[key] if line.strip()]
location_numbers = []
for seed in seeds:
    soil = dest(seed, mapping_sections['seed-to-soil'])
    fertilizer = dest(soil, mapping_sections['soil-to-fertilizer'])
    water = dest(fertilizer, mapping_sections['fertilizer-to-water'])
    light = dest(water, mapping_sections['water-to-light'])
    temperature = dest(light, mapping_sections['light-to-temperature'])
    humidity = dest(temperature, mapping_sections['temperature-to-humidity'])
    location = dest(humidity, mapping_sections['humidity-to-location'])
    location_numbers.append(location)

print(min(location_numbers))



