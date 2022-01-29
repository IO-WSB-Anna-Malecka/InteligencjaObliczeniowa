import pygad
import numpy
import time

przedmioty = ["zegar", "obraz-pejzaż", "obraz-portret", "radio", "laptop", "lampka nocna", "srebrne sztućce", "porcelana", "figura z brązu", "skórzana torebka", "odkurzacz"]
S = [100, 300, 200, 40, 500, 70, 100, 250, 300, 280, 300]
wagi = [7, 7, 6, 2, 5, 6, 1, 3, 10, 3, 15]

gene_space = [0, 1]

#definiujemy funkcję fitness
def fitness_func(solution, solution_idx):
    sumwartosc = numpy.sum(solution * S)
    sumwagi = numpy.sum(solution * wagi)
    if sumwagi > 25:
        return 0
    else:
        return sumwartosc
fitness_function = fitness_func

sol_per_pop = 11
num_genes = len(S)

num_parents_mating = 5
num_generations = 30
keep_parents = 2

parent_selection_type = "sss"


crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 8

ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes,
                       stop_criteria=["reach_1630"]

start = time.time()
ga_instance.run()
end = time.time()
print(end - start)

print("Number of generations passed is {generations_completed}".format(generations_completed=ga_instance.generations_completed))
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

prediction = numpy.sum(S*solution)
waga = numpy.sum(wagi*solution)
for index in range(len(solution)):
    if solution[index] == 1:
        print("%s" % przedmioty[index])

print("Predicted output based on the best solution : {waga} kg, {prediction} zł".format(prediction=prediction, waga=waga))

ga_instance.plot_fitness()
