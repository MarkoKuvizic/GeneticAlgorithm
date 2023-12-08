from unit import *
from matplotlib import pyplot as plt
import numpy as np
current_generation = []
points = []
def init_unit():
    items = []
    items = random.choices([0,1], k = len(ITEMS), weights=[1, 1])
    return Unit(items)
def init_generation(N = 100):
    global current_generation
    for i in range(N):
        current_generation.append(init_unit())
    #current_generation = sorted(current_generation, key = lambda x: -x.value)
def roulette_selection(N = 50, elitism = 2):
    elitism = N/25
    global current_generation
    global points
    pop_fitness = sum([unit.value for unit in current_generation])
    probabilities = [unit.value/pop_fitness for unit in current_generation]
    parents = random.choices(current_generation, weights=probabilities, k=2*N)
    next_generation = []
    for i in range(1, 2*N+1, 2):
        children = generate_children(parents[i-1].items, parents[i].items)
        next_generation.append(children[0])
        next_generation.append(children[1])
    parents_and_children = current_generation + next_generation
    parents_and_children = sorted(parents_and_children, key = lambda x : -x.value)

    next_generation = []
    for el in (parents_and_children):
        if(len(next_generation) == 2*N):
            break
        if el in current_generation:
            if(elitism > 0):
                elitism -= 1
                next_generation.append(el)
                continue
        next_generation.append(el)
    current_generation = next_generation
    
    points.append(current_generation[0].value)

def generate_children(p1, p2):
    a = random.randint(0, len(p1))
    b = random.randint(0, len(p1))
    l = [p1, p2]
    x = 0
    c1 = []
    c2 = []
    for i in range(len(p1)):
        if(x == a or x == b):
            x = 1-x
        c1.append(l[x][i])
        c2.append(l[1-x][i])
        if (random.randint(0, 10) == 2):
            c1[-1] = 1-c1[-1]
        if (random.randint(0, 10) == 2):
            c2[-1] = 1-c2[-1]
    return [Unit(c1), Unit(c2)]
def run_algorithm(iter = 300, N = 50):
    init_generation(N)
    global current_generation

    for i in range(iter):
        roulette_selection(int(N/2))
    global points
    current_generation = sorted(current_generation, key = lambda x : x.value)
    print("POBEDNICKA JEDINKA IMA VREDOST: ", current_generation[0].value)
    print("TEZINU: ", current_generation[0].weight)
    print("KODIRANJE POBEDNICKE JEDINKE")
    print(current_generation[0].items)
    b = np.arange(0, iter, 1)
    plt.plot(b, points)
    plt.show()
def main():
    iter = int(input("UNESITE BROJ ITERACIJA: "))
    N = int(input("UNESITE BROJ JEDINKI: "))
    run_algorithm(iter, N)
    
if __name__ == "__main__":
    main()
