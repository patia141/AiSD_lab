class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            self.parent[root1] = root2


def kruskal(graph):
    vertices = set()
    for edge in graph:
        vertices.add(edge[0])
        vertices.add(edge[1])

    ds = DisjointSet(vertices)
    graph.sort(key=lambda item: item[2])

    tree = []
    for edge in graph:
        u, v, weight = edge
        if ds.find(u) != ds.find(v):
            tree.append(edge)
            ds.union(u, v)

    return tree


graph = [(0, 1, 1), (0, 4, 4), (0, 5, 8), (1, 5, 6), (1, 2, 2), (1, 6, 6),
         (2, 6, 2), (2, 3, 3), (3, 6, 1), (3, 7, 4), (4, 5, 5), (5, 6, 1),
         (6, 7, 1)]

drzewko = kruskal(graph)
print(drzewko)