import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file = sys.argv[1]

    if not file.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(file, "r") as f:
            count = 0
            for line in f:
                stripped = line.strip()

                if stripped == "":
                    continue

                if stripped.startswith("#"):
                    continue

                count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(count)


if __name__ == "__main__":
    main()
