import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file = sys.argv[1]

    if not file.endswith(".csv"):
        sys.exit("Not a csv file")

    try:
        with open(file, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = list(reader)
    except FileNotFoundError:
        sys.exit("File does not exists")

    if not rows:
        sys.exit()

    headers = rows[0]
    data = rows[1:]

    print(tabulate(data, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
