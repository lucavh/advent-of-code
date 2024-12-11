import re

def find_diagonals_left(test):
      results = set()
      for i in range(len(test)):
        tmp1=""
        tmp2=""
        for j in range(0,len(test)-i):
            tmp1+=test[i+j][j]
            tmp2+=test[j][i+j]
        results.add(tmp1)
        results.add(tmp2)
      return list(results) # if you need to return it like a list


def find_diagonals_right(test):
    results = set()
    n=len(test)
    for i in range(n):
        tmp1=""
        tmp2=""
        for j in range(i+1):
            tmp1+=test[i-j][j]
            tmp2+=test[n-1-j][n-1-i+j]
        results.add(tmp1)
        results.add(tmp2)
    return list(results)


def use_regex(input_text, regex):
    pattern = re.compile(regex, re.IGNORECASE)
    return pattern.findall(input_text)


with open("2024/day04.txt", 'r') as file:
    puzzle_input = file.readlines()

puzzle_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split("\n")

lines = [line.strip('\n') for line in puzzle_input]

results = 0

# Find horizontal
for line in lines:
    matches = use_regex(line, r"(XMAS)")
    results += len(matches)
    matches = use_regex(line, r"(SAMX)")
    results += len(matches)

# Find vertical
length = len(list(lines[0]))
for i in range(len(lines[0])):
    h_line = ''.join([line[i] for line in lines])
    matches = use_regex(h_line, r"(XMAS)")
    results += len(matches)
    matches = use_regex(h_line, r"(SAMX)")
    results += len(matches)

# Find diagonal
lines_as_list = [list(line) for line in lines]
diagonals_left = find_diagonals_left(lines)
for d_line in diagonals_left:
    matches = use_regex(d_line, r"(XMAS)")
    results += len(matches)
    matches = use_regex(d_line, r"(SAMX)")
    results += len(matches)

diagonals_right = find_diagonals_right(lines)
for d_line in diagonals_right:
    matches = use_regex(d_line, r"(XMAS)")
    results += len(matches)
    matches = use_regex(d_line, r"(SAMX)")
    results += len(matches)

print(f"Part 1: {results}")

test_lines = lines

n_rows = len(test_lines) 
n_cols = len(test_lines[0])

count = 0

for i in range(n_rows):
    if i+2 < n_rows:
        for j in range(n_rows):
            if j+2 < n_cols:
                
                c_c = test_lines[i+1][j+1]
                if c_c == "A":
                    
                    t_l = test_lines[i][j]
                    t_r = test_lines[i][j+2]
                    b_l = test_lines[i+2][j]
                    b_r = test_lines[i+2][j+2]

                    if (
                        ((t_l == "M") & (b_r == "S")) or 
                        ((t_l == "S") & (b_r == "M"))
                    ):
                        if (
                            ((t_r == "M") & (b_l == "S")) or 
                            ((t_r == "S") & (b_l == "M"))
                        ):
                            count += 1

print(f"Part 2: {count}")