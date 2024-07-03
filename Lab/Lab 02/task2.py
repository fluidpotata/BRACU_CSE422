import numpy as np


def random_selection(population:np.ndarray) -> np.ndarray:
    choices = np.random.choice(len(population), size=2, replace=False)
    return population[choices[0]], population[choices[1]]


def two_point_crossover(x,y):
    point1 = np.random.randint(1,len(x)-1)
    point2 = np.random.randint(point1+1, len(x))
    # print(point1,point2)
    offspring1 = np.concatenate([x[:point1],y[point1:point2],x[point2:]])
    offspring2 = np.concatenate([y[:point1],x[point1:point2],y[point2:]])
    # print(offspring1,offspring2)
    return offspring1, offspring2


def GA(population):
    parent1, parent2 = random_selection(population)
    offspring1, offspring2 = two_point_crossover(parent1, parent2)
    print(offspring1,offspring2)


start_population = 10
population = np.random.randint(0, 2, (start_population, 9))
GA(population)

