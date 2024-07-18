with open('hard_A.txt', 'r') as f:
    n = int(f.readline())
    edges = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        v, u, cost = map(int, f.readline().split())
        edges[v].append((u, cost))
        edges[u].append((v, cost))

for i, neighbours in enumerate(edges):
    if i == 0:
        continue
    print(i, 'is connected to', *neighbours)
