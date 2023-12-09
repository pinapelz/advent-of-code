with open("input.txt", "r") as f:
    final_vals = []
    lines = f.read().splitlines()
    for data in lines:
        points = list(map(int, data.split()))
        diff = list(map(int, data.split()))
        history = [list(map(int, data.split()))]
        while not all(element == 0 for element in diff):
            diff = []
            for i in range(len(points)-1):
                x1 = points[i]
                x2 = points[i+1]
                diff.append(x2-x1)
            history.append(diff)
            points = diff
        history = list(reversed(history))
        for i in range(len(history)-1):
            history_1 = history[i]
            history_2 = history[i+1]
            extrapolated = history_1[len(history_1)-1] + history_2[len(history_2)-1]
            history[i+1].append(extrapolated)
        final_vals.append(history[len(history)-1][len(history[len(history)-1])-1])
    print("p1:", sum(final_vals))

with open("input.txt", "r") as f:
    final_vals = []
    lines = f.read().splitlines()
    for data in lines:
        points = list(map(int, data.split()))
        diff = list(map(int, data.split()))
        history = [list(map(int, data.split()))]
        while not all(element == 0 for element in diff):
            diff = []
            for i in range(len(points)-1):
                x1 = points[i]
                x2 = points[i+1]
                diff.append(x2-x1)
            history.append(diff)
            points = diff
        history = list(reversed(history))
        for i in range(len(history)-1):
            history_1 = history[i]
            history_2 = history[i+1]
            extrapolated = history_2[0] - history_1[0]
            history[i+1] = [extrapolated] + history[i+1]
        final_vals.append(extrapolated)
    print("p2:", sum(final_vals))