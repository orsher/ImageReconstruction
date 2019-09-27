import itertools
import random

import math
from argparse import Namespace

import numpy as np
from PIL import Image

from image_reconstruction.algo.genetic.images.genetic_image import GeneticImage
from image_reconstruction.algo.image_reconstruction_algo import ImageReconstructionAlgo
from image_reconstruction.utils.utils import timeit, Viewer


class GeneticAlgo(ImageReconstructionAlgo):

    def __init__(self, target_image, shape="Circle", parameters=Namespace()) -> None:
        """
        Creating a GeneticAlgo object for image reconstruction
        :param target_image: target_image PIL Image object
        :param shape: GeneticShape type
        :param parameters: Algorithms tuning parameters
        """
        super().__init__(target_image, shape)
        self.mutate_ratio = parameters.mutate_ratio
        self.mutate_max_change_pct = parameters.mutate_max_change_pct
        self.population_size = parameters.population_size
        self.fitness_sampling_portion = parameters.fitness_sampling_portion
        self.x_length_small = int(self.x_length * self.fitness_sampling_portion)
        self.y_length_small = int(self.y_length * self.fitness_sampling_portion)
        self.background_color = (255, 255, 255, 255)
        self.target_small_image = prepare_image(target_image, self.x_length_small, self.y_length_small,
                                                self.background_color)
        self.population = []
        self.selection_portion = parameters.selection_portion
        self.max_generations = parameters.max_generations
        self.genes_num = parameters.number_of_shapes
        self.stop_at = parameters.stop_at

    def initialization(self):
        """
            Create an initial population of size population_size using genes_num number of shapes
        """
        self.population = GeneticImage.get_random_image_array(self.shape, genes_num=self.genes_num,
                                                              array_size=self.population_size)

    @timeit
    def run(self):
        """
            Start running to algorithm implementation
            Stop when max fitness is above stop_at parameter or we passed max_generations parameter
        """
        self.initialization()

        for x in range(self.max_generations):
            self.run_iteration(x)
            if self.population[0].fitness > self.stop_at:
                break
        self.selection()
        self.refresh_images()
        input("Press Enter to continue...")


    def refresh_images(self):
        """
            Show te current best fitted image in comparison to the original one
        """
        Viewer.show_image(image1=self.population[0].draw(self.x_length_small, self.y_length_small),
                          title1=f'Sampled Resolution - fitness {self.population[0].fitness}',
                          image2=self.population[0].draw(self.x_length, self.y_length),
                          title2=f'Full Resolution',
                          image3=self.target_small_image, title3="Sampled Resolution - Original",
                          image4=self.target_image, title4="Full Resolution - Original",
                          )

    @timeit
    def run_iteration(self, iteration_number):
        """
        Run a whole iteration. selection, breed, mutate and refreshed the images once in a while
        :param iteration_number: current iteration
        """
        print(f"Iteration {iteration_number}")
        self.selection()
        self.breed_all()
        if iteration_number % 50 == 0:
            self.refresh_images()

    def fitness(self, genetic_object):
        """
        Test the genetic_object fitness compared to the target_image
        :param genetic_object: a genetic image
        :return: fitness score between the genetic_object and the small resolution target image
        """
        if genetic_object.fitness is None:
            target_array = np.array(self.target_small_image)
            object_array = np.array(genetic_object.draw(self.x_length_small, self.y_length_small))
            total_diff = calc_arrays_diff(object_array, target_array)
            max_diff = self.x_length_small * self.y_length_small * 255 * 4
            # Calculate the fitness as percentage from max difference
            genetic_object.fitness = (max_diff - total_diff) / max_diff

        return genetic_object.fitness

    def selection(self):
        """
        Set the population to the selected best fitted population
        """
        selected_size = math.ceil(self.selection_portion * len(self.population))
        sorted_population = sorted(self.population, key=self.fitness, reverse=True)
        self.population = sorted_population[0:selected_size]

    def breed_all(self):
        """
        Choose random couples, breed them, mutate their children and add all children to current population
        """
        self.population = self.population + [self.breed_and_mutate(chromosome1, chromosome2)
                                             for (chromosome1, chromosome2) in
                                             random.sample(list(itertools.combinations(self.population, 2)),
                                                           int(self.population_size - len(self.population)))]

    def breed_and_mutate(self, chromosome1, chromosome2):
        """
        Create a child chromosome from both chromosomes and mutate it
        :param chromosome1:
        :param chromosome2:
        :return: the mutated child chromosome
        """
        child_chromosome = chromosome1.breed_with(chromosome2)
        child_chromosome.mutate(self.mutate_ratio, self.mutate_max_change_pct)
        return child_chromosome


def calc_arrays_diff(object_array, target_array):
    """
    Calculate the diff between all pixels RGB values from the object and target array
    :param object_array:
    :param target_array:
    :return: absolute summed diff
    """
    return abs(object_array.astype('int') - target_array.astype('int')).sum()


def prepare_image(image, x_length, y_length, background_color):
    """
    Prepare the image for processing.
    Resize it for a smaller resolution and apply it on a standard background
    :param image: PIL Image
    :param x_length: small resolution x length
    :param y_length: small resolution y length
    :param background_color:
    :return: Prepared PIL image
    """
    resized_image = image.resize((x_length, y_length))
    img = Image.new('RGBA', (x_length, y_length), color=background_color)
    return Image.alpha_composite(img, resized_image)
