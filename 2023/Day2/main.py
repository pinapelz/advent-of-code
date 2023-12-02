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
                if not part_two:
                    if num_red > 12 or num_green > 13 or num_blue > 14:
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





    
