#!/usr/bin/python3
# Px2ANSI: Pixel Art to ANSI Art conversions
# Author: Nell Fauveau
# https://github.com/Nellousan/px2ansi
#
# Copyright 2022 Nell Fauveau
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# version 2 as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

from PIL import Image
import numpy as np
import argparse


def pixels_to_ansi(px1: np.array, px2: np.array) -> str:
    res = ""
    if px1[3] != 255 or px2[3] != 255:
        res += "\033[0m"
    if px1[3] != 255 and px2[3] != 255:
        res += " "
    if px1[3] == 255:
        res += "\033[38;2;{};{};{}m".format(px1[0], px1[1], px1[2])
        if px2[3] == 255:
            res += "\033[48;2;{};{};{}m".format(px2[0], px2[1], px2[2])
        res += "▀"
    elif px2[3] == 255:
        res += "\033[38;2;{};{};{}m".format(px2[0], px2[1], px2[2])
        res += "▄"
    return res


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("-o", "--output")
    args = parser.parse_args()

    image = Image.open(args.filename)
    image = image.convert("RGBA")
    array = np.array(image)

    final_res = ""

    for i in range(int(array.shape[0] / 2)):
        for j in range(array.shape[1]):
            final_res += pixels_to_ansi(array[i * 2][j], array[i * 2 + 1][j])
        final_res += "\033[0m\n"

    if args.output is not None:
        with open(args.output, "w") as f:
            f.write(final_res)
    else:
        print(final_res)
