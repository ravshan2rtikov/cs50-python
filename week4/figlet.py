import sys
import random
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    font = None
    font = parse_args(figlet, font)
    render_text(figlet, font)


def parse_args(figlet, font):
    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
    elif (
        len(sys.argv) == 3
        and sys.argv[1] in ["-f", "--font"]
        and sys.argv[2] in figlet.getFonts()
    ):
        font = sys.argv[2]
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")
    return font


def render_text(figlet, font):
    figlet.setFont(font=font)
    text = input("Input: ")
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
