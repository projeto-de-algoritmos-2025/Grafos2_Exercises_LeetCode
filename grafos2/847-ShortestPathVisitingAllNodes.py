from collections import deque

def shortestPathLength(graph):
    n = len(graph)
    target = (1 << n) - 1 
    queue = deque()
    visited = set()

    for i in range(n):
        mask = 1 << i
        queue.append((i, mask, 0))
        visited.add((i, mask))

    while queue:
        node, mask, dist = queue.popleft()

        if mask == target:
            return dist

        for neighbor in graph[node]:
            next_mask = mask | (1 << neighbor)
            if (neighbor, next_mask) not in visited:
                visited.add((neighbor, next_mask))
                queue.append((neighbor, next_mask, dist + 1))