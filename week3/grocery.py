grocery_list = {}

while True:
    try:
        item = input().upper()
        grocery_list[item] = grocery_list.get(item, 0) + 1
    except EOFError:
        print("\n")
        break

for item in sorted(grocery_list):
    print(f"{grocery_list[item]} {item}")
