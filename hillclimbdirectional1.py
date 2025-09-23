graph = {
    'A': {'B': 2},
    'B': {'C': 3},  
    'C': {'D': 1},
    'D': {'A': 4}   
}
def print_all_edges():
    print("Cost of all edges in the directed graph:")
    for node, neighbors in graph.items():
        for neighbor, cost in neighbors.items():
            print(f"Edge {node} -> {neighbor}: Cost {cost}")

def calculate_path_cost(path_name, path_nodes):
    print(f"\ncost for path {' -> '.join(path_nodes)}:")
    total_cost = 0
    valid_path = True
    
    for i in range(len(path_nodes) - 1):
        current = path_nodes[i]
        next_node = path_nodes[i + 1]
        
        if current in graph and next_node in graph[current]:
            cost = graph[current][next_node]
            print(f"edge: Cost {cost}")
            total_cost += cost
        else:
            print(f"Error: No directed edge from {current} to {next_node}!")
            valid_path = False
            total_cost = -1
            break
    
    if valid_path:
        print(f"Total cost: {total_cost}")
    else:
        print("Invalid path")
    
    return total_cost

print_all_edges()

path1 = ['A', 'B', 'C', 'D']
calculate_path_cost("A -> B -> C -> D", path1)

path2 = ['A', 'B', 'C', 'D', 'A']
calculate_path_cost("A -> B -> C -> D -> A", path2)
