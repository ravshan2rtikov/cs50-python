def main():
    fraction = get_fraction()
    percentage = round(fraction * 100)

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


def get_fraction():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x, y = int(x), int(y)
            if y == 0 or x > y:
                raise ValueError("Invalid fraction")
            return x / y
        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
