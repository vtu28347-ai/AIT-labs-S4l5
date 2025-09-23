def dfs_iterative(start):
    visited = set()
    stack = [start]

    print("\nDFS Traversal order:")
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(reversed(graph[node]))

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [],
    3: [],
    4: [2]
}

dfs_iterative(0)
