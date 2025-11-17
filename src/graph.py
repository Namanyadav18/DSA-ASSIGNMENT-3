from typing import Dict, List, Tuple, Optional
import heapq

class CampusGraph:
    def __init__(self, num_nodes: int):
        self.n = num_nodes
        self.adj: Dict[int, List[Tuple[int, float]]] = {i: [] for i in range(num_nodes)}
        self.matrix = [[float('inf')] * num_nodes for _ in range(num_nodes)]
        for i in range(num_nodes):
            self.matrix[i][i] = 0.0

    def add_edge(self, u: int, v: int, w: float):
        # undirected edge
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
        self.matrix[u][v] = w
        self.matrix[v][u] = w

    def bfs(self, start: int) -> List[int]:
        from collections import deque
        visited = [False] * self.n
        q = deque([start])
        visited[start] = True
        order: List[int] = []
        while q:
            u = q.popleft()
            order.append(u)
            for v, _ in self.adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        return order

    def dfs(self, start: int) -> List[int]:
        visited = [False] * self.n
        order: List[int] = []
        def _dfs(u: int):
            visited[u] = True
            order.append(u)
            for v, _ in self.adj[u]:
                if not visited[v]:
                    _dfs(v)
        _dfs(start)
        return order

    def dijkstra(self, src: int) -> Tuple[List[float], List[Optional[int]]]:
        dist = [float('inf')] * self.n
        parent: List[Optional[int]] = [None] * self.n
        dist[src] = 0.0
        heap: List[Tuple[float, int]] = [(0.0, src)]
        while heap:
            d,u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v,w in self.adj[u]:
                nd = dist[u] + w
                if nd < dist[v]:
                    dist[v] = nd
                    parent[v] = u
                    heapq.heappush(heap, (nd, v))
        return dist, parent

    def edges(self) -> List[Tuple[float,int,int]]:
        seen = set()
        eds: List[Tuple[float,int,int]] = []
        for u in self.adj:
            for v,w in self.adj[u]:
                if (v,u) not in seen:
                    eds.append((w,u,v))
                    seen.add((u,v))
        return eds

    def kruskal_mst(self) -> Tuple[float, List[Tuple[int,int,float]]]:
        parent = list(range(self.n))
        rank = [0]*self.n
        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x: int, y: int) -> bool:
            rx, ry = find(x), find(y)
            if rx == ry: return False
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            else:
                parent[ry] = rx
                if rank[rx] == rank[ry]:
                    rank[rx] += 1
            return True
        edges = sorted(self.edges(), key=lambda e: e[0])
        mst_w = 0.0
        mst_edges: List[Tuple[int,int,float]] = []
        for w,u,v in edges:
            if union(u,v):
                mst_edges.append((u,v,w))
                mst_w += w
        return mst_w, mst_edges
