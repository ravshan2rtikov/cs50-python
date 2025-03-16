def main():
    greeting = input("Greeting: ").strip().lower()
    if hello(greeting):
        print("$0")
    elif h(greeting):
        print("$20")
    else:
        print("$100")


def hello(greeting):
    hello = "hello"
    return True if hello in greeting else False


def h(greeting):
    h = "h"
    if greeting.startswith(h):
        return True
    else:
        return False


main()