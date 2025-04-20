import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")


def convert(i):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, i)
    if not match:
        raise ValueError

    def to24(hour, minute, period):
        h = int(hour)
        m = int(minute) if minute else 0

        if not (1 <= h <= 12) or not (0 <= m < 60):
            raise ValueError

        if period == "AM":
            h = 0 if h == 12 else h
        else:
            h = h if h == 12 else h + 12
        return f"{h:02}:{m:02}"

    h1, m1, p1, h2, m2, p2 = match.groups()
    start = to24(h1, m1, p1)
    end = to24(h2, m2, p2)
    return f"{start} to {end}"


if __name__ == "__main__":
    main()
