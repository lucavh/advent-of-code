with open("2024/day09.txt", 'r') as file:
    puzzle_input = file.read()

puzzle_input = "2333133121414131402"

input = list(puzzle_input)
files = [input[i] for i in range(len(input)) if (i % 2) == 0]
free_space = [input[i] for i in range(len(input)) if (i % 2) == 1]

full = []
for i in range(len(files)):

    full += int(files[i]) * [i]
    try:
        full += int(free_space[i]) * ["."]
    except IndexError:
        pass

n_files = len([i for i in full if i != "."])
new_full = []

for i in range(len(full)):
    if len(new_full) == n_files:
        break

    if (full[i] != "."):
        new_full.append(full[i])
    elif (full[i] == "."):

        last_file = "."
        while last_file == ".":
            last_file = full[-1]
            full = full[:-1]

        new_full.append(last_file)

print(f"Part 1: {sum([i * new_full[i] for i in range(len(new_full))])}")


def move_files(blocks):
    """Move files to the leftmost free space that can accommodate them."""
    max_file_id = max((block for block in blocks if block != '.'), default=-1)

    for file_id in range(max_file_id, -1, -1):
        file_indices = [i for i, block in enumerate(blocks) if block == file_id]
        if not file_indices:
            continue

        file_start = file_indices[0]
        file_end = file_indices[-1] + 1
        file_length = file_end - file_start

        for i in range(len(blocks) - file_length + 1):
            if all(block == '.' for block in blocks[i:i + file_length]) & (i < file_start):
                new_blocks = blocks[:]
                new_blocks[file_start:file_end] = ['.'] * file_length
                new_blocks[i:i + file_length] = [file_id] * file_length
                blocks[:] = new_blocks
                break  # Move on to the next file
    return blocks


def calculate_checksum(blocks):
    """Calculate the checksum of the filesystem."""
    return sum(i * block for i, block in enumerate(blocks) if block != '.')


disk_map = list(puzzle_input)
files = [disk_map[i] for i in range(len(disk_map)) if (i % 2) == 0]
free_space = [disk_map[i] for i in range(len(disk_map)) if (i % 2) == 1]

decoded_disk_map = []
for i in range(len(files)):

    decoded_disk_map += int(files[i]) * [i]
    try:
        decoded_disk_map += int(free_space[i]) * ["."]
    except IndexError:
        pass

compacted_blocks = move_files(decoded_disk_map)
checksum = calculate_checksum(compacted_blocks)

print("Part 2:", checksum)