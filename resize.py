#!/usr/bin/env python3

import shutil
from PIL import Image
import os
import sys


def resize():
    src = "./images/"
    target = "./images/small/"

    shutil.rmtree(target)
    os.mkdir(target)

    dirs = os.listdir(src)
    for item in dirs:
        if os.path.isfile(src+item):
            filename, extension = os.path.splitext(item)
            if extension == ".png":
                print("Resize {}".format(item))
                im = Image.open(src+item)
                im.thumbnail((200, 200), Image.ANTIALIAS)
                im.save(target + filename + extension, "PNG", quality=90)
            else:
                print("Skip {}".format(item))
        else:
            print("Skip {}".format(item))


if __name__ == "__main__":
    resize()
