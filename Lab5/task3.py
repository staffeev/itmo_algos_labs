from random import randint
import simple_colors as sc


def find_subseq(n: int, a: list[int]) -> tuple[int, int]:
    """Возвращает индексы начала и конца наибольшей возврастающей подпоследовательности"""
    pref = [0] * n
    pref[0] = 1
    max_ = 1
    for i in range(1, n):
        if a[i] > a[i - 1]:
            pref[i] = pref[i - 1] + 1
            max_ = max(max_, pref[i])
        else:
            pref[i] = 1
    print(pref)
    end_index = pref.index(max_)
    start_index = end_index - max_ + 1
    return start_index, end_index


if __name__ == "__main__":
    n = int(input())
    array = [randint(-100, 100) for _ in range(n)]
    print(*array)
    start_ix, end_ix = find_subseq(n, array)
    print(*[sc.cyan(array[i]) if start_ix <= i <= end_ix else array[i] for i in range(n)])
