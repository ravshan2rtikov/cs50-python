import re
import sys


def main():
    print(count(input("Text: ")))


def count(i):
    pattern = r"\bum\b"
    match = re.findall(pattern, i, flags=re.IGNORECASE)
    return len(match)


if __name__ == "__main__":
    main()
