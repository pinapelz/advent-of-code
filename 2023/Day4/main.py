with open("input.txt") as f:
    processed = []
    for line in f.readlines():
        if not line.strip():
            continue
        line = line.strip()
        garbage, data = line.split(": ")
        processed.append(data)
    pts = []
    for line in processed:
        win, nums = line.split(" | ")
        win = set(map(int, win.split()))
        nums = set(map(int, nums.split()))
        winners = win.intersection(nums)
        points = 1 if winners else 0
        for _ in range(1, len(winners)):
            points *= 2
        pts.append(points)
    print(sum(pts))

    totalcards = len(processed)
    card_counts = [1] * totalcards
    for i in range(totalcards):
        win, nums = processed[i].split(" | ")
        win = set(map(int, win.split()))
        nums = set(map(int, nums.split()))
        winners = win.intersection(nums)
        for j in range(i + 1, i + 1 + len(winners)):
            # You win copies of the cards directly below it.
            # As such we start at i+1 and go down however many winners there are,
            card_counts[j] += card_counts[i]
    print(sum(card_counts))

