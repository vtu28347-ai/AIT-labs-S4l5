def a_star(graph, h, start, goal):
    queue = [(h[start], start)]
    g_cost = {start: 0}
    path = {}

    while queue:
        queue.sort()
        f, current = queue.pop(0)
        if current == goal:
            p = []
            while current:
                p.append(current)
                current = path.get(current)
            return p[::-1], g_cost[goal]

        for nbr, w in graph.get(current, {}).items():
            cost = g_cost[current] + w
            if cost < g_cost.get(nbr, float('inf')):
                g_cost[nbr] = cost
                path[nbr] = current
                queue.append((cost + h[nbr], nbr))
    return None, None


graph = {'S': {'A': 2, 'B': 3}, 'A': {'G': 1}, 'B': {'G': 2}}
h = {'S': 5, 'A': 2, 'B': 3, 'G': 0}

path, cost = a_star(graph, h, 'S', 'G')

if path:
    print(f"Path: {' -> '.join(path)}")
    print(f"Total cost: {cost}")
else:
    print("No path found.")
