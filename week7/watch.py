import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([^\"]+)"'
    match = re.search(pattern, s)

    if match:
        video = match.group(1)
        return f"https://youtu.be/{video}"

    return None


if __name__ == "__main__":
    main()
