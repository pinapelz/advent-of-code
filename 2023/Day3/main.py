import re
# Certainly not the efficient way to do this problem but uhh it got the right answer
with open("input.txt", "r") as f:
    # Parse the input into lines
    schematic = f.read()
    total = 0
    symbol_pos = []
    grid = [line for line in schematic.split("\n") if line.strip() != ""]
    for i in range(len(grid)):
        # Iterate through each line
        for j in range(len(grid[i])):
            # Iterate through each character in the grid
            if not grid[i][j].isdigit() and grid[i][j] != ".":
                # If its a symbol we store its position as a tuple into a list
                symbol_pos.append((i, j))
    for i in range(len(grid)):
        # Iterate through each line
        for m in re.finditer(r"\d+", grid[i]):
            # Find all the numbers in the line, m becomes a match object for each number
            num = int(m.group())  # Take the current number from the match object and convert it to an int
            start, end = m.span() # Get the start and end index of the number using match object's span
            for j in range(start, end): # j becomes the position we should check for adjacency
                adjacent_to_symbol = False
                for symbol in symbol_pos: # Check every symbol to see if it is adjacent to the number
                    # symbol[0] = row, symbol[1] = column
                    if (abs(i - symbol[0]) <= 1 and abs(j - symbol[1]) <= 1):
                        """
                        We know that the number is adjacent to a symbol if both the row and column are within 
                        1 tile from the symbol's row and column 
                        ...
                        .x.
                        ...
                        As shown to be adjacent the distance between the number and the symbol must be less than or equal to 1
                        """
                        adjacent_to_symbol = True
                        break
                if adjacent_to_symbol:
                    # If the number is adjacent to a symbol we add it to the total and break out of the loop
                    total += num
                    break 
    # Part 2 is basically the same thing but with numbers instead of symbols
    num_pos = []
    total_2 = 0
    for i, row in enumerate(grid):
        # We find each number and store its data as a tuple: (row, col, value) value = the number itself
        for m in re.finditer(r"\d+", row):
            num = int(m.group())
            start, end = m.span()
            for j in range(start, end):
                num_pos.append((i, j, num))
    for i in range(len(grid)):
        # Iterate through each line
        for j in range(len(grid[i])):
            if grid[i][j] == "*":
                # If its a gear then we need to check if there are 2 numbers adjacent to it
                unique_nums = set()
                for x, y, num in num_pos:
                    if (abs(i - x) <= 1 and abs(j - y) <= 1):
                        # exact same logic as what was used previously for checking adjacency
                        unique_nums.add(num)
                if len(unique_nums) == 2:
                    total_2 += unique_nums.pop() * unique_nums.pop()
print(total)
print(total_2)