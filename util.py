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
    return image.astype(numpy.uint8)


def getArraySliceAt(array, start, shape):
    end = numpy.asarray(start) + numpy.asarray(shape)
    return array[start[0]:end[0], start[1]:end[1]]


def getBrightnessMap(image, factor=1.7):
    shape = image.shape # black & white
    if len(image.shape) == 3: # RGB
        shape = shape[:-1]
    brightness = numpy.zeros(shape)
    for index in numpy.ndindex(shape):
        brightness[index] = numpy.average(image[index])
    brightness = brightness ** factor
    return brightness / numpy.sum(brightness)


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
    