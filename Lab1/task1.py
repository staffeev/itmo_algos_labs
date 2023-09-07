def binary_search(a: list[int], x: int) -> int | float:
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


if __name__ == "__main__":
    a = list(map(int, input().split()))
    x = int(input())
    print(binary_search(a, x))
