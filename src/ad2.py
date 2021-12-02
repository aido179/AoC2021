
with open('src/data/ad2.txt') as file:
    data = file.read().strip().split("\n")

# Part 1
x_pos = 0
y_pos = 0
for dir in data:
    if "up" in dir:
        y_pos -= int(dir.split(" ")[1])
    if "down" in dir:
        y_pos += int(dir.split(" ")[1])
    if "forward" in dir:
        x_pos += int(dir.split(" ")[1])
print("part 1", x_pos, y_pos, x_pos*y_pos)

# Part 2

x_pos = 0
y_pos = 0
aim = 0
for dir in data:
    if "up" in dir:
        aim -= int(dir.split(" ")[1])
    if "down" in dir:
        aim += int(dir.split(" ")[1])
    if "forward" in dir:
        x_pos += int(dir.split(" ")[1])
        y_pos += int(dir.split(" ")[1])*aim
print("part 2", x_pos, y_pos, x_pos*y_pos)
