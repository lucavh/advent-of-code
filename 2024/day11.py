from collections import Counter
import math


def solve(n_blinks, stones):
    current = dict(Counter(stones))

    for _ in range(n_blinks):
        updated = {}
        for stone, count in current.items():
            if stone == 0:
                updated[1] = updated.get(1, 0) + count
            else:
                length = math.floor(math.log10(stone)) + 1
                if length % 2 == 0:
                    half_length = length // 2
                    power_of_ten = 10 ** half_length
                    left_part = stone // power_of_ten
                    right_part = stone % power_of_ten

                    updated[left_part] = updated.get(left_part, 0) + count
                    updated[right_part] = updated.get(right_part, 0) + count
                else:
                    new_number = stone*2024
                    updated[new_number] = updated.get(new_number, 0) + count
                
        current = updated
    return sum(updated.values())


with open("2024/day11.txt", 'r') as file:
    puzzle_input = file.read()

puzzle_input = "125 17"

stones = [int(stone) for stone in puzzle_input.split(" ")]

print(f"Part 1: {solve(6, stones)}")
print(f"Part 2: {solve(75, stones)}")