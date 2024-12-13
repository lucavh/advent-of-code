from collections import deque

def get_neighbors(x, y, n, m):
    # Directions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            neighbors.append((nx, ny))
    return neighbors


def bfs(grid, start_x, start_y, visited):
    queue = deque()
    queue.append((start_x, start_y))
    plant_type = grid[start_x][start_y]
    region_plots = []
    
    while queue:
        x, y = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        region_plots.append((x, y))
        
        for nx, ny in get_neighbors(x, y, len(grid), len(grid[0])):
            if not visited[nx][ny] and grid[nx][ny] == plant_type:
                queue.append((nx, ny))
    
    return region_plots


def calculate_area_and_perimeter(region, grid):
    area = len(region)
    perimeter = 0
    plant_type = grid[region[0][0]][region[0][1]]

    # Use a set to track unique perimeter edges
    perimeter_edges = set()

    for x, y in region:
        # Check each side of the plot
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] != plant_type:
                perimeter_edges.add(((x, y), (nx, ny)))

    perimeter = len(perimeter_edges)
    return area, perimeter


with open("2024/day12.txt", 'r') as file:
    puzzle_input = file.read()

puzzle_input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

grid = [list(line) for line in puzzle_input.split('\n')]
visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
total_price = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if not visited[i][j]:
            region = bfs(grid, i, j, visited)
            area, perimeter = calculate_area_and_perimeter(region, grid)
            total_price += area * perimeter
            # print(grid[i][j], area, perimeter)
    
print(f"Part 1: {total_price}")


def count_connected_lines(points, axis='y'):
    if axis == 'y':
        points.sort(key=lambda point: (point[1], point[0]))
    elif axis == 'x':
        points.sort(key=lambda point: (point[0], point[1]))
    connected_lines = 0
    current_line = set()

    for (x, y) in points:
        if not current_line:
            current_line.add((x, y))
        else:
            if axis == 'y':
                is_connected = any(abs(x - px) == 1 and y == py for (px, py) in current_line)
            elif axis == 'x':
                is_connected = any(abs(y - py) == 1 and x == px for (px, py) in current_line)
            else:
                raise ValueError("Invalid axis. Choose 'x' or 'y'.")

            if is_connected:
                current_line.add((x, y))
            else:
                connected_lines += 1
                current_line = {(x, y)}

    if current_line:
        connected_lines += 1

    return connected_lines


def calculate_area_and_sides(region, grid):
    area = len(region)
    plant_type = grid[region[0][0]][region[0][1]]

    lh = []
    rh = []
    tv = []
    bv = []
    
    for x, y in region:
        
        dx, dy = (-1, 0)
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] != plant_type:
            tv.append((x,y))
        
        dx, dy = (1, 0)
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] != plant_type:
            bv.append((x,y))

        dx, dy = (0, -1)
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] != plant_type:
            lh.append((x,y))
        
        dx, dy = (0, 1)
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] != plant_type:
            rh.append((x,y))

    n_lh = count_connected_lines(lh, axis="y")
    n_rh = count_connected_lines(rh, axis="y")
    n_tv = count_connected_lines(tv, axis="x")
    n_bv = count_connected_lines(bv, axis="x")
    # print(lh, n_lh, n_rh, n_tv, n_bv)
    sides = n_lh + n_rh + n_tv + n_bv
    return area, sides

visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
total_price = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if not visited[i][j]:
            region = bfs(grid, i, j, visited)
            area, sides = calculate_area_and_sides(region, grid)
            total_price += area * sides
            # print(grid[i][j], area, sides)
    
print(f"Part 2: {total_price}")
