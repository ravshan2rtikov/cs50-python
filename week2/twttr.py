full = input("Input: ")
vow = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for c in full:
    if c not in vow:
        print(c, end="")

print()
