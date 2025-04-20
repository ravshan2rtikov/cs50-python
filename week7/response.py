import sys
from validators import email as is_email_valid


def main():
    emaddr = input("Email: ")

    if is_email_valid(emaddr):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
