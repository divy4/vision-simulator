import imageio
import numpy


def __removeAlpha(image):
    return image[:, :, :3]


def __intImgToFloat(image):
    image = image / 255.
    image = numpy.maximum(0., image)
    return numpy.minimum(1., image)


def __floatImgToInt(image):
    image *= 255
    image = numpy.maximum(0, image)
    image = numpy.minimum(255, image)
    return image.astype(int)


def getBrightnessMap(image):
    pass


def readImage(path, convertToFloat=False):
    image = imageio.imread(path)
    image = numpy.asarray(image, dtype=int)
    if not image.shape[-1] == 3:
        image = __removeAlpha(image)
    if convertToFloat:
        image = __intImgToFloat(image)
    return image


def writeImage(path, image):
    if image.dtype is not int:
        image = __floatImgToInt(image)
    imageio.imsave(path, image)
    