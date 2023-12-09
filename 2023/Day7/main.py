from collections import defaultdict
from collections import Counter

with open("input.txt", "r") as f:
    lines = f.readlines()
    hands = []
    for line in lines:
        print(line)
        cards, bid = line.strip().split()[0], line.strip().split()[1]
        current_hand = defaultdict(int)
        for card in cards:
            current_hand[card] += 1
        hand_counter = Counter(current_hand.values())
        print(hand_counter)
        if len(current_hand.keys()) == 1 and hand_counter[5] == 1:
            hands.append((cards, bid,  "Five of a kind"))
        elif len(current_hand.keys()) == 2 and hand_counter[4] == 1:
            hands.append((cards, bid,  "Four of a kind"))
        elif len(current_hand.keys()) == 3 and hand_counter[3] == 1:
            hands.append((cards, bid,  "Three of a kind"))
        elif len(current_hand.keys()) == 2 and 2 in current_hand.values() and 3 in current_hand.values():
            hands.append((cards, bid, "Full house"))
        elif len(current_hand.keys()) == 3 and hand_counter[2] == 2:
            hands.append((cards, bid, "Two pair"))
        elif len(current_hand.keys()) == 4 and hand_counter[2] == 1:
            hands.append((cards, bid, "One pair"))
        else:
            hands.append((cards, bid, "High card"))
    high_cards = [hand for hand in hands if hand[2] == "High card"]
    one_pair = [hand for hand in hands if hand[2] == "One pair"]
    two_pair = [hand for hand in hands if hand[2] == "Two pair"]
    full_house = [hand for hand in hands if hand[2] == "Full house"]
    three_kind = [hand for hand in hands if hand[2] == "Three of a kind"]
    four_kind = [hand for hand in hands if hand[2] == "Four of a kind"]
    five_kind = [hand for hand in hands if hand[2] == "Five of a kind"]
    
    point_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

    # sort each list above according to the point values for each category go card by card elft to right
    # if the next card is the same, then compare the next card
    
    sorted_high_cards = sorted(high_cards, key=lambda x: (point_values[x[0][0]], point_values[x[0][1]], point_values[x[0][2]], point_values[x[0][3]], point_values[x[0][4]]))
    sorted_one_pair = sorted(one_pair, key=lambda x: (point_values[x[0][0]], point_values[x[0][1]], point_values[x[0][2]], point_values[x[0][3]], point_values[x[0][4]]))
    sorted_two_pair = sorted(two_pair, key=lambda x: (point_values[x[0][0]], point_values[x[0][1]], point_values[x[0][2]], point_values[x[0][3]], point_values[x[0][4]]))
    sorted_full_house = sorted(full_house, key=lambda x: (point_values[x[0][0]], point_values[x[0][1]], point_values[x[0][2]], point_values[x[0][3]], point_values[x[0][4]]))
    sorted_three_kind = sorted(three_kind, key=lambda x: (point_values[x[0][0]], point_values[x[0][1]], point_values[x[0][2]], point_values[x[0][3]], point_values[x[0][4]]))
    sorted_four_kind = sorted(four_kind, key=lambda x: (point_values[x[0][0]], point_values[x[0][1]], point_values[x[0][2]], point_values[x[0][3]], point_values[x[0][4]]))
    sorted_five_kind = sorted(five_kind, key=lambda x: (point_values[x[0][0]], point_values[x[0][1]], point_values[x[0][2]], point_values[x[0][3]], point_values[x[0][4]]))



    final_hand = []
    for hand in sorted_high_cards:
        final_hand.append(hand)
    for hand in sorted_one_pair:
        final_hand.append(hand)
    for hand in sorted_two_pair:
        final_hand.append(hand)
    for hand in sorted_full_house:
        final_hand.append(hand)
    for hand in sorted_three_kind:
        final_hand.append(hand)
    for hand in sorted_four_kind:
        final_hand.append(hand)
    for hand in sorted_five_kind:
        final_hand.append(hand)

    total_winning = 0
    multiplier = 1
    for hand in final_hand:
        total_winning += int(hand[1]) * multiplier
        multiplier += 1
    print(total_winning)

        
   
        