import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$"
    match = re.match(pattern, ip)
    if not match:
        return False

    for group in match.groups():
        num = int(group)
        if num < 0 or num > 255:
            return False

    return True


if __name__ == "__main__":
    main()
