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
    subseq = arr[start_index:max_length_index + 1]
    return subseq, len(subseq)


if __name__ == "__main__":
    arr = [5, 3, 8, 1, 9, 2, 4, 7]
    seq, length = find_longest_increasing_seq(arr)
    print(seq)  # [2, 4, 7]
    print(length)  # 3

    # n = int(input())
    # array = [randint(-100, 100) for _ in range(n)]
    # print(*array)
    # start_ix, end_ix = find_subseq(n, array)
    # print(*[sc.cyan(array[i]) if start_ix <= i <= end_ix else array[i] for i in range(n)])
