import argparse

from image_reconstruction.algo.image_reconstruction_algo import ImageReconstructionAlgo


def main():
    parser = argparse.ArgumentParser(prog='reconstruct')
    parser.add_argument('--image', dest='image', action='store', required=True)
    parser.add_argument('--shape', dest='shape', default='Circle', action='store')
    subparsers = parser.add_subparsers(help='sub-command help', dest="algo")
    genetic_algo_parser = subparsers.add_parser("GeneticAlgo", help="Using the Genetic Algorithm")
    genetic_algo_parser.add_argument('--max-generations', dest='max_generations', action='store', type=int, default=1000)
    genetic_algo_parser.add_argument('--mutate-ratio', dest='mutate_ratio', action='store', type=float, default=0.1)
    genetic_algo_parser.add_argument('--mutate-max-change-pct', dest='mutate_max_change_pct', action='store', type=int, default=100)
    genetic_algo_parser.add_argument('--population-size', dest='population_size', action='store', type=int, default=50)
    genetic_algo_parser.add_argument('--fitness-sampling-portion', dest='fitness_sampling_portion', action='store', type=float, default=0.1)
    genetic_algo_parser.add_argument('--selection-portion ', dest='selection_portion', action='store', type=float, default=0.2)
    genetic_algo_parser.add_argument('--number-of-shapes', dest='number_of_shapes', action='store', type=int, default=1000)
    genetic_algo_parser.add_argument('--stop-at', dest='stop_at', action='store', type=float, default=0.95)
    parameters = parser.parse_args()
    ImageReconstructionAlgo.run_algo(parameters.algo, parameters.image, shape=parameters.shape, parameters=parameters)

