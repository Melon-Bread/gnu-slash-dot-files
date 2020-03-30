#!/usr/bin/env python3
"""
Converts every HEIC image in a directory into a PNG image.
This script assumes you have `heif-convert` in your PATH
"""

__author__ = "Melon Bread"
__version__ = "1.0.0"
__license__ = "MIT"

import argparse
import os
import subprocess

def main(args):
    """ Main entry point of the app """
    working_directory = args.input

    for file in os.listdir(working_directory):
        if file.upper().endswith('.HEIC'):
            print(f'Converting {file}...')
            subprocess.Popen(['heif-convert', file, f'{file[:-4]}png']).wait()
        else:
            print(f"Skipping {file}...")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument('-i', '--input', metavar='STRING', required=True,
                        help='The directory containing the HEIC image files')

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
