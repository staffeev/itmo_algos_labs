from time import time
from functions import binary_search_for, binary_search_while, binary_search_log, binary_search_wcond
import os

os.chdir("task1_compare")


def create(flag="while"):
    title = f"res_{flag}.txt"
    func = {"while": binary_search_while, "for": binary_search_for, "log": binary_search_log,
            "wcond": binary_search_wcond}[flag]
    with open(title, "a") as file:
        for N in range(100):
            print(N + 1)
            start = time()
            for i in range(0, len(f), 2):
                a = sorted(map(int, f[i].split()))
                x = int(f[i + 1])
                res = func(a, x)
            end = time()
            file.write(str(end - start) + "\n")


if __name__ == "__main__":
    f = open("gen.txt").readlines()
    # create("while")
    # create("for")
    # create("log")
    create("wcond")