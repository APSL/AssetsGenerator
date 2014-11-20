#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import os
import sys
import json
import argparse
from PIL import Image


def main():
    sizes = [29, 40, 50, 57, 58, 72, 76, 80, 87, 100, 114, 120, 144, 152, 180]
    image_name = "icon.png"
    contents = {
        "info": {
            "version": 1,
            "author": "apsl"
        }
    }

    if os.path.isfile(image_name) is False:
        sys.exit("Missing icon.png file in current directory")

    img = Image.open(image_name)

    # Create Assets folder
    current_dir = os.getcwd()
    asset_dir = "{0}/Assets.appiconset".format(current_dir)
    if not os.path.exists(asset_dir):
        os.makedirs(asset_dir)
    os.chdir(asset_dir)
    print asset_dir

    # Generate images
    images = []
    for size in sizes:
        i = img.resize((size, size), Image.ANTIALIAS)
        img_filename = "icon{0}.png".format(size)
        i.save(img_filename, format="PNG")
        if size == 29:
            asset_entry = {
                "size": "29x29",
                "idiom": "iphone",
                "scale": "1x",
                "filename": img_filename
            }
            images.append(asset_entry)
            asset_entry = {
                "size": "29x29",
                "idiom": "ipad",
                "scale": "1x",
                "filename": img_filename
            }
            images.append(asset_entry)
        elif size == 40:
            asset_entry = {
                "size": "40x40",
                "idiom": "ipad",
                "scale": "1x",
                "filename": img_filename
            }
            images.append(asset_entry)
        elif size == 50:
            asset_entry = {
                "size": "50x50",
                "idiom": "ipad",
                "scale": "1x",
                "filename": img_filename
            }
            images.append(asset_entry)
        elif size == 57:
            asset_entry = {
                "size": "57x57",
                "idiom": "iphone",
                "scale": "1x",
                "filename": img_filename
            }
            images.append(asset_entry)
        elif size == 58:
            asset_entry = {
                "size": "29x29",
                "idiom": "iphone",
                "scale": "2x",
                "filename": img_filename
            }
            images.append(asset_entry)
            asset_entry = {
                "size": "29x29",
                "idiom": "ipad",
                "scale": "2x",
                "filename": img_filename
            }
            images.append(asset_entry)
        elif size == 72:
            asset_entry = {
                "size": "72x72",
                "idiom": "ipad",
                "scale": "1x",
                "filename": img_filename
            }
            images.append(asset_entry)
        elif size == 76:
            asset_entry = {
                "size": "76x76",
                "idiom": "ipad",
                "scale": "1x",
                "filename": img_filename
            }
            images.append(asset_entry)
        elif size == 80:
            asset_entry = {
                "size": "40x40",
                "idiom": "iphone",
                "scale": "2x",
                "filename": img_filename
            }
            images.append(asset_entry)
            asset_entry = {
                "size": "40x40",
                "idiom": "ipad",
                "scale": "2x",
                "filename": img_filename
            }
            images.append(asset_entry)
        elif size == 87:
            asset_entry = {
                "size": "29x29",
                "idiom": "iphone",
                "scale": "3x",
                "filename": img_filename
            }
            images.append(asset_entry)
        elif size == 100:
            asset_entry = {
                "size": "50x50",
                "idiom": "ipad",
                "scale": "2x",
                "filename": img_filename
            }
            images.append(asset_entry)
        elif size == 114:
            asset_entry = {
                "size": "57x57",
                "idiom": "iphone",
                "scale": "2x",
                "filename": img_filename
            }
            images.append(asset_entry)
        elif size == 120:
            asset_entry = {
                "size": "40x40",
                "idiom": "iphone",
                "scale": "3x",
                "filename": img_filename
            }
            images.append(asset_entry)
            asset_entry = {
                "size": "120x120",
                "idiom": "car",
                "scale": "1x",
                "filename": img_filename
            }
            images.append(asset_entry)
        elif size == 144:
            asset_entry = {
                "size": "72x72",
                "idiom": "ipad",
                "scale": "2x",
                "filename": img_filename
            }
            images.append(asset_entry)
        elif size == 152:
            asset_entry = {
                "size": "76x76",
                "idiom": "ipad",
                "scale": "2x",
                "filename": img_filename
            }
            images.append(asset_entry)
        elif size == 180:
            asset_entry = {
                "size": "60x60",
                "idiom": "iphone",
                "scale": "3x",
                "filename": img_filename
            }
            images.append(asset_entry)

    contents["images"] = images
    file = open("Contents.json", "w")
    file.write(json.dumps(contents))
    file.close()


if __name__ == '__main__':
    main()
