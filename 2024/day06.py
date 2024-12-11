with open("2024/day06.txt", 'r') as file:
    puzzle_input = file.read()

puzzle_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

input = [list(line) for line in puzzle_input.split("\n")]
len(input), len(input[0])

map  = input
rows = len(map)
cols = len(map[0])

directions = ["^", ">", "v", "<"]
next_directions = {
    "^":">", 
    ">":"v", 
    "v":"<", 
    "<":"^"
}

guard_on_scene = True

def find_next_step(d, r, c):
    if d == "^":
        next_r = r-1
        next_c = c
    elif d == ">":
        next_r = r
        next_c = c+1
    elif d == "<":
        next_r = r
        next_c = c-1
    elif d == "v":
        next_r = r+1
        next_c = c
    return next_r, next_c

def check_if_guard_left(rows, cols, r, c, guard_on_scene):   
    if (r < 0) or (c < 0) or (r > rows-1) or (c > cols-1):
        # print("Guard will leave the scene")
        guard_on_scene = False

    return guard_on_scene

# Find starting position
for r in range(rows):
    for c in range(cols):
        if map[r][c] in directions:
            current_r = r
            current_c = c
            direction = map[r][c]

# Predict steps   
while guard_on_scene:
    map[current_r][current_c] = "X"
    (next_r, next_c) = find_next_step(d=direction, r=current_r, c=current_c)

    guard_on_scene = check_if_guard_left(
        rows=rows, 
        cols=cols, 
        r=next_r, 
        c=next_c, 
        guard_on_scene=guard_on_scene)
    
    if guard_on_scene == False:
        break

    if map[next_r][next_c] == "#":
        direction = next_directions[direction]
        (next_r, next_c) = find_next_step(d=direction, r=current_r, c=current_c)
        guard_on_scene = check_if_guard_left(
            rows=rows, 
            cols=cols, 
            r=next_r, 
            c=next_c, 
            guard_on_scene=guard_on_scene)
        
        if guard_on_scene == False:
            break
        
    current_r = next_r
    current_c = next_c

# Count steps
count = 0
for row in map:
    for step in row:
        if step == "X":
            count += 1

print(f"Part 1: {count}")