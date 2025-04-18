def main():
    full = input("Input: ")
    print("Output: ", shorten(full))


def shorten(word):
    vow = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    return "".join(c for c in word if c not in vow)


if __name__ == "__main__":
    main()
