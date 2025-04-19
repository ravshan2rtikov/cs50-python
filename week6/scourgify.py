import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    if not in_file.lower().endswith(".csv") or not out_file.lower().endswith(".csv"):
        sys.exit("Both input and output files must be CSV")

    try:
        with (
            open(in_file, newline="", encoding="utf-8") as inf,
            open(out_file, "w", newline="", encoding="utf-8") as outf,
        ):
            reader = csv.DictReader(inf)
            fields = ["first", "last", "house"]
            writer = csv.DictWriter(outf, fieldnames=fields)
            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({"first": first, "last": last, "house": row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read{in_file}")


if __name__ == "__main__":
    main()
