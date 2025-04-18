def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if len(plate) < 2 or len(plate) > 6:
        return False

    if not plate[:2].isalpha():
        return False

    number_seen = False
    for i in range(len(plate)):
        if plate[i].isdigit():
            if not number_seen:
                if plate[i] == "0":
                    return False
                number_seen = True
            else:
                if not plate[i - 1].isdigit():
                    return False
        elif number_seen:
            return False

    for char in plate:
        if not char.isalnum():
            return False

    return True


if __name__ == "__main__":
    main()
