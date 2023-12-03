import re

with open("input.txt", "r") as f:
    schematic = f.read()
    total = 0
    symbol_pos = []
    grid = [line for line in schematic.split("\n") if line.strip() != ""]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if not grid[i][j].isdigit() and grid[i][j] != ".":
                symbol_pos.append((i, j))
    for i in range(len(grid)):
        for m in re.finditer(r"\d+", grid[i]):
            num = int(m.group())
            start, end = m.span()
            for j in range(start, end):
                adjacent_to_symbol = False
                for symbol in symbol_pos:
                    if (abs(i - symbol[0]) <= 1 and abs(j - symbol[1]) <= 1):
                        adjacent_to_symbol = True
                        break
                if adjacent_to_symbol:
                    total += num
                    break 
    num_pos = []
    total_2 = 0
    for i, row in enumerate(grid):
        for m in re.finditer(r"\d+", row):
            num = int(m.group())
            start, end = m.span()
            for j in range(start, end):
                num_pos.append((i, j, num))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "*":
                unique_nums = set()
                for x, y, num in num_pos:
                    if (abs(i - x) <= 1 and abs(j - y) <= 1):
                        unique_nums.add(num)
                if len(unique_nums) == 2:
                    total_2 += unique_nums.pop() * unique_nums.pop()
print(total)
print(total_2)