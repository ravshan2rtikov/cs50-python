def main():
    greet = input("Greeting: ")
    print(f"${value(greet)}")


def value(g):
    g = g.lower()
    if g.startswith("hello"):
        return 0
    elif g.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
