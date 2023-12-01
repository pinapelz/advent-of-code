def part_one():
    with open("input.txt", "r") as f:
        lines  = f.readlines()
        calibration_values = []
        for line in lines:
            first_digit = ""
            second_digit = ""
            for c in line:
                try:
                    int(c)
                    if first_digit == "":
                        first_digit = c
                    else:
                        second_digit = c
                except ValueError:
                    pass
            if first_digit != "":
                if second_digit == "":
                    second_digit = first_digit
                calibration_values.append(int(first_digit + second_digit))
    print(sum(calibration_values))

def part_two():
    def get_number(text):
        number_words = {
            'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
            'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
        }
        positions = []
        for word, digit in number_words.items():
            start = 0
            while word in text[start:]:
                found_at = text[start:].find(word)
                if found_at != -1:
                    positions.append((start + found_at, digit))
                    start += found_at + len(word)
                else:
                    break
        positions.sort(key=lambda x: x[0])
        for i, char in enumerate(text):
            if char.isdigit():
                positions.append((i, char))
        positions.sort(key=lambda x: x[0])
        if positions:
            return positions[0][1], positions[-1][1]
        else:
            return None, None
    
    with open("input.txt", "r") as f:
        lines  = f.readlines()
        calibration_values = []
        for line in lines:
            first_digit, second_digit = get_number(line)
            if first_digit != None:
                calibration_values.append(int(first_digit + second_digit))
    print(sum(calibration_values))

if __name__ == "__main__":
    part_one()
    part_two()



                