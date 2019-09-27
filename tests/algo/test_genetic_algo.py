from argparse import Namespace
from unittest import TestCase
import numpy as np
from PIL import Image

from image_reconstruction.algo.genetic.genetic_algo import GeneticAlgo, calc_arrays_diff


class TestGeneticAlgo(TestCase):

    def init_tests(self):
        import warnings
        warnings.simplefilter("ignore", ResourceWarning)
        params = Namespace()
        params.mutate_ratio=0.1
        params.mutate_max_change_pct = 100
        params.population_size = 50
        params.fitness_sampling_portion = 0.5
        params.selection_portion = 0.2
        params.max_generations = 100
        params.number_of_shapes = 100
        params.stop_at = 0.95

        self.algo = GeneticAlgo(target_image=Image.new('RGBA', (100, 100), color=(0, 0, 0, 255)).convert('RGBA'), parameters=params)

    def test_initialization(self):
        self.init_tests()
        self.algo.initialization()
        assert len(self.algo.population) ==  self.algo.population_size

    def test_calc_arrays_diff(self):
        arr1 = np.array([[[50, 100, 100], [0, 0, 0]]])
        arr2 = np.array([[[100, 50, 100], [255, 255, 255]]])
        self.init_tests()
        diff = calc_arrays_diff(arr1, arr2)
        print(diff)
        assert diff == 50 + 50 + 0 + 255 + 255 + 255


