from PIL import Image, ImageDraw

from image_reconstruction.algo.genetic.images.color import Color
from image_reconstruction.algo.genetic.images.shape.genetic_shape import GeneticShape


class GeneticCircle(GeneticShape):
    def __init__(self, radius_percent=None, center_x_percent=None, center_y_percent=None, color=None, gene=None) -> None:
        """
        Create a genetic circle from a gene or a set of attributes
        :param radius_percent:
        :param center_x_percent:
        :param center_y_percent:
        :param color:
        :param gene:
        """
        super().__init__()
        if gene is None:
            self.radius_percent = radius_percent
            self.center_x_percent = center_x_percent
            self.center_y_percent = center_y_percent
            self.color = color
        else:
            self.set_from_gene(gene)

    def copy(self):
        """
        :return: A copy of the current circle
        """
        copied_circle = GeneticCircle(gene=self.get_gene())
        copied_circle.cached_image = self.cached_image
        return copied_circle

    def get_gene(self):
        """
        :return: An array of circle attributes called gene
        """
        return [self.radius_percent, self.center_x_percent, self.center_y_percent,
                self.color.r * 100 / 255, self.color.g * 100 / 255, self.color.b * 100 / 255,
                self.color.a * 100 / 255]

    def set_from_gene(self, gene):
        """
        Set the current circle from a gene
        :param gene:
        """
        self.radius_percent = gene[0]
        self.center_x_percent = gene[1]
        self.center_y_percent = gene[2]
        self.color = Color(r=int(gene[3] * 255 / 100),
                           g=int(gene[4] * 255 / 100),
                           b=int(gene[5] * 255 / 100),
                           a=int(gene[6] * 255 / 100))

    def draw(self, x_length, y_length):
        """
        Draw this Circle as a PIL image
        :param x_length:
        :param y_length:
        :return:
        """
        if self.cached_image is not None and self.cached_image.size[0] == x_length \
                and self.cached_image.size[1] == y_length:
            return self.cached_image
        else:
            img = Image.new('RGBA', (x_length, y_length), color=(0, 0, 0, 0))
            # Get a drawing handle
            draw = ImageDraw.Draw(img)
            r = int(self.radius_percent * max(x_length, y_length) / 100)
            x = x_length * self.center_x_percent / 100
            y = y_length * self.center_y_percent / 100
            self.draw_circle(draw, r, x, y)
        return img

    def draw_circle(self, draw, r, x, y):
        # Draw on image
        draw.ellipse(
            xy=(x - r, y - r, x + r, y + r),
            fill=(self.color.r, self.color.g, self.color.b, self.color.a))
