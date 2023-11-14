from random import randint
import simple_colors as sc


def find_longest_increasing_seq(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            dp[i] = dp[i-1] + 1

    max_length = max(dp)
    max_length_index = dp.index(max_length)
    start_index = max_length_index - max_length + 1
    return start_index, max_length_index


if __name__ == "__main__":
    n = int(input())
    array = [randint(-100, 100) for _ in range(n)]
    print("Исходный массив")
    print(*array)
    start_ix, end_ix = find_longest_increasing_seq(array)
    print("С выделенной подпоследовательностью:")
    print(*[sc.cyan(array[i]) if start_ix <= i <= end_ix else array[i] for i in range(n)])
