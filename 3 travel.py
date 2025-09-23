def astar(start, goal, grid):
    closed_set = set()
    open_list = [(0 + abs(start[0] - goal[0]) + abs(start[1] - goal[1]), 0, start, [start])]

    while open_list:
        i, (f, g, (x, y), path) = min(enumerate(open_list), key=lambda x: x[1][0])
        open_list.pop(i)

        if (x, y) == goal:
            return path

        if (x, y) in closed_set:
            continue

        closed_set.add((x, y))

        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                if (nx, ny) in closed_set:
                    continue
                new_g = g + 1
                new_f = new_g + abs(nx - goal[0]) + abs(ny - goal[1])
                open_list.append((new_f, new_g, (nx, ny), path + [(nx, ny)]))

    return None


grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

path = astar((0, 0), (4, 4), grid)
print(f"path: {path}\n cost: {len(path) - 1}" if path else "No path found")
