def main():
    try:
        fraction = input("Fraction: ")
        percent = convert(fraction)
        print(gauge(percent))
    except (ValueError, ZeroDivisionError):
        pass


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError("Cannot divide by 0")
        if x > y:
            raise ValueError("Invalid fraction")

        return round((x / y) * 100)
    except (ValueError, ZeroDivisionError):
        raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
