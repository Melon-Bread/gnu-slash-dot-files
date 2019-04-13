#!/usr/bin/env python3
"""
Converts .lopus to .ogg via vgmstream & ffmpeg
"""

__author__ = "Melon Bread"
__version__ = "0.5.0"
__license__ = "MIT"

import argparse
import os
import subprocess


def main(args):
    file = args.input[:-6]

    try:
        print("Converting .lpous to .wav via vgmstream-cli...")
        subprocess.Popen(['vgmstream-cli', '-o',
                          '{}.wav'.format(file), args.input]).wait()
        pass
    except Exception as e:
        print("ERROR: Please make sure 'vgmstream-cli' is in the PATH!")
        raise

    try:
        print("Converting .wav to .ogg via ffmpeg...")
        subprocess.Popen(['ffmpeg', '-i', '{}.wav'.format(file), '-acodec',
                          'libvorbis', '{}.ogg'.format(file)]).wait()
        pass
    except Exception as e:
        print("ERROR: Please make sure 'ffmpeg' is in the PATH!")
        raise

    print("Removing .wav file...")
    os.remove("{}.wav".format(file))


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', metavar='STRING', required=True,
                        help='.lopus file your want to convert to .ogg')

    args = parser.parse_args()
    main(args)
