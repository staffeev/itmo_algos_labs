def binary_search(arr, number):
    arr, number = sorted(arr), float(number)
    steps = 0
    low, high  = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        steps += 1
        if arr[mid] == number:
            return steps
        elif arr[mid] < number:
            low = mid + 1
        else:
            high = mid - 1
    return "введённого числа нет в заданном списке"

if __name__ == '__main__':
    arr = list(map(float, input('введите список: ').split()))
    number = input('введите число: ')
    print(binary_search(arr, number))
