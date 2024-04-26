# coding:utf-8

import os

from PIL import Image
from xarg import cmds
from xarg import color

script_dir: str = os.path.dirname(os.path.abspath(__file__))
base_dir: str = os.path.dirname(script_dir)
png_dir: str = os.path.join(base_dir, "archive", "png")


def resize_image_height(img: Image.Image, file: str, height: int):
    dir: str = os.path.join(png_dir, f"height-{height}")
    if not os.path.exists(dir):
        os.makedirs(dir)
    dst: str = os.path.join(dir, file)
    # get original image width and height
    original_width, original_height = img.size
    # calculate new width and height
    width = round(original_width * (height / original_height))
    resized_img = img.resize((width, height), resample=Image.LANCZOS)
    # save the resized image to destination
    resized_img.save(dst, format="PNG")


def resize_png_image(file: str):
    src: str = os.path.join(png_dir, file)
    cmds.stdout(f"resize {color.green(src)}")
    with Image.open(src) as img:
        resize_image_height(img, file, 64)
        resize_image_height(img, file, 32)
        resize_image_height(img, file, 25)
        resize_image_height(img, file, 20)
        resize_image_height(img, file, 16)


for file in os.listdir(png_dir):
    if not file.endswith(".png"):
        continue
    resize_png_image(file)
