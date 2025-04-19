import sys
import os
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    in_path = sys.argv[1]
    out_path = sys.argv[2]

    vexts = {".jpg", ".jpeg", ".png"}
    inroot, inext = os.path.splitext(in_path)
    outroot, outext = os.path.splitext(out_path)

    inext = inext.lower()
    outext = outext.lower()

    if inext not in vexts:
        sys.exit("Invalid input")
    if outext not in vexts:
        sys.exit("Invalid output")
    if inext != outext:
        sys.exit("Input and output have different extensions")

    if not os.path.isfile(in_path):
        sys.exit("Input does not exist")

    try:
        photo = Image.open(in_path)
        shirt = Image.open("shirt.png")

        photo = ImageOps.fit(photo, shirt.size)

        photo.paste(shirt, (0, 0), shirt)

        photo.save(out_path)
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
