import re
import pulp

def get_x_y(note):
    coordinates = re.findall(r'X[+=](\d+), Y[+=](\d+)', note)
    print
    return tuple(map(int, coordinates[0]))


def find_minimum_cost_path(a,b,p, scale_factor=1):
    problem = pulp.LpProblem("find_minimum_cost_path", pulp.LpMinimize)

    a_presses = pulp.LpVariable('A', lowBound=0, cat='Integer')
    b_presses = pulp.LpVariable('B', lowBound=0, cat='Integer')

    problem += a_presses * a[2] + b_presses * b[2], "total_cost"
    
    x = p[0] / scale_factor
    y = p[1] / scale_factor
    ax = a[0] / scale_factor
    ay = a[1] / scale_factor
    bx = b[0] / scale_factor
    by = b[1] / scale_factor
    problem += a_presses * ax + b_presses * bx == x, "X"
    problem += a_presses * ay + b_presses * by == y, "Y"

    problem.solve(pulp.PULP_CBC_CMD(msg=False))

    if pulp.LpStatus[problem.status] == "Optimal":
        return pulp.value(problem.objective)
    return 0   


with open("2024/day13.txt", 'r') as file:
    puzzle_input = file.read()

puzzle_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

tokens_total = 0

for i in puzzle_input.split("\n\n"):
    instructions = i.split("\n")

    a = get_x_y(instructions[0]) + (3,)
    b = get_x_y(instructions[1]) + (1,)
    p = get_x_y(instructions[2])

    tokens = find_minimum_cost_path(a,b,p)
    tokens_total += tokens
    # print(tokens)

print(f"Part 1: {int(tokens_total)}")

tokens_total = 0

for i in puzzle_input.split("\n\n"):

    instructions = i.split("\n")

    a = get_x_y(instructions[0])
    b = get_x_y(instructions[1])
    p = get_x_y(instructions[2])
    p = tuple(x + 10000000000000 for x in p)
    
    A = int((p[0] * b[1] - p[1] * b[0]) / (a[0] * b[1] - a[1] * b[0]))
    B = int((a[0] * p[1] - a[1] * p[0]) / (a[0] * b[1] - a[1] * b[0]))

    if ((A * a[0] + B * b[0]) == p[0]) & ((A * a[1] + B * b[1]) == p[1]):
        tokens_total += (A*3 + B*1)
    
print(f"Part 2: {int(tokens_total)}")