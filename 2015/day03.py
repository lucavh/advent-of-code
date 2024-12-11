with open("2015/day03.txt", 'r') as file:
    puzzle_input = file.read()

puzzle_input = "^<<v<^<v^>^^<<v<"

def walk_route(route, visited):
    visiting_house = (1,1)
    visited.add(visiting_house)
    for i in range(len(route)):
        if route[i] == "^":
            visiting_house = (visiting_house[0]-1, visiting_house[1])
        elif route[i] == "v":
            visiting_house = (visiting_house[0]+1, visiting_house[1])
        elif route[i] == "<":
            visiting_house = (visiting_house[0], visiting_house[1]-1)
        elif route[i] == ">":
            visiting_house = (visiting_house[0], visiting_house[1]+1)
        visited.add(visiting_house)
    return visited

input = list(puzzle_input)

visited = set()
visited = walk_route(input, visited)

print(f"Part 1: {len(visited)}")

santa_input = [input[i] for i in range(len(input)) if (i % 2) == 0]
robo_input = [input[i] for i in range(len(input)) if (i % 2) == 1]

visited = set()
visited = walk_route(santa_input, visited)
visited = walk_route(robo_input, visited)

print(f"Part 2: {len(visited)}")
