import heapq

def prim(vertices, edges, start):
    graph = {v: [] for v in vertices}
    for u, v, weight in edges:
        graph[u].append((weight, v))
        graph[v].append((weight, u))
    
    mst = []
    visited = set()
    min_heap = [(0, start, None)]  # (가중치, 현재 정점, 이전 정점)
    
    while min_heap and len(visited) < len(vertices):
        weight, current, prev = heapq.heappop(min_heap)
        if current not in visited:
            visited.add(current)
            if prev is not None:
                mst.append((prev, current, weight))
            for edge in graph[current]:
                if edge[1] not in visited:
                    heapq.heappush(min_heap, (edge[0], edge[1], current))
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

mst = prim(vertices, edges, 'A')
print("프림 알고리즘으로 찾은 MST:", mst)
