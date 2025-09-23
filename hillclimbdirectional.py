graph = {
    'A': {'B': 2},
    'B': {'C': 3},
    'C': {'D': 1},
    'D': {'A': 4},
}

print("Cost of all edges:")
for start_node, edges in graph.items():
    for end_node, cost in edges.items(): 
        print(f"Edge {start_node}-{end_node}: cost {cost}")  

total_cost_path = 0
path_edges = [('A', 'B'), ('B', 'C'), ('C', 'D'),('D','A')]

for u, v in path_edges:
    if u in graph and v in graph[u]:
        total_cost_path += graph[u][v]
    else:
        print(f"Error: Edge {u}-{v} not found in graph.")
        total_cost_path = -1
        break

if total_cost_path != -1:
    print(f"\nTotal cost for path A-B-C-D: {total_cost_path}")

path = ['A', 'B', 'C', 'D', 'A']
total_cost = 0
for i in range(len(path) - 1):
    current_node = path[i]
    next_node = path[i + 1]
    if next_node in graph[current_node]:
        total_cost += graph[current_node][next_node]
    else:
        print(f"Error: No direct edge from {current_node} to {next_node}")
        total_cost = -1
        break

if total_cost != -1:
    print(f"\nTotal cost of path ABCDA: {total_cost}")
