def part_1():
	from collections import defaultdict
	with open("input.txt") as f:
		lines = f.readlines()
		direction = lines[0].strip()
		m_map = defaultdict()
		for path in lines[2:]:
			node, choice = path.strip().split("=")
			node = node.strip()
			choice = choice.strip()
			left, right = choice[1:-1].split(", ")
			choice = (left,right)
			m_map[node] = choice

	curr_node = "AAA"
	index = 0
	steps = 0
	while curr_node != "ZZZ":
		if direction[index] == "R":
			curr_node = m_map[curr_node][1]
		else:
			curr_node = m_map[curr_node][0]
		index += 1
		steps += 1
		if index == len(direction):
			index = 0
	print(steps)




from collections import defaultdict
with open("input.txt") as f:
	lines = f.readlines()
	direction = lines[0].strip()
	m_map = defaultdict()
	for path in lines[2:]:
		node, choice = path.strip().split("=")
		node = node.strip()
		choice = choice.strip()
		left, right = choice[1:-1].split(", ")
		choice = (left,right)
		m_map[node] = choice

curr_nodes = []
end_nodes = []
for node in m_map.keys():
	if node.endswith("A"):
		curr_nodes.append(node)
	if node.endswith("Z"):
		end_nodes.append(node)

import math



index = 0

total_steps = []
for node in curr_nodes:
	steps = 0
	curr_node = node
	while not curr_node.endswith("Z"):
		for d in direction:
			if d == "R":
				curr_node = m_map[curr_node][1]
			else:
				curr_node = m_map[curr_node][0]
			steps += 1
	total_steps.append(steps)

print(math.lcm(*total_steps))


        
        



    