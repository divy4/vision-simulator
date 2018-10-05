import argparse

import util


def applyVision(visionMap, image):
    pass


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
    args = parser.parse_args()

    visionImg = util.readImage(args.pixel_map)
    visionMap = util.getBrightnessMap(visionImg)
    for path in args.images:
        image = util.readImage(path, convertToFloat=True)
        image = applyVision(visionMap, image)
        util.writeImage(path + '.vision.png', image)

if __name__ == '__main__':
    main()