def is_psp(sequence:str):
    brackets_tuple = {')':'(', ']':'[','}':'{'}
    stack = []
    for i, bracket in enumerate(sequence):
        if bracket in list(brackets_tuple.values()):
            stack.append((i, bracket))
        elif bracket in list(brackets_tuple.keys()):
            if len(stack) == 0:
                return (f'скобочная последовательность неправильная, индекс первой неправильной скобки:{i}')
            else:
                last_index, last = stack.pop()
                if last != brackets_tuple[bracket]:
                    return (f'скобочная последовательность неправильная, индекс первой неправильной скобки:{last_index}')
    if len(stack) != 0:
        while len(stack) != 0:
            last_index, last = stack.pop()
        return (f'скобочная последовательность неправильная, индекс первой неправильной скобки:{last_index}')
    return "скобочная последовательность правильная"




if __name__ == "__main__":
    sequence = '{}(}}}{}'
    print(is_psp(sequence))