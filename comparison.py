def compare(input_str):
    
    parts = input_str.split()

    if len(parts) != 3:
        return False  

    operand1 = int(parts[0])
    operator = parts[1]
    operand2 = int(parts[2])

    if operator == "<":
        return operand1 < operand2
    else operator == ">":
        return operand1 > operand2
