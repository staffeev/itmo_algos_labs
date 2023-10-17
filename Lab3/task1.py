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


def combsort(array): # алгоритм сортировки расчёской
    factor = 1.2743
    step = len(array)
    swaps = 1
    while step > 1 or swaps > 0:
        index = 0
        swaps = 0
        if step > 1:
            step = int(step // factor)
        while index + step < len(array):
            if array[index] > array[index + step]:
                array[index], array[index + step] = array[index + step], array[index]
                swaps += 1
            index += 1
    return array


if __name__ == "__main__":
    quicksort_time = []
    combsort_time = []
    for x in [100, 1_000, 10_000, 100_000]:
        array = [random.randint(0, 100) for _ in range(0, x)]
        quicksort_time.append(round((timeit.timeit(lambda: quicksort(array), number=1)), 5))
        combsort_time.append(round((timeit.timeit(lambda: combsort(array), number=1)), 5))
    print("Количество элементов: ", [100, 1_000, 10_000, 100_000])
    print(f"Метод быстрой сортирвоки, время выполнения: {quicksort_time:}")
    print(f"Метод сортировки расчёской, время выполнения: {combsort_time}")

