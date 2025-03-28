price = 50
denom = [25, 10, 5]

while price > 0:
    try:
        paid = int(input("Insert coin: "))
        if paid in denom:
            price -= paid
        print(f"Amount Due: {max(price, 0)}") if price > 0 else print(
            f"Change Owed: {abs(price)}"
        )
    except ValueError:
        pass
