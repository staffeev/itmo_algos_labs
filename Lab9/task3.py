import random as rnd
import timeit

def merge_sort(a: list[float], left, right):
    """Сортировка слиянием"""
    if left >= right or len(a) < 2:
        return
    mid = (left + right) // 2
    merge_sort(a, left, mid)
    merge_sort(a, mid + 1, right)
    merge(a, left, right, mid)


def merge(a: list[float], start: int, end: int, mid: int):
    """Слияние двух частей массива на очередном вызове рекурсии"""
    p1, p2 = 0, 0
    ix = start
    left_half, right_half = a[start:mid+1], a[mid+1:end+1]

    while p1 < len(left_half) and p2 < len(right_half):
        if left_half[p1] > right_half[p2]:
            a[ix] = right_half[p2]
            p2 += 1
        else:
            a[ix] = left_half[p1]
            p1 += 1
        ix += 1
    
    while p1 < len(left_half):
        a[ix] = left_half[p1]
        ix += 1
        p1 += 1
    
    while p2 < len(right_half):
        a[ix] = right_half[p2]
        ix += 1
        p2 += 1


def insertion_sort(a, left, right):
    """Сортировка вставками"""
    for step in range(left, right):
        key = a[step]
        j = step - 1   
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key


def hybrid_sort(in_data, threshold=40):
    n = len(in_data)
    if n < threshold:
        insertion_sort(in_data, 0, n)
    for start in range(0, n, threshold):
        end = min(start + threshold - 1, n - 1)
        insertion_sort(in_data, start, end + 1)
    
    curr_size = threshold
    while curr_size < n:
        for start in range(0, n, curr_size * 2):
            mid = min(n - 1, start + curr_size - 1)
            end = min(n - 1, mid + curr_size)
            merge(in_data, start, end, mid)
        curr_size *= 2
    return in_data


def quicksort(array):
    """Быстрая сортировка"""
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


def make_heap(a: list[float], key, ix):
    """Рекурсивное создание кучи"""
    left_child = 2 * ix + 1
    right_child = 2 * ix + 2
    max_ = ix

    if left_child < key:
        max_ = left_child if a[left_child] > a[max_] else max_
    if right_child < key:
        max_ = right_child if a[right_child] > a[max_] else max_
    if max_ == ix:
        return
    a[ix], a[max_] = a[max_], a[ix]
    make_heap(a, key, max_)


def heap_sort(a: list[float]):
    "Пирамидальная сортировка"

    for i in range(len(a) // 2, -1, -1):
        make_heap(a, len(a), i)
    
    for i in range(len(a) - 1, -1, -1):
        a[0], a[i] = a[i], a[0]
        make_heap(a, i, 0)


def make_test(n, rev=0):
    print(f"Размер массива - {n}")
    array = [rnd.randint(-500, 500) for _ in range(n)]
    if rev == 1:
        array.sort()
    elif rev == -1:
        array.sort(reverse=True)
        
    hybr = round((timeit.timeit(lambda: hybrid_sort(array), number=1)), 5)
    print(f"Гибридная сортировка выполнилась за {hybr} с")

    quick = round((timeit.timeit(lambda: quicksort(array), number=1)), 5)
    print(f"Быстрая сортировка выполнилась за {quick} с")

    heap = round((timeit.timeit(lambda: heap_sort(array), number=1)), 5)
    print(f"Пирамидальная сортировка выполнилась за {heap} с")

    mg = round((timeit.timeit(lambda: merge_sort(array, 0, n), number=1)), 5)
    print(f"Сортировка слиянием выполнилась за {mg} с")

    ins = round((timeit.timeit(lambda: insertion_sort(array, 0, n), number=1)), 5)
    print(f"Сортировка вставками выполнилась за {ins} с")

    d = {round(hybr, 5): "гибридная", round(quick, 5): "быстрая", "пирамидальная": round(heap, 5), 
         "слиянием": round(mg, 5), "вставками": round(ins, 5)}
    print(f"Самой быстрой оказалась сортировка - {d[round(min([hybr, quick, heap, mg, ins]), 5)]}")


if __name__ == "__main__":
   make_test(1000, -1)