with open("2015/day01.txt", 'r') as file:
    puzzle_input = file.read()

puzzle_input = "()())((())())))()((((()((()"

level = 0

for c in list(puzzle_input):
    if c == "(":
        level += 1
    if c == ")":
        level -= 1

print(f"Part 1: {level}")

level = 0
l = list(puzzle_input)

for i in range(len(l)):
    if l[i] == "(":
        level += 1
    if l[i] == ")":
        level -= 1
    if level < 0:
        print(f"Part 2: {i+1}")
        break