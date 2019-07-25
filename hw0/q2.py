from PIL import Image
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("source_img")

args = parser.parse_args()
im = Image.open(args.source_img)
im.rotate(180).save("ans2.png")
