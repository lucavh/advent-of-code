import re

def use_regex(input_text):
    pattern = re.compile(r"mul\(([0-9]+),([0-9]+)\)", re.IGNORECASE)
    return pattern.findall(input_text)


with open("2024/day03.txt", 'r') as file:
    puzzle_input = file.read().replace('\n', '')

puzzle_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

matches = use_regex(puzzle_input)

total = 0
for match in matches:
    num1, num2 = int(match[0]), int(match[1])
    total += int(match[0]) * int(match[1])

print(f"Part 1: {total}")

relevant_text = []
split_on_dont = puzzle_input.split("don't()")
relevant_text.append(split_on_dont[0])

for i in split_on_dont[1:]:
    split_on_do = i.split("do()")
    if len(split_on_do) > 1:
        relevant_text += split_on_do[1:]

matches = use_regex(str(relevant_text))
total = 0

for match in matches:
    num1, num2 = int(match[0]), int(match[1])
    total += int(match[0]) * int(match[1])

print(f"Part 2: {total}")