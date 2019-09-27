import abc
import random


class GeneticImage(abc.ABC):
    def __init__(self, chromosome=None) -> None:
        """
        Base class and factory for all Genetic Images
        :param chromosome: a list of genetic shapes
        """
        if chromosome is not None:
            self.chromosome = chromosome
            self.genes_num = len(chromosome)
        # Cached fitness score - init to None
        self.fitness = None

    def breed_with(self, genetic_image):
        """
        Breed image with genetic image
        :param genetic_image:
        :return: return a child Image consisting with 50% genes of current image and 50% genes of genetic_image
        """
        child = [self.chromosome[i].copy() if bool(random.getrandbits(1)) else genetic_image.chromosome[i].copy()
                 for i in range(self.genes_num)]
        return self.from_chromosome(child)

    @abc.abstractstaticmethod
    def from_chromosome(chromosome):
        """
        Create a genetic image from a chromosome
        :param chromosome:
        """
        pass

    @abc.abstractmethod
    def draw(self, x_length, y_length):
        """
        Create a PIL Image of size x_length, y_length
        :param x_length:
        :param y_length:
        """
        pass

    @abc.abstractstaticmethod
    def generate_random_array(genes_num, array_size):
        """
        Generate a random array of images from a genes_num number of shapes
        :param genes_num: number of shapes per image
        :param array_size: number of images to return
        """
        pass

    @staticmethod
    def get_random_image_array(shape, genes_num, array_size):
        """
        Factory method to generate a specific image array
        :param shape:
        :param genes_num:
        :param array_size:
        :return:
        """
        if shape == 'Circle':
            from image_reconstruction.algo.genetic.images.genetic_circles_image import GeneticCirclesImage
            return GeneticCirclesImage.generate_random_array(genes_num, array_size)
        elif shape == "Triangle":
            from image_reconstruction.algo.genetic.images.genetic_triangles_image import GeneticTrianglesImage
            return GeneticTrianglesImage.generate_random_array(genes_num, array_size)
        else:
            ValueError(f'{shape} is not a recognized genetic image type')

    @staticmethod
    def get_image(shape, chromosome):
        """
        Factory method to create a specific image from a chromosome
        :param shape:
        :param chromosome:
        :return:
        """
        if shape == 'Circle':
            from image_reconstruction.algo.genetic.images.genetic_circles_image import GeneticCirclesImage
            return GeneticCirclesImage(chromosome)
        elif shape == "Triangle":
            from image_reconstruction.algo.genetic.images.genetic_triangles_image import GeneticTrianglesImage
            return GeneticTrianglesImage(chromosome)
        else:
            ValueError(f'{shape} is not a recognized genetic image type')

    def mutate(self, mutate_ratio, mutate_max_change_pct):
        """
        Mutate the image shapes by mutate_ratio and mutate_max_change_pct params
        :param mutate_ratio:
        :param mutate_max_change_pct:
        """
        for index in range(self.genes_num):
            if mutate_ratio * 10000 > random.randint(0, 10000):
                self.chromosome[index].mutate(mutate_max_change_pct)
