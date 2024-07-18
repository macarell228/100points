import sys

sys.setrecursionlimit(20000)

with open('medium_B.txt', 'r') as f:
    n, k = map(int, f.readline().split())
    edges = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        v, u = map(int, f.readline().split())
        v -= 1
        u -= 1
        edges[v].append(u)
        edges[u].append(v)

used = [False for _ in range(n)]
potential = []


def dfs(cur):
    used[cur] = True

    if cur == 0:
        if len(edges[cur]) == 0:
            return 1
    else:
        if len(edges[cur]) == 1:
            return 1

    q_leaves = 0
    for neighbour in edges[cur]:
        if used[neighbour]:
            continue

        q_leaves += dfs(neighbour)

    if q_leaves == k:
        potential.append(cur)

    return 0  # сама эта вершина не лист, значит, на своего предка она не влияет


dfs(0)
print(min(potential) + 1) # все действия были в 0-индексации, поэтому +1 в конце
