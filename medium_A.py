with open('medium_A.txt', 'r') as f:
    n, k = map(int, f.readline().split())
    edges = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        v, u = map(int, f.readline().split())
        edges[v].append(u)
        edges[u].append(v)

for i, neighbours in enumerate(edges):
    if i == 0:
        continue
    print(i, 'is connected to', *neighbours)


