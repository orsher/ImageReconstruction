from unittest import TestCase

from image_reconstruction.algo.genetic.images.color import Color
from image_reconstruction.algo.genetic.images.shape.genetic_triangle import to_absolute_point, GeneticTriangle


class TestGeneticTriangle(TestCase):
    def test_copy_and_get_gene(self):
        genetic_triangle = GeneticTriangle(point1_percent=(50, 50),
                                           point2_percent=(100, 100),
                                           point3_percent=(25, 24),
                                           color=Color(100, 50, 100, 40))
        genetic_triangle_copy = genetic_triangle.copy()
        for index in range(len(genetic_triangle_copy.get_gene())):
            assert genetic_triangle.get_gene()[index] == genetic_triangle_copy.get_gene()[index]

    def test_to_absolute_point(self):
        assert (100, 300) == to_absolute_point((50, 75), 200, 400)
