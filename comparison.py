def compare(expression):
    parts = expression.split('>')

    if len(parts) != 2:
        return False

    try:
        left = int(parts[0])
        right = int(parts[1])
    except ValueError:
        return False

    return left > right
