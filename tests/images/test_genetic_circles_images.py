from unittest import TestCase

from image_reconstruction.algo.genetic.images.color import Color
from image_reconstruction.algo.genetic.images.genetic_triangles_image import GeneticTrianglesImage
from image_reconstruction.algo.genetic.images.shape.genetic_triangle import GeneticTriangle


class TestGeneticImage(TestCase):
    def test_from_chromosome(self):
        genetic_triangle = GeneticTriangle(point1_percent=(50, 50),
                                           point2_percent=(100, 100),
                                           point3_percent=(25, 24),
                                           color=Color(100, 50, 100, 40))
        chromosome = [genetic_triangle]
        image = GeneticTrianglesImage(chromosome)
        assert image.chromosome == chromosome
