import time

import matplotlib

matplotlib.use('TkAgg')
from matplotlib import pyplot


def timeit(method):
    """
    A function decorator for timing and loggin a function execution time
    :param method:
    :return:
    """
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result

    return timed


class Viewer:
    f = pyplot.figure()
    graph1 = f.add_subplot(421)
    graph2 = f.add_subplot(422)
    graph3 = f.add_subplot(423)
    graph4 = f.add_subplot(424)
    pyplot.ion()
    pyplot.subplots_adjust(wspace=1, hspace=1)

    @staticmethod
    @timeit
    def show_image(image1, title1=None,
                   image2=None, title2=None,
                   image3=None, title3=None,
                   image4=None, title4=None):
        """
        Display up to 4 images and 4 titles on pyplot figure
        """
        if image1 is not None:
            Viewer.set_image_on(Viewer.graph1, image1, title1)
        if image2 is not None:
            Viewer.set_image_on(Viewer.graph2, image2, title2)
        if image3 is not None:
            Viewer.set_image_on(Viewer.graph3, image3, title3)
        if image4 is not None:
            Viewer.set_image_on(Viewer.graph4, image4, title4)

        Viewer.f.show()
        pyplot.pause(.001)

    @staticmethod
    def set_image_on(graph, image, title):
        graph.imshow(image)
        graph.set_title(title)

