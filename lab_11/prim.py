from queue import PriorityQueue

def prim(g):
    n = len(g)
    visited = [False] * n
    T = set()
    u = 0
    visited[u] = True
    Q = PriorityQueue()
    for v in range(n):
        if v != u:
            Q.put((g[u][v], u, v))

    while not Q.empty():
        weight, u, v = Q.get()
        if visited[v]: continue
        T.add((u, v, weight))
        visited[v] = True
        for w in range(n):
            if not visited[w] and w != v:
                Q.put((g[v][w], v, w))

    return T


graph2 = [(0, 1, 1), (0, 4, 4), (0, 5, 8), (1, 5, 6), (1, 2, 2), (1, 6, 6),
         (2, 6, 2), (2, 3, 3), (3, 6, 1), (3, 7, 4), (4, 5, 5), (5, 6, 1),
         (6, 7, 1)]

graph = [
    [0,1,0,0,4,8,0,0],
    [1,0,2,0,0,6,6,0],
    [0,2,0,3,0,0,2,0],
    [0,0,3,0,0,0,1,4],
    [4,0,0,0,0,5,0,0],
    [8,6,0,0,5,0,1,0],
    [0,6,2,1,0,1,0,1],
    [0,0,0,4,0,0,1,0]
]

T = prim(graph)
print(T)