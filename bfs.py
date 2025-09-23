from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    print("\nBFS Traversal Order:")
    while queue:
        node = queue.popleft()
        if node not in visited:
            print("Visited:", node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter name of node {i+1}: ")
    graph[node] = []

e = int(input("Enter number of edges: "))
print("Enter each edge as 'node1 node2':")

for _ in range(e):
    u, v = input().split()
graph[u].append(v)
graph[v].append(u) 
start_node = input("Enter starting node for BFS: ")
bfs(graph, start_node)
