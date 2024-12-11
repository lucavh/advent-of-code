def is_ordered(numbers):
    is_increasing = all(x < y for x, y in zip(numbers, numbers[1:]))
    is_decreasing = all(x > y for x, y in zip(numbers, numbers[1:]))
    return is_increasing or is_decreasing


def is_reasonable_step(numbers):
    is_reasonable_step = all( 1 <= abs(x - y) <= 3 for x, y in zip(numbers, numbers[1:]))
    return is_reasonable_step


with open("2024/day02.txt", 'r') as file:
    puzzle_input = file.readlines()

puzzle_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split("\n")

reports = [[int(number) for number in line.split()] for line in puzzle_input]
valid_reports = [report for report in reports if is_ordered(report) and is_reasonable_step(report)]

print(f"Part 1: {len(valid_reports)}")

valid_reports = []
for report in reports:
    is_valid = (is_ordered(report) and is_reasonable_step(report))

    if is_valid:
        valid_reports.append(report)
        continue

    for i in range(len(report)):
        temp = report[:]
        temp.pop(i)
        
        is_valid = (is_ordered(temp) and is_reasonable_step(temp))
        if is_valid:
            valid_reports.append(report)
            break

print(f"Part 2: {len(valid_reports)}")