def dfs(v: int):
    visited[v] = True
    country.append(v)
    for i in range(x):
        if f[v][i] and not visited[i]:
            dfs(i)


if __name__ == "__main__":
    x = int(input())
    f = []
    for i in range(x):
        f.append(list(map(int, input().split())))
    visited = [False] * x
    countries = []
    country = []
    for i in range(x):
        if not visited[i]:
            dfs(i)
            countries.append(country)
            country = []
    print(countries)
    print(len(countries))