from PIL import Image, ImageDraw

from image_reconstruction.algo.genetic.images.color import Color
from image_reconstruction.algo.genetic.images.shape.genetic_shape import GeneticShape


class GeneticTriangle(GeneticShape):
    def __init__(self, point1_percent=None, point2_percent=None, point3_percent=None, color=None, gene=None) -> None:
        """
        Craetes a genetic triangle from a gene or a set of attributes
        :param point1_percent:
        :param point2_percent:
        :param point3_percent:
        :param color:
        :param gene:
        """
        super().__init__()
        if gene is None:
            self.point1_percent = point1_percent
            self.point2_percent = point2_percent
            self.point3_percent = point3_percent
            self.color = color
        else:
            self.set_from_gene(gene)

    def copy(self):
        """
        :return: A copy of the genetic triangle
        """
        copied_circle = GeneticTriangle(gene=self.get_gene())
        copied_circle.cached_image = self.cached_image
        return copied_circle

    def get_gene(self):
        """
        :return: This triangle gene - a list of values between 0-100
        """
        return [self.point1_percent[0], self.point1_percent[1],
                self.point2_percent[0], self.point2_percent[1],
                self.point3_percent[0], self.point3_percent[1],
                self.color.r * 100 / 255, self.color.g * 100 / 255, self.color.b * 100 / 255,
                self.color.a * 100 / 255]

    def set_from_gene(self, gene):
        """
        Init this triangle from a gene
        :param gene:
        """
        self.point1_percent = (gene[0], gene[1])
        self.point2_percent = (gene[2], gene[3])
        self.point3_percent = (gene[4], gene[5])
        self.color = Color(r=int(gene[6] * 255 / 100),
                           g=int(gene[7] * 255 / 100),
                           b=int(gene[8] * 255 / 100),
                           a=int(gene[9] * 255 / 100))

    def draw(self, x_length, y_length):
        """
        Draw the triangle as a PIL image
        :param x_length:
        :param y_length:
        :return: PIL image containing the triangle
        """
        if self.cached_image is not None and self.cached_image.size[0] == x_length \
                and self.cached_image.size[1] == y_length:
            return self.cached_image
        else:
            img = Image.new('RGBA', (x_length, y_length), color=(0, 0, 0, 0))
            # Get a drawing handle
            draw = ImageDraw.Draw(img)
            draw.polygon(xy=[to_absolute_point(self.point1_percent, x_length, y_length),
                         to_absolute_point(self.point2_percent, x_length, y_length),
                         to_absolute_point(self.point3_percent, x_length, y_length)],
                         fill=(self.color.r, self.color.g, self.color.b, self.color.a))
        return img


def to_absolute_point(point, x_length, y_length):
    """
    Converts a relative point with x and y values ranges between 0-100 to an absolute
    point with x,y values between x_length & y_length
    :param point:
    :param x_length:
    :param y_length:
    :return:
    """
    return point[0] * x_length / 100, point[1] * y_length / 100
