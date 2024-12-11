def find_routes(grid):
    def is_valid(x, y, prev_val):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            cell_val = grid[x][y]
            if cell_val.isdigit() and int(cell_val) == prev_val + 1:
                return True
        return False

    def dfs(x, y, path):
        if grid[x][y] == '9':
            routes.append(list(path))
            return

        direction_vectors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        current_val = int(grid[x][y])

        for dx, dy in direction_vectors:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, current_val):
                path.append((nx, ny))
                dfs(nx, ny, path)
                path.pop()

    # Find starting position '0'
    routes = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '0':
                dfs(i, j, [(i, j)])

    return routes


with open("2024/day10.txt", 'r') as file:
    puzzle_input = file.read()

puzzle_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

grid = [list(line.strip()) for line in puzzle_input.strip().split('\n')]
full_routes = find_routes(grid)
start_end_routes = set([str(route[0])+str(route[-1]) for route in full_routes])

print(f"Part 1: {len(start_end_routes)}")
print(f"Part 2: {len(full_routes)}")