def main():
    forty2 = input("What is the answer to The Great Question of Life, the Universe and Everything? ")
    forty2 = forty2.strip().lower()
    if answer(forty2):
        print("Yes")
    else:
        print("No")


def answer(forty2):
    answer = ["42", "forty two", "forty-two"]
    return True if forty2 in answer else False


main()
