from collections import defaultdict

with open("2024/day08.txt", 'r') as file:
    puzzle_input = file.read()

puzzle_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

input = [list(line) for line in puzzle_input.split("\n")]

antinodes = set()
frequencies = defaultdict(set)

rows = len(input)
cols = len(input[0])

for i in range(rows):
    for j in range(cols):
        if input[i][j] != ".":
            frequencies[input[i][j]].add((i, j))
            antinodes.add((i, j))

for f, coords in frequencies.items():
    coords_list = list(coords)
    # print(f, coords)
    for c in range(len(coords_list)):
        for d in range(c+1, len(coords_list)):
            try:
                
                x_1 = coords_list[c][0]
                x_2 = coords_list[d][0]
                x_distance = x_2-x_1

                y_1 = coords_list[c][1]
                y_2 = coords_list[d][1]
                y_distance = y_2-y_1
                
                # print(f"({x_1}, {y_1}) ({x_2}, {y_2})")

                # Negative antinodes
                for r in range(1, rows):
                    x_a_1 = x_1 - (x_distance * r)
                    y_a_1 = y_1 - (y_distance * r)
                    # print(f"Neg antinode: ({x_a_1}, {y_a_1})")

                    if (0 <= x_a_1 < rows) & (0 <= y_a_1 < cols):
                        antinodes.add((x_a_1, y_a_1))

                # Positive antinode
                for r in range(1, rows):
                    x_a_2 = x_2 + (x_distance * r)
                    y_a_2 = y_2 + (y_distance * r)
                    # print(f"2nd antinode: ({x_a_2}, {y_a_2})")

                    if (0 <= x_a_2 < rows) & (0 <= y_a_2 < cols):
                        antinodes.add((x_a_2, y_a_2))

            except IndexError:
                pass

print(f"Part 2 : {len(antinodes)}")