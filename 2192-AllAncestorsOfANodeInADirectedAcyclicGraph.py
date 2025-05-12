from collections import defaultdict, deque


class Solution:
    def getAncestors(self, n, edges):
        graph = defaultdict(list)
        in_degree = [0] * n
        ancestors = [set() for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        queue = deque([i for i in range(n) if in_degree[i] == 0])

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return [sorted(list(a)) for a in ancestors]

sol = Solution()

n1 = 8
edges1 = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
expected1 = [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
assert sol.getAncestors(n1, edges1) == expected1


n2 = 5
edges2 = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
expected2 = [[],[0],[0,1],[0,1,2],[0,1,2,3]]
assert sol.getAncestors(n2, edges2) == expected2

n3 = 3
edges3 = []
expected3 = [[], [], []]
assert sol.getAncestors(n3, edges3) == expected3
