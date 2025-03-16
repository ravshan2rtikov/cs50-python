def main():
    expr = input("Expression: ")
    x, y, z = expr.split(" ")
    x = float(x)
    z = float(z)
    answ = result(x, y, z)

    if answ is not None:
        print(answ)
    else:
        print("Please enter valid operator")


def result(x, y, z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z
    elif y == "**":
        return x ** z
    elif y == "//":
        return x // z
    elif y == "%":
        return x % z
    else:
        return None


main()
