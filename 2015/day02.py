with open("2015/day02.txt", 'r') as file:
    puzzle_input = file.read()

puzzle_input = """1x4x6
9x13x16
32x21x14
16x4x13"""

input_list = [
    [int(d) for d in line] 
    for line in [line.split("x") for line in puzzle_input.split("\n")]
]

total = 0
for l,w,h in input_list:
    total += 2*l*w + 2*w*h + 2*h*l + min([l*w, w*h, h*l])

print(f"Part 1: {total}")

total = 0
for present in input_list:
    s_d = sorted(present)
    total += s_d[0] * 2 + s_d[1] * 2 + s_d[0] * s_d[1] * s_d[2]

print(f"Part 2: {total}")