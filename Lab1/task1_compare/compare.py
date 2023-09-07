import os

os.chdir("task1_compare")


def mean(s):
    n = len(s)
    if n % 2 == 0:
        return (s[n // 2 - 1] + s[n // 2]) / 2
    return s[n // 2]


res_while = sorted(map(float, open("res_while.txt").readlines()))
res_for = sorted(map(float, open("res_for.txt").readlines()))
res_log = sorted(map(float, open("res_log.txt").readlines()))
res_wcond = sorted(map(float, open("res_wcond.txt").readlines()))
m1, m2, m3, m4 = mean(res_while), mean(res_for), mean(res_log), mean(res_wcond)
print(f"Время выполнения с циклом while - {m1}")
print(f"Время выполнения с циклом for - {m2}")
print(f"Время выполнения с циклом for и log - {m3}")
print(f"Время выполнения с циклом for и без условия выхода - {m4}")
d = {m1: "while", m2: "for", m3: "log", m4: "wcond"}
print(d[min(m1, m2, m3)])