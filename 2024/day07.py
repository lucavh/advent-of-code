import itertools


def generate_binary_combinations(length):
    return list(itertools.product([0, 1], repeat=length))


def perform_operation(values, operation):
    total = values[0]
    for i in range(len(operation)):
        if operation[i] == 0:  # Addition
            total += values[i+1]
        elif operation[i] == 1:  # Multiplication
            total *= values[i+1]
    return total


with open("2024/day07.txt", 'r') as file:
    puzzle_input = file.read()

puzzle_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

input = {int(e[0]): [int(num) for num in e[1].strip().split(" ")]
              for e in (line.split(":") for line in puzzle_input.split("\n"))}

grand_total = 0

for k,v in input.items():
    operations = generate_binary_combinations(len(v)-1)
    for operation in operations:
        total = perform_operation(v,operation)
        if total == k:
            grand_total += k
            break
        else:
            pass

print(f"Part 1: {grand_total}")