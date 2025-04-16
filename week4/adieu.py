import inflect

p = inflect.engine()
bye_to = []

while True:
    try:
        name = input("Name: ")
        bye_to.append(name)
    except EOFError:
        break

farewell = p.join(bye_to)
print(f"Adieu, adieu, to {farewell}")
