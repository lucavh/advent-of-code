with open("2015/day06.txt", 'r') as file:
    puzzle_input = file.read()

puzzle_input = """turn on 1,6 through 2,8
turn off 2,6 through 2,7
toggle 1,4 through 8,8"""

instructions = puzzle_input.split("\n")

grid = [[0 for j in range(1000)] for i in range(1000)]

for instruction in instructions:
    action = instruction[6]
    if action == " ":
        start = [int(c) for c in instruction.split(" ")[1].split(",")]
        end = [int(c) for c in instruction.split(" ")[3].split(",")]
    else:
        start = [int(c) for c in instruction.split(" ")[2].split(",")]
        end = [int(c) for c in instruction.split(" ")[4].split(",")]


    for r in range(start[0], end[0]+1, 1):
        for c in range(start[1], end[1]+1, 1):
            if action == "f":
                grid[r][c] = 0
            elif action == "n":
                grid[r][c] = 1
            elif (action == " ") & (grid[r][c] == 0):
                grid[r][c] = 1
            elif (action == " ") & (grid[r][c] == 1):
                grid[r][c] = 0

print(f"Part 1: {sum([sum(r) for r in grid])}")

grid = [[0 for j in range(1000)] for i in range(1000)]

for instruction in instructions:
    action = instruction[6]
    if action == " ":
        start = [int(c) for c in instruction.split(" ")[1].split(",")]
        end = [int(c) for c in instruction.split(" ")[3].split(",")]
    else:
        start = [int(c) for c in instruction.split(" ")[2].split(",")]
        end = [int(c) for c in instruction.split(" ")[4].split(",")]

    for r in range(start[0], end[0]+1, 1):
        for c in range(start[1], end[1]+1, 1):
            if action == "f":
                grid[r][c] -= 1
            elif action == "n":
                grid[r][c] += 1
            elif (action == " "):
                grid[r][c] += 2
    
    grid = [[c if c >= 0 else 0 for c in r]  for r in grid]

print(f"Part 2: {sum([sum(r) for r in grid])}")

