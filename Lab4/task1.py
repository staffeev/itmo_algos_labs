import random
from queue import LifoQueue
def create_sequence(length):
    sample_string = '(){}[]'
    result = ''.join((random.choice(sample_string)) for x in range(length))
    return result


def is_psp(sequence:str):
    brackets_tuple = {')':'(', ']':'[','}':'{'}
    stack = LifoQueue()
    for i, bracket in enumerate(sequence):
        if bracket in list(brackets_tuple.values()):
            stack.put([i, bracket])
        elif bracket in list(brackets_tuple.keys()):
            if not stack.qsize():
                return (f'скобочная последовательность неправильная, индекс первой неправильной скобки:{i}')
            else:
                last_index, last = stack.get()
                if last != brackets_tuple[bracket]:
                    return (f'скобочная последовательность неправильная, индекс первой неправильной скобки:{last_index}')
    if stack.qsize():
        while stack.qsize():
            last_index, last = stack.get()
        return (f'скобочная последовательность неправильная, индекс первой неправильной скобки:{last_index}')
    return "скобочная последовательность правильная"




if __name__ == "__main__":
    length = int(input('введите длину скобочной последовательности: '))
    sequence = create_sequence(length)
    print(sequence, is_psp(sequence), sep='\n')