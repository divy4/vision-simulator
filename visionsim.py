import argparse
import numpy

import util


def applyVision(visionMap, image, verbose=False):
    visionMap = numpy.flip(visionMap)
    shape = numpy.asarray([image.shape[0] - visionMap.shape[0], \
                           image.shape[1] - visionMap.shape[1], \
                           image.shape[2]],
                          dtype=int)
    applied = numpy.zeros(shape)
    for index, brightnessFactor in numpy.ndenumerate(visionMap):
        if not brightnessFactor == 0:
            imageSlice = util.getArraySliceAt(image, index, applied.shape[:-1])
            applied += brightnessFactor * imageSlice
        if verbose and index[1] + 1 == visionMap.shape[1]:
            percent = (index[0] * visionMap.shape[1] + index[1] + 1) \
                    * 100 / (visionMap.shape[0] * visionMap.shape[1])
            print('{:.2f}%'.format(percent))
    return applied


def main():
    parser = argparse.ArgumentParser(description='Vision Simulator')
    parser.add_argument(
        'pixel_map',
        type=str,
        help='An image of what a single white pixel looks like to you.')
    parser.add_argument(
        'images',
        nargs='+',
        help='Images to apply your vision to.')
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Run in verbose mode.')
    args = parser.parse_args()

    visionImg = util.readImage(args.pixel_map)
    visionMap = util.getBrightnessMap(visionImg)
    for path in args.images:
        image = util.readImage(path, convertToFloat=True)
        image = applyVision(visionMap, image, verbose=args.verbose)
        util.writeImage(path + '.vision.png', image)

if __name__ == '__main__':
    main()