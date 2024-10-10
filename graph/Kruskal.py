class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root != v_root:
            self.parent[v_root] = u_root

def kruskal(vertices, edges):
    ds = DisjointSet(vertices)
    mst = []
    edges = sorted(edges, key=lambda x: x[2])  # 간선을 가중치 기준으로 정렬

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
    return mst

# 그래프 예시
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('C', 'D', 1),
    ('C', 'E', 5),
    ('D', 'E', 2)
]

mst = kruskal(vertices, edges)
print("크루스칼 알고리즘으로 찾은 MST:", mst)
