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


def bucket_sort(a: list[float]):
    min_, max_ = float("inf"), float("-inf")
    for el in a:
        min_ = min(el, min_)
        max_ = max(el, max_)

    range_ = max_ - min_

    buckets = [[] for _ in range(len(a))]

    for element in a:
        index = min(int(element * len(a) / range_), len(a) - 1)
        buckets[index].append(element)
    

    print(buckets)

    for i in range(len(buckets)):
        buckets[i] = sorted(buckets[i])

    result = []
    [result.extend(bucket) for bucket in buckets]
    return result

    

if __name__ == "__main__":
    # # merge sort (example 2 4 1 6 8 3 5 7)
    # a = list(map(int, input("Введите числа массива через пробел: ").split()))
    # merge_sort(a, 0, len(a) - 1)
    # print("Отсортированный массив:", a)

    #bucket sort (exampple 21 1 88 2 3 89 23 24 86)
    a = list(map(int, input("Введите числа массива через пробел: ").split()))
    print("Отсортированный массив:", bucket_sort(a))

