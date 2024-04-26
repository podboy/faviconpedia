# coding:utf-8

import os

from PIL import Image
from xarg import cmds
from xarg import color

script_dir: str = os.path.dirname(os.path.abspath(__file__))
base_dir: str = os.path.dirname(script_dir)
ico_dir: str = os.path.join(base_dir, "archive", "ico")
png_dir: str = os.path.join(base_dir, "archive", "png")


if not os.path.exists(png_dir):
    os.makedirs(png_dir)


def ico_to_png(ico: str, png: str):
    cmds.stdout(f"save {color.green(ico)} to {color.yellow(png)}")
    with Image.open(ico) as img:
        img.save(png, format="PNG")


for file in os.listdir(ico_dir):
    if not file.endswith(".ico"):
        continue
    ico_path: str = os.path.join(ico_dir, file)
    png_path: str = os.path.join(png_dir, f"{os.path.splitext(file)[0]}.png")
    ico_to_png(ico_path, png_path)
