with open("2015/day05.txt", 'r') as file:
    puzzle_input = file.read()

puzzle_input = """ugknbfddgicrmopn
qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy"""

input = puzzle_input.split("\n")

nice_strings = 0
for s in input:
    # print(s)

    vowels = ["a", "e", "i", "o", "u"]
    check_for_vowels = len([i for i in s if i in vowels]) >= 3
    # print(check_for_vowels)

    check_for_doubles = len([s[i] for i in range(len(s)-1) if s[i]==s[i+1]]) >= 1
    # print(check_for_doubles)

    yuks = ["ab", "cd", "pq", "xy"]
    check_for_yuks = len([s[i]+s[i+1] for i in range(len(s)-1) if s[i]+s[i+1] in yuks]) == 0
    # print(check_for_yuks)

    if check_for_vowels and check_for_doubles and check_for_yuks:
        nice_strings += 1

print(f"Part 1: {nice_strings}")

nice_strings = 0
for s in input:
    # print(s)

    check_for_double_doubles = False
    doubles = set([s[i]+s[i+1] for i in range(len(s)-1)])
    double_doubles = 0
    for double in doubles:
        list_s = list(s)
        matches = 0
        for i in range(len(list_s)-1):
            if list_s[i] == double[0] and list_s[i+1] == double[1]:
                matches += 1
                list_s[i] = "@"
                list_s[i+1] = "@"
        if matches >= 2:
            check_for_double_doubles = True
            break
    # print(check_for_double_doubles)

    check_for_triplets = len([s[i]+s[i+1]+s[i+2] for i in range(len(s)-2) if s[i]==s[i+2]]) >= 1
    # print(check_for_triplets)
    
    if check_for_double_doubles and check_for_triplets:
        nice_strings += 1

print(f"Part 2: {nice_strings}")