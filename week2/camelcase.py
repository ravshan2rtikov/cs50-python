def camel_to_snake(name):
    snake_case = ""

    for char in name:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char

    return snake_case.lstrip("_")  # Remove leading underscore if any


# Get user input
user_input = input("Enter a camelCase or PascalCase string: ")
snake_case_output = camel_to_snake(user_input)

print("Snake case:", snake_case_output)
