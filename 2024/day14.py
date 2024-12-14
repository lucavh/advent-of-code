from PIL import Image, ImageDraw

def make_snapshot(coordinates, n, m, i):
    # Create a new white image
    image = Image.new("RGB", (m * 10, n * 10), "white")
    draw = ImageDraw.Draw(image)

    # Draw gridlines
    for x in range(0, m * 10, 10):
        draw.line([(x, 0), (x, n * 10)], fill="white", width=1)
    for y in range(0, n * 10, 10):
        draw.line([(0, y), (m * 10, y)], fill="white", width=1)

    # Draw the coordinates
    for (x, y) in coordinates:
        if x < n and y < m:
            # Highlight the point with a small rectangle or dot
            draw.rectangle([y * 10, x * 10, (y + 1) * 10 - 1, (x + 1) * 10 - 1], fill="red")

    # Save the image file
    image.save(f"2024/day14_2/{i}.png", dpi=(100, 100))

with open("2024/day14.txt", 'r') as file:
    puzzle_input = file.read()

puzzle_input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

rows = 7 # 103
cols = 11 # 101
blinks = 100
robots_p = []
robots_v = []
robots_final = []

for robot in puzzle_input.split("\n"):
    instr = robot.split(" ")

    p = tuple(map(int, instr[0][2:].split(',')))
    v = tuple(map(int, instr[1][2:].split(',')))

    robots_p.append(p)
    robots_v.append(v)

for s in range(10500):
    robots_next = []
    for i in range(len(robots_p)):
        p = robots_p[i]
        v = robots_v[i]
    
        px = p[0] + v[0]
        py = p[1] + v[1] 
    
        if px < 0:
            px = px + cols
        if px >= cols:
            px = px - cols
        
        if py < 0:
            py = py + rows
        if py >= rows:
            py = py - rows
    
        robots_next.append((px, py))

    robots_p = robots_next
    # make_snapshot(robots_p, rows, cols, s)

r_split = int(rows/2)
c_split = int(cols/2)

tlq = [r for r in robots_p if (r[0] < c_split) & (r[1] < r_split)]
trq = [r for r in robots_p if (r[0] > c_split) & (r[1] < r_split)]
blq = [r for r in robots_p if (r[0] < c_split) & (r[1] > r_split)]
brq = [r for r in robots_p if (r[0] > c_split) & (r[1] > r_split)]

print(f"Part 1: {len(tlq)*len(trq)*len(blq)*len(brq)}")
