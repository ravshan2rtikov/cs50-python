def main():
    x = int(input("What is x: "))
    if is_even(x):
        print("X is even")
    else:
        print("X is odd")

def is_even(n):
    if n % 2 == 0:
        return True;
    else:
        return False;

main() 