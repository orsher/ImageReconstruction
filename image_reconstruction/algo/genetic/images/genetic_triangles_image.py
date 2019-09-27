import random

from PIL import Image
from image_reconstruction.algo.genetic.images.color import Color
from image_reconstruction.algo.genetic.images.genetic_image import GeneticImage
from image_reconstruction.algo.genetic.images.shape.genetic_triangle import GeneticTriangle


def generate_triangle(genetic_triangle, x_length, y_length):
    """
    Generating a triangle of a specified size cache and return it
    :param genetic_triangle:
    :param x_length:
    :param y_length:
    :return:
    """
    return genetic_triangle.draw_and_cache(x_length, y_length)


def generate_genetic_triangle_array(size):
    """
    Generate and return an array of size number of random triangles
    :param size:
    :return:
    """
    return [GeneticTriangle(point1_percent=(random.randint(0, 100), random.randint(0, 100)),
                            point2_percent=(random.randint(0, 100), random.randint(0, 100)),
                            point3_percent=(random.randint(0, 100), random.randint(0, 100)),
                            color=Color(random.randint(0, 255),
                                        random.randint(0, 255),
                                        random.randint(0, 255),
                                        random.randint(0, 255)))
            for i in range(size)]


class GeneticTrianglesImage(GeneticImage):

    def __init__(self, chromosome=None) -> None:
        super().__init__(chromosome=chromosome)

    @staticmethod
    def from_chromosome(chromosome):
        """
        Create triangle from chromosome
        :param chromosome:
        :return:
        """
        return GeneticTrianglesImage(chromosome)

    def draw(self, x_length, y_length):
        """
        Draw a PIL Image of the triangle of the specified size
        :param x_length:
        :param y_length:
        :return:
        """
        # Set background
        img = Image.new('RGBA', (x_length, y_length), color=(0, 0, 0, 255))
        # Blend all triangles by array order
        for genetic_triangle in self.chromosome:
            triangle = generate_triangle(genetic_triangle, x_length, y_length)
            img = Image.alpha_composite(img, triangle)
        return img

    @staticmethod
    def generate_random_array(genes_num, array_size):
        """
        Generate a random triangles images array of size array_size
        :param genes_num: Number of unique shapes
        :param array_size: Number of images in array
        :return:
        """
        seed_chromosome = generate_genetic_triangle_array(genes_num)
        return [GeneticTrianglesImage(chromosome=seed_chromosome)
                for i in range(array_size)]
