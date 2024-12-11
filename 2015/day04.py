import hashlib

with open("2015/day04.txt", 'r') as file:
    puzzle_input = file.read()

puzzle_input = "abcdef"

def solve(n):
    i = 0
    while True:
        s_i = puzzle_input + str(i)
        hex_code = hashlib.md5(s_i.encode()).hexdigest()
        if hex_code[:n] == ("0" * n):
            return s_i.replace(puzzle_input, "")
        i += 1
    
print(f"Part 1: {solve(5)}")
print(f"Part 2: {solve(6)}")