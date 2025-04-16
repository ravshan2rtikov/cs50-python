import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        print("Please enter a valid positive number.")

number = random.randint(1, level)

guess = 0
while guess != number:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            print("Please enter a valid positive number.")
        elif guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
    except ValueError:
        print("Please enter a valid number.")
