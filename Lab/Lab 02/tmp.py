import numpy as np
import numpy.typing as npt

def fitness(population, n):
    """Calculates the fitness score of each individual in the population.

    Args:
        population: A 2D numpy array representing the population of chromosomes.
        n: An integer representing the number of courses.

    Returns:
        A 1D numpy array where the index refers to the ith individual
        in the population, and the value refers to the fitness score.
    """

    fitness_scores = np.zeros(len(population))
    for i, chromosome in enumerate(population):
        print(f"Choromosome: {chromosome}")
        schedule = chromosome.reshape(n, -1)  # Reshape into n courses x timeslots
        overlap_penalty = 0
        consistency_penalty = 0
        print(f"schedule: {schedule}")

        for timeslot in range(n):
            courses_in_timeslot = np.sum(schedule[timeslot, :])
            overlap_penalty += courses_in_timeslot - 1
        # print(f"Overlap penalty: {overlap_penalty}")
        # for course in range(n):
            times_scheduled = np.sum(schedule[:, timeslot])
            consistency_penalty += abs(times_scheduled - 1)
        print(f'Consistency penalty: {consistency_penalty}')

        fitness_scores[i] = - (overlap_penalty + consistency_penalty)
        print(f"Fitness SCore{fitness_scores}")

    return fitness_scores


def random_selection(population):
    """Randomly selects two parents from the population."""
    indices = np.random.choice(len(population), size=2, replace=False)
    return population[indices[0]], population[indices[1]]

def crossover(x, y):
    """Performs single-point crossover between two parents."""
    crossover_point = np.random.randint(1, len(x))
    child1 = np.concatenate([x[:crossover_point], y[crossover_point:]])
    child2 = np.concatenate([y[:crossover_point], x[crossover_point:]])
    return child1, child2

def mutate(child, mutation_threshold):
    """Mutates a child chromosome based on the mutation rate."""
    for i in range(len(child)):
        if np.random.random() < mutation_threshold:
            child[i] = 1 - child[i]  # Flip the bit
    return child

def GA(population, n, mutation_threshold=0.1, max_iterations=10):
    """Runs the genetic algorithm to find the optimal course schedule."""

    for _ in range(max_iterations):
        fit = fitness(population, n)

        # Randomly select two parents
        parent1, parent2 = random_selection(population)
        new_population = [parent1, parent2]  # Start with the parents

        # Create 10 more offspring (total 20)
        while len(new_population) < 20:
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_threshold)
            child2 = mutate(child2, mutation_threshold)
            new_population.extend([child1, child2])

        # Select the top 10 fittest from the 20 offspring
        fit_offspring = fitness(np.array(new_population), n)
        top_indices_offspring = np.argsort(fit_offspring)[-10:]
        population = np.array(new_population)[top_indices_offspring]

        best_index = np.argmax(fit)
        best_chromosome = population[best_index]
        if fit[best_index] == 0:  # Optimal solution found
            break

    print("Best chromosome:", best_chromosome)
    print("Fitness value:", fit[best_index])
    return best_chromosome
# ... (Your file reading code to get courses and n)

start_population = 5  # Adjust as needed
population_size = 10 # Adjust as needed
population = np.random.randint(0, 2, (population_size, n*t))

best_chromosome = GA(population, n)



courses = []
with open('input.txt') as f:
    store = f.readline().split()
    n, t = store
    n, t = int(n), int(t)
    print(store)
    for i in range(n):
        courses.append(f.readline().strip("\n"))


start_population = 5
population = np.random.randint(0, 2, (start_population, n*t))
# GA(population,n)
# print(population)
# fitness(np.array([[1, 1, 0, 0, 0, 0, 1, 1, 0], [1, 1, 1, 1, 0, 0, 0, 0, 0]]),n)
fitness(np.array([[1,1,0,1,1,0,0,1,0]]),n)