def compare(expression):

    parts = expression.split()

    if len(parts) != 3:
        raise ValueError("тесты у вас отличные!!!")

    left = int(parts[0])
    operator = parts[1]
    right = int(parts[2])

    if operator == ">":
        return left > right
    elif operator == "<":
        return left < right
    else:
        raise ValueError("тесты у вас отличные!!!")
