# Vision Simulator
Vision Simulator is a python script that can emulate your vision.

## Usage
Below is the arguments visionsim.py takes. (This info can be printed by executing `python visionsim.py --help` in your terminal.)
```
usage: visionsim.py [-h] [-n NORM_FACTOR] [-v] pixel_map images [images ...]

Vision Simulator

positional arguments:
  pixel_map             An image of what a single white pixel looks like to
                        you.
  images                Images to apply your vision to.

optional arguments:
  -h, --help            show this help message and exit
  -n NORM_FACTOR, --norm-factor NORM_FACTOR
                        The exponent factor used in normalizing pixel_map. You
                        may have to adjust this value for good results.
  -v, --verbose         Run in verbose mode.
```

## Requirements
Vision Simulator requires python 3 ass well as the following python modules:
- numpy
- imageio