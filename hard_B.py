import sys

sys.setrecursionlimit(20000)

with open('hard_B.txt', 'r') as f:
    n = int(f.readline())
    edges = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        v, u, cost = map(int, f.readline().split())
        v -= 1
        u -= 1
        edges[v].append((u, cost))
        edges[u].append((v, cost))

used = [False for _ in range(n)]


def dfs(cur):
    used[cur] = True

    result = 10**18
    has_kids = False
    for neighbour, weight in edges[cur]:
        if used[neighbour]:
            continue

        has_kids = True

        result = min(result, dfs(neighbour) + weight)

    if has_kids:
        return result
    return 0


print(dfs(0))
