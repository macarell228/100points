import sys

sys.setrecursionlimit(20000)

with open('easy_B.txt', 'r') as f:
    n = int(f.readline())
    edges = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        v, u = map(int, f.readline().split())
        v -= 1
        u -= 1
        edges[v].append(u)
        edges[u].append(v)

used = [False for _ in range(n)]


def dfs(cur):
    used[cur] = True

    if cur == 0:
        if len(edges[cur]) == 0:
            return 1
    else:
        if len(edges[cur]) == 1:
            return 1

    s = 0
    for neighbour in edges[cur]:
        if used[neighbour]:
            continue

        s += dfs(neighbour)

    return s


print(dfs(0))
