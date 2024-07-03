import numpy as np


def fitness(population:np.ndarray, n:int) -> np.ndarray:
    m = len(population)
    penalty = np.zeros(m)
    for i in range(m):
        chromosome = population[i]
        slot = chromosome.reshape(n, -1)
        overlap, consistent = 0, 0

        for j in range(n):
            tmp = np.sum(slot[j,:])
            overlap += abs(tmp-1)
            tmp = np.sum(slot[:,j])
            consistent += abs(tmp-1)
        penalty[i] = -(overlap+consistent)

    return penalty

def random_selection(population:np.ndarray) -> np.ndarray:
    choices = np.random.choice(len(population), size=2, replace=False)
    return population[choices[0]], population[choices[1]]


def single_point_crossover(x, y):
    l = len(x)
    point = np.random.randint(1, l)
    off1 = np.concatenate([x[:point], y[point:]])
    off2 = np.concatenate([y[:point], x[point:]])
    return off1,off2


def mutate(child, mutation_threshold=0.3):
    n = len(child)
    for i in range(n):
      x = np.random.random()
      if x<mutation_threshold:
        child[i] = 1 - child[i]
    return child



def GA(population, n, mutation_threshold = 0.3):
    for k in range(1000):
        for i in range(5):
            parent1, parent2 = random_selection(population)
            offspring1, offspring2 = single_point_crossover(parent1, parent2)
            offspring1 = mutate(offspring1)
            offspring2 = mutate(offspring2)
            population = np.concatenate((population,[offspring1]))
            population = np.concatenate((population,[offspring2]))
        penalties = fitness(population, n)
        best_results = np.argsort(penalties)
        best_results = best_results[-10:]
        population = np.array(population)[best_results]
        penalties = fitness(population, n)
        best_res = np.argmax(penalties)
        if penalties[best_res]==0:
            break
    print(population[best_res])
    print(penalties[best_res])
    return

"""
    Driver Code
"""
ks = []
with open('input.txt') as f:
    store = f.readline().split()
    n, t = store
    n, t = int(n), int(t)
    for i in range(n):
        ks.append(f.readline().strip("\n"))


start_population = 10
population = np.random.randint(0, 2, (start_population, n*t))
GA(population,n)
