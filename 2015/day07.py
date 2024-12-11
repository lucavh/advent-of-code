from collections import defaultdict

with open("2015/day07.txt", 'r') as file:
    puzzle_input = file.read()

puzzle_input = """123 -> x
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
456 -> y
NOT x -> h
NOT y -> i"""

input = puzzle_input.split("\n")

tracker = defaultdict()
parked_input = []

def solve_lines(input, tracker, parked_input):
    
    for line in input:
        x, y = line.split(" -> ")
        x = x.split(" ")

        try:
            if len(x) == 1:
                tracker[y] = int(x[0])
            elif x[1] in ["AND", "OR", "LSHIFT", "RSHIFT"]:
                try:
                    a = int(x[0])
                except:
                    a = tracker[x[0]]
                try:
                    b = int(x[2])
                except:
                    b = tracker[x[2]]

                if x[1] == "AND":
                    tracker[y] = a & b
                elif x[1] == "OR":
                    tracker[y] = a | b
                elif x[1] == "LSHIFT":
                    tracker[y] = a << b
                elif x[1] == "RSHIFT":
                    tracker[y] = a >> b
                    
            elif x[0] == "NOT":
                tracker[y] = ~tracker[x[1]] & 0xFFFF

        except:
            parked_input.append(line)

solve_lines(input, tracker, parked_input)


while len(parked_input) > 0:
    # print(len(parked_input))
    input = parked_input
    parked_input = []

    solve_lines(input, tracker, parked_input)

wire = "i"
print(f"Part 1: {tracker[wire]}")
