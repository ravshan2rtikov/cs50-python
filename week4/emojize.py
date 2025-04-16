import emoji


def main():
    text = input("Input: ")
    em_text = emoji.emojize(text, language="alias")
    print("Output: ", em_text)


if __name__ == "__main__":
    main()
