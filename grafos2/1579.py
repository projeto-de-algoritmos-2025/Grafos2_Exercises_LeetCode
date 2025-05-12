class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.count = n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        self.count -= 1
        return True

class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        alice = UnionFind(n)
        bob = UnionFind(n)
        removed = 0

        # Primeiro, use as arestas do tipo 3
        for t, u, v in edges:
            if t == 3:
                if not (alice.union(u, v) | bob.union(u, v)):
                    removed += 1

        # Depois, use as arestas do tipo 1 para Alice e 2 para Bob
        for t, u, v in edges:
            if t == 1:
                if not alice.union(u, v):
                    removed += 1
            elif t == 2:
                if not bob.union(u, v):
                    removed += 1

        if alice.count > 1 or bob.count > 1:
            return -1
        return removed
        