from random import randint
import os

os.chdir("task1_compare")

if __name__ == "__main__":
    with open("gen.txt", "w") as file:
        for _ in range(100):
            x = randint(-100, 1100)
            a = [randint(1, 10000) for _ in range(randint(10, 50000))]
            file.write(" ".join(map(str, a)) + "\n")
            file.write(str(x) + "\n")