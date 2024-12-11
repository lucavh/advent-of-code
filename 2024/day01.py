with open("2024/day01.txt", 'r') as file:
    puzzle_input = file.readlines()

puzzle_input = """3   4
4   3
2   5
1   3
3   9
3   3""".split("\n")

left_column = []
right_column = []

for line in puzzle_input:
    left, right = line.split()
    left_column.append(int(left))
    right_column.append(int(right))

left_sorted = sorted(left_column)
right_sorted = sorted(right_column)

print(f"Part 1: {sum([abs(left_sorted[i] - right_sorted[i]) for i in range(len(left_sorted))])}")
print(f"Part 2: {sum([(i * len([j for j in right_sorted if j == i])) for i in left_sorted])}")