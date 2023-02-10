import random

class Organism:
    def __init__(self, fitness=0.0, mutations=0.0, mutation_rate=0.1, gui=None):
        self.fitness = fitness
        self.mutations = mutations
        self.mutation_rate = mutation_rate
        self.fitness_history = []
        self.gui = gui

    def reproduce(self, partner=None, times=1, mutation_rate=None):
        if mutation_rate is None:
            mutation_rate = self.mutation_rate
        for i in range(times):
            if partner is None:
                # Haploid Reproduction
                offspring_fitness = self.fitness
            else:
                # Diploid Reproduction - Not implemented
                offspring_fitness = (self.fitness + partner.fitness) / 2

            offspring = Organism(fitness=offspring_fitness, mutations=0.0, mutation_rate=mutation_rate)
            offspring.mutate(mutation_rate=mutation_rate)
            if self.gui:
                self.gui.update_graph()
        return offspring


    def mutate(self, mutation_rate=None):
        if mutation_rate is None:
            mutation_rate = self.mutation_rate
        # Add mutations
        mutations = random.normalvariate(0.0, mutation_rate)
        self.fitness = max(0.0, self.fitness + mutations)
        self.mutations += mutations

    def __repr__(self):
        return f"Organism(fitness={self.fitness:.2f}, mutations={self.mutations:.2f}, mutation_rate={self.mutation_rate:.2f})"
