import random
import timeit


def quicksort(array):  # алгоритм быстрой сортировки
    if len(array) < 2:
        return array
    else:
        pivot = array[(0 + len(array) - 1) // 2]
        prev_nums, eq_nums, next_nums = [], [], []
        for numb in array:
            if numb < pivot:
                prev_nums.append(numb)
            elif numb == pivot:
                eq_nums.append(numb)
            else:
                next_nums.append(numb)
        return quicksort(prev_nums) + eq_nums + quicksort(next_nums)


def combsort(array):
    factor = 1.2743
    step = int(len(array) // factor)
    swaps = 1
    while step > 1 or swaps > 0:
        index = 0
        swaps = 0
        while index + step < len(array):
            if array[index] > array[index + step]:
                array[index], array[index + step] = array[index + step], array[index]
                swaps += 1
            index += 1
        if step > 1:
            step = int(step // factor)
    return array


if __name__ == "__main__":
    array = [random.randint(0, 1000) for _ in range(0, 1_000)]
    print(f"Исходный массив: {array[:20]}...")
    print()
    print(f"Метод быстрой сортирвоки: {quicksort(array)[:20]}, время выполнения: {((timeit.timeit(lambda: quicksort(array), number=100)) / 100):.5f}")
    print()
    print(f"Метод сортировки расчёской: {combsort(array)[:20]}, время выполнения: {((timeit.timeit(lambda: combsort(array), number=100)) / 100):.5f}")
