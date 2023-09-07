from math import log2, ceil


def binary_search_while(a: list[int], x: int) -> int | float:
    iter_count = 0
    left_bound, right_bound = 0, len(a) - 1
    while left_bound <= right_bound:
        mid = left_bound + (right_bound - left_bound) // 2
        iter_count += 1
        if a[mid] == x:
            return iter_count
        if a[mid] < x:
            left_bound = mid + 1
        else:
            right_bound = mid - 1
    return float("inf")


def binary_search_for(a: list[int], x: int) -> int | float:
    iter_count = 0
    left_bound, right_bound = 0, len(a) - 1
    for _ in range(100):
        if left_bound > right_bound:
            break
        mid = left_bound + (right_bound - left_bound) // 2
        iter_count += 1
        if a[mid] == x:
            return iter_count
        if a[mid] < x:
            left_bound = mid + 1
        else:
            right_bound = mid - 1
    return float("inf")


def binary_search_wcond(a: list[int], x: int) -> int | float:
    iter_count = 0
    left_bound, right_bound = 0, len(a) - 1
    for _ in range(50):
        mid = left_bound + (right_bound - left_bound) // 2
        iter_count += 1
        if a[mid] == x:
            return iter_count
        if a[mid] < x:
            left_bound = mid + 1
        else:
            right_bound = mid - 1
    return float("inf")


def binary_search_log(a: list[int], x: int) -> int | float:
    iter_count = 0
    left_bound, right_bound = 0, len(a) - 1
    for _ in range(ceil(log2(len(a)))):
        mid = left_bound + (right_bound - left_bound) // 2
        iter_count += 1
        if a[mid] == x:
            return iter_count
        if a[mid] < x:
            left_bound = mid + 1
        else:
            right_bound = mid - 1
    return float("inf")