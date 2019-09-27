import abc

from PIL import Image


class ImageReconstructionAlgo(abc.ABC):

    def __init__(self, target_image, shape="Circle", parameters={}) -> None:
        """
        Base class and factory for all image reconstruction algorithms
        :param target_image: Target image path
        :param shape: Shape to use for construction
        :param parameters: list of algorithm specific parameters
        """
        super().__init__()
        self.target_image = target_image
        self.x_length, self.y_length = target_image.size
        self.shape = shape

    @staticmethod
    def run_algo(algo, target_image_path, shape="Circle", parameters={}):
        """
        Run the requested algo with the requested parameters
        :param algo:
        :param target_image_path:
        :param shape:
        :param parameters:
        """
        target_image = Image.open(target_image_path).convert('RGBA')
        if algo == "GeneticAlgo":
            from image_reconstruction.algo.genetic.genetic_algo import GeneticAlgo
            GeneticAlgo(target_image, shape, parameters).run()

    @abc.abstractmethod
    def run(self):
        pass
