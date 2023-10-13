def merge_sort(a: list[int], left, right):
    """Сортировка слиянием"""
    if left >= right or len(a) < 2:
        return
    mid = (left + right) // 2
    merge_sort(a, left, mid)
    merge_sort(a, mid + 1, right)
    merge(a, left, right, mid)


def merge(a: list[int], start: int, end: int, mid: int):
    """Слияние двух частей массива на очередном вызове рекурсии"""
    p1, p2 = 0, 0
    ix = start
    left_half, right_half = a[start:mid+1], a[mid+1:end+1]
    print(left_half, right_half)

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


if __name__ == "__main__":
    # merge sort
    a = list(map(int, input("Введите числа массива через пробел: ").split()))
    merge_sort(a, 0, len(a) - 1)
    print("Отсортированный массив:", a)

