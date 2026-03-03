class UnionFind:
    def __init__(self, n):
        # Assuming vertices are 1-indexed based on your input
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.count = n

    def find(self, e):
        if self.parent[e] != e:
            self.parent[e] = self.find(self.parent[e]) # Path compression
        return self.parent[e]

    def union(self, e1, e2):
        root1 = self.find(e1)
        root2 = self.find(e2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            self.count -= 1
            return True
        return False

def union(self, e1, e2):
    root1 = self.find(e1)
    root2 = self.find(e2)

    if root1 != root2:
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
        
        self.count -= 1
        return True
    return False

import heapq

class PriorityQ:
    def __init__(self):
        self.heap = [] 

    def is_empty(self):
        return len(self.heap) == 0

    def add(self, weight, u, v):
       heapq.heappush(self.heap, (weight, u, v))

    def remove(self):
       return heapq.heappop(self.heap)

def kruskals_algorithm(num_vertices, edges):
    mst = []
    total_cost = 0
    
    pq = PriorityQ()
    for u, v, weight in edges:
        pq.add(weight, u, v)
        
    uf = UnionFind(num_vertices)
    
    while not pq.is_empty() and len(mst) < num_vertices - 1:
        weight, u, v = pq.remove()
        
        root_u = uf.find(u)
        root_v = uf.find(v)
        
        if root_u != root_v:
            uf.union(root_u, root_v)
            mst.append((u, v, weight))
            total_cost += weight
            
    return mst, total_cost

num_v = 4

edges = [
(1, 2, 10),
(2, 3, 15),
(1, 3, 5),
(3, 4, 10),
(2, 4, 2)
]

mst, cost = kruskals_algorithm(num_v, edges)
print(f"Minimum Spanning Tree: {mst}")
print(f"Total Cost: {cost}")