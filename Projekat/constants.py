CAPACITY = 0
ITEMS = []
def load():
    with open("data_knapsack01.txt", "r") as f:
        line = f.readline()
        CAPACITY = int(line.split(" ")[1])
        while True:
            line = f.readline()
            if not line:
                break
            ITEMS.append([int(line.split(",")[0]), int(line.split(",")[1])])
    return CAPACITY
CAPACITY = load()