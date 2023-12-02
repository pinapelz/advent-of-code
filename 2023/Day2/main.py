"""
You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
"""
import re
def solve(part_two=False):
    with open("input.txt", "r") as f:
        games = f.read().splitlines()
        possible_games_id_sum = 0
        sum_of_power = 0
        for game in games:
            game_id = int(re.search(r"\d+", game).group())
            game = game.replace(f"Game {game_id}: ", "")
            game_possible = True
            largest_red = largest_green = largest_blue = 0
            for round in game.split("; "):
                num_red = num_green = num_blue = 0
                for cube in round.split(", "):
                    count, color = cube.split(" ")
                    if "red" in color:
                        num_red = int(count)
                    elif "green" in color:
                        num_green = int(count)
                    elif "blue" in color:
                        num_blue = int(count)


                if num_red > 12 or num_green > 13 or num_blue > 14 and not part_two:
                    game_possible = False
                    break

                if num_red > largest_red:
                    largest_red = num_red
                if num_green > largest_green:
                    largest_green = num_green
                if num_blue > largest_blue:
                    largest_blue = num_blue

            if game_possible:
                power = largest_red * largest_green * largest_blue
                sum_of_power += power
                possible_games_id_sum += game_id
    if part_two:
        return sum_of_power
    else:
        return possible_games_id_sum

print(solve())
print(solve(part_two=True))




    
