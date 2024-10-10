class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find_parent(parent, x)
        root_y = self.find_parent(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def boruvka(self):
        parent = []
        rank = []
        cheapest = [-1] * self.V
        num_trees = self.V
        mst_weight = 0

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while num_trees > 1:
            for i in range(self.V):
                cheapest[i] = -1

            for u, v, w in self.graph:
                set_u = self.find_parent(parent, u)
                set_v = self.find_parent(parent, v)

                if set_u != set_v:
                    if cheapest[set_u] == -1 or cheapest[set_u][2] > w:
                        cheapest[set_u] = [u, v, w]
                    if cheapest[set_v] == -1 or cheapest[set_v][2] > w:
                        cheapest[set_v] = [u, v, w]

            for node in range(self.V):
                if cheapest[node] != -1:
                    u, v, w = cheapest[node]
                    set_u = self.find_parent(parent, u)
                    set_v = self.find_parent(parent, v)

                    if set_u != set_v:
                        mst_weight += w
                        self.union(parent, rank, set_u, set_v)
                        num_trees -= 1

        print("MST의 총 가중치:", mst_weight)

# 그래프 초기화 및 간선 추가
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.boruvka()
