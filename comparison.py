def compare(expression):
    try:
        return eval(expression)
    except Exception as e:
        print(f"{e}")
        return False
