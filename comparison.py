def compare(input_str):
    
    input_str = input_str.replace(" ", "")

    if len(input_str) != 3:
        return False  

    operand1 = float(input_str[0])
    operator = input_str[1]
    operand2 = float(input_str[2])

    if operator == "<":
        return operand1 < operand2
    elif operator == ">":
        return operand1 > operand2
    else:
        return False
