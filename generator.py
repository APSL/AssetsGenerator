#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import os
import sys
import json
import argparse
from PIL import Image


def generate_icon_images(icon_filename):
    sizes = [29, 40, 50, 57, 58, 72, 76, 80, 87, 100, 114, 120, 144, 152, 180]
    image_name = icon_filename
    contents = {
        "info": {
            "version": 1,
            "author": "apsl"
        }
    }

    if os.path.isfile(image_name) is False:
        sys.exit("Missing {0} file".format(image_name))

    img = Image.open(image_name)

    # Check image size
    if img.size < (1024, 1024):
        sys.exit("{0} size is {1}. Must be 1024x1024 or higher.".format(image_name, img.size))

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
        img_filename = "Icon{0}.png".format(size)
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
                "size": "60x60",
                "idiom": "iphone",
                "scale": "2x",
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


def generate_launch_image(image_name):
    # 1334x750 not available yet, see: http://stackoverflow.com/a/26275887/1034126
    sizes = [(1242, 2208), (2208, 1242), (750, 1334), (640, 1136), (640, 960)]
    contents = {
        "info": {
            "version": 1,
            "author": "apsl"
        }
    }

    if os.path.isfile(image_name) is False:
        sys.exit("Missing {0} file".format(image_name))

    img = Image.open(image_name)

    # Check image size
    if img.size < (1242, 2208):
        sys.exit("{0} size is {1}. Must be 1242x2208 or higher.".format(image_name, img.size))

    # Create Assets folder
    current_dir = os.getcwd()
    asset_dir = "{0}/LaunchImage.launchimage".format(current_dir)
    if not os.path.exists(asset_dir):
        os.makedirs(asset_dir)
    os.chdir(asset_dir)
    print asset_dir

    # Generate images
    images = []
    for size in sizes:
        i = img.resize(size, Image.ANTIALIAS)
        img_filename = "launchimage{0}x{1}.png".format(size[0], size[1])
        i.save(img_filename, format="PNG")
        if size == (1242, 2208):
            asset_entry = {
                "extent": "full-screen",
                "idiom": "iphone",
                "subtype": "736h",
                "minimum-system-version": "8.0",
                "orientation": "portrait",
                "scale": "3x",
                "filename": img_filename
            }
        elif size == (2208, 1242):
            asset_entry = {
                "orientation": "landscape",
                "idiom": "iphone",
                "extent": "full-screen",
                "minimum-system-version": "8.0",
                "subtype": "736h",
                "scale": "3x",
                "filename": img_filename
            }
        elif size == (750, 1334):
            asset_entry = {
                "extent": "full-screen",
                "idiom": "iphone",
                "subtype": "667h",
                "minimum-system-version": "8.0",
                "orientation": "portrait",
                "scale": "2x",
                "filename": img_filename
            }
        elif size == (640, 1136):
            asset_entry = {
                "orientation": "portrait",
                "idiom": "iphone",
                "extent": "full-screen",
                "minimum-system-version": "7.0",
                "subtype": "retina4",
                "scale": "2x",
                "filename": img_filename
            }
            images.append(asset_entry)
            asset_entry = {
                "orientation": "portrait",
                "idiom": "iphone",
                "extent": "full-screen",
                "subtype": "retina4",
                "scale": "2x",
                "filename": img_filename
            }
        elif size == (640, 960):
            asset_entry = {
                "orientation": "portrait",
                "idiom": "iphone",
                "extent": "full-screen",
                "minimum-system-version": "7.0",
                "scale": "2x",
                "filename": img_filename
            }
            images.append(asset_entry)
            asset_entry = {
                "orientation": "portrait",
                "idiom": "iphone",
                "extent": "full-screen",
                "scale": "2x",
                "filename": img_filename
            }
        images.append(asset_entry)

    contents["images"] = images
    file = open("Contents.json", "w")
    file.write(json.dumps(contents))
    file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Assets generator for iOS projects")
    parser.add_argument("--launchimage",
                        help="Generate launch image assets")
    parser.add_argument("--icon",
                        help="Generate icons assets")
    parser.parse_args()
    args = parser.parse_args()
    if args.launchimage:
        print "Generating launch image with image {0}".format(args.launchimage)
        generate_launch_image(args.launchimage)
    if args.icon:
        print "Generating icons with image {0}".format(args.icon)
        generate_icon_images(args.icon)
