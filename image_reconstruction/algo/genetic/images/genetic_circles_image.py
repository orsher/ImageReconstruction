import random

from PIL import Image
from image_reconstruction.algo.genetic.images.color import Color
from image_reconstruction.algo.genetic.images.genetic_image import GeneticImage
from image_reconstruction.algo.genetic.images.shape.genetic_circle import GeneticCircle


def generate_circle(genetic_circle, x_length, y_length):
    """
    Generate a circle of the specified size, cache it and return it
    :param genetic_circle:
    :param x_length:
    :param y_length:
    :return:
    """
    return genetic_circle.draw_and_cache(x_length, y_length)


def generate_generic_circle_array(size):
    """
    Generate and return a random array of circles
    :param size:
    :return:
    """
    return [GeneticCircle(radius_percent=random.randint(0, 100),
                          center_x_percent=random.randint(0, 100),
                          center_y_percent=random.randint(0, 100),
                          color=Color(random.randint(0, 255),
                                      random.randint(0, 255),
                                      random.randint(0, 255),
                                      random.randint(0, 255)))
            for i in range(size)]


class GeneticCirclesImage(GeneticImage):

    def __init__(self, chromosome=None) -> None:
        super().__init__(chromosome=chromosome)

    @staticmethod
    def from_chromosome(chromosome):
        """
        Create a genetice circle image from a chromosome
        :param chromosome:
        :return:
        """
        return GeneticCirclesImage(chromosome)

    def draw(self, x_length, y_length):
        """
        Draw a PIL image of the triangle of the specified size
        :param x_length:
        :param y_length:
        :return:
        """
        # Set background
        img = Image.new('RGBA', (x_length, y_length), color=(0, 0, 0, 255))
        # Blend all shapes
        for genetic_circle in self.chromosome:
            circle = generate_circle(genetic_circle, x_length, y_length)
            img = Image.alpha_composite(img, circle)
        return img

    @staticmethod
    def generate_random_array(genes_num, array_size):
        """
        Generate a random array of genetic circles images
        :param genes_num: Number of distinct shapes
        :param array_size: Number of images
        :return:
        """
        seed_chromosome = generate_generic_circle_array(genes_num)
        return [GeneticCirclesImage(chromosome=seed_chromosome)
                for i in range(array_size)]
