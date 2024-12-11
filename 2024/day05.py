from collections import defaultdict

with open("2024/day05.txt", 'r') as file:
    puzzle_input = file.read().split("\n\n")

puzzle_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".split("\n\n")

ordering_rules_list = [line.split("|") for line in puzzle_input[0].split("\n")]
ordering_rules = defaultdict()
for rule in ordering_rules_list:
    k = int(rule[0])
    v = int(rule[1])
    if k in ordering_rules.keys():
        ordering_rules[k] = ordering_rules[k] + [v]
    else:
        ordering_rules[k] = [v]

pages_to_produce = [[int(x) for x in line] for line in [line.split(",") for line in puzzle_input[1].split("\n")]]

k = ordering_rules.keys()

middle_values = []
false_sequences = []

for sequence in pages_to_produce:
    check = True
    for i in range(len(sequence)):

        if (i > len(sequence)-2):
            continue

        if (sequence[i] in k):
            successors = ordering_rules[sequence[i]]
            if sequence[i+1] in successors:
                check = True
            else:
                check = False
                break
        else:
            check = False
            break
    
    if check: 
        middle = int(len(sequence)/2)
        middle_values.append(sequence[middle])
    else:
        false_sequences.append(sequence)

print(f"Part 1: {sum(middle_values)}")

middle_values = []

for sequence in false_sequences:
    check = False

    while check == False:
        # Update
        for i in range(len(sequence)):
            if (i > len(sequence)-2):
                continue
            elif (sequence[i] in k) and (sequence[i+1] not in ordering_rules[sequence[i]]):
                    i_0 = sequence[i]
                    sequence[i] = sequence[i+1]
                    sequence[i+1] = i_0
            elif (sequence[i] not in k):
                i_0 = sequence[i]
                sequence[i] = sequence[i+1]
                sequence[i+1] = i_0
        
        # Check
        for i in range(len(sequence)):
            if (i > len(sequence)-2):
                continue
            elif (sequence[i] in k):
                if sequence[i+1] not in ordering_rules[sequence[i]]:
                    check = False
                    break
                else:
                    check = True
            else:
                check = False
                break
        
    middle = int(len(sequence)/2)
    middle_values.append(sequence[middle])

print(f"Part 2: {sum(middle_values)}")
