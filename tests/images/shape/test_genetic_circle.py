from unittest import TestCase

from image_reconstruction.algo.genetic.images.color import Color
from image_reconstruction.algo.genetic.images.shape.genetic_circle import GeneticCircle


class TestGeneticCircle(TestCase):
    def test_copy_and_get_gene(self):
        genetic_circle = GeneticCircle(radius_percent=100,
                                       center_x_percent=100,
                                       center_y_percent=50,
                                       color=Color(100, 100, 50, 30))
        genetic_circle_copy = genetic_circle.copy()
        for index in range(len(genetic_circle_copy.get_gene())):
            assert genetic_circle.get_gene()[index] == genetic_circle_copy.get_gene()[index]
