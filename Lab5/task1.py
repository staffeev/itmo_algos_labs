import random
import copy

def knapsack_dynamic_programming(stuff, capacity):
    n = len(stuff)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    #заполнение dp динамически
    for i in range(1, n + 1):
        for j in range(capacity + 1):
            weight, price = stuff[i - 1]
            dp[i][j] = dp[i - 1][j]
            if weight <= j:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - weight] + price)


    #получение забранных предметов
    result = []

    for i in range(n, 0, -1):
        if dp[i][capacity] != dp[i - 1][capacity]:
                result.append(stuff[i - 1])
                capacity -= stuff[i - 1][0]

    return result



if __name__ == '__main__':
    N, M, K = map(int, input().split())
    """stuff = [(random.randint(1, 30), random.randint(1, 30)) for _ in range(N)]"""
    stuff = [(1, 2), (2, 1), (1, 4), (2, 10), (1, 14), (6, 10), (3, 8)]
    print(stuff)
    general_stolen_stuff = []
    for _ in range(M):
        if len(stuff) == 0:
            break

        stolen_stuff = knapsack_dynamic_programming(stuff, K)
        general_stolen_stuff.append(stolen_stuff)

        # Удаляем вещи, которые унесли
        for item in stolen_stuff:
            stuff.remove(item)



    for i, stolen_stuff in enumerate(general_stolen_stuff, start=1):
        print(f"Заход {i}:")
        for weight, price in stolen_stuff:
            print(f"weight: {weight}, price: {price}")


