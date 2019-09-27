import abc
import random


class GeneticShape(abc.ABC):
    def __init__(self) -> None:
        super().__init__()
        self.cached_image = None

    def clear_cache(self):
        self.cached_image = None

    def draw_and_cache(self, x_length, y_length):
        self.cached_image = self.draw(x_length, y_length)
        return self.cached_image

    @abc.abstractmethod
    def get_gene(self):
        pass

    @abc.abstractmethod
    def draw(self, x_length, y_length):
        pass

    @abc.abstractmethod
    def copy(self):
        pass

    @abc.abstractmethod
    def set_from_gene(self, gene):
        pass

    def mutate(self, mutate_max_change_pct):
        """
        Mutate this shape
        :param mutate_max_change_pct: Max percentage of change for the selected gene
        """
        gene = self.get_gene()
        # Select a random gene to mutate
        random_gene_index = random.randint(0, len(gene) - 1)
        # Set a random percentage
        mutate_pct = random.randint(0 - mutate_max_change_pct, mutate_max_change_pct)
        # Mutate the gene by setting it between 0 and 100
        gene[random_gene_index] = min(max(gene[random_gene_index] + mutate_pct, 0), 100)
        self.set_from_gene(gene)
        # Clear cached image as it's not relevant any more
        self.clear_cache()
