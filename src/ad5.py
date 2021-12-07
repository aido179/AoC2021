from typing import List
from collections import defaultdict

with open('src/data/ad5.txt') as file:
    data = file.read().strip().split("\n")

line_segments = []
for line in data:
    [p1, p2] = [list(map(int, p.split(","))) for p in line.split(" -> ")]
    line_segments.append([p1, p2])

def getVHSegmentPoints(seg):
    points = []
    for x in range(min(seg[0][0], seg[1][0]), max(seg[0][0], seg[1][0])+1):
        for y in range(min(seg[0][1], seg[1][1]), max(seg[0][1], seg[1][1])+1):
            points.append((x, y))
    return points

def is_vert_horiz(seg):
    return seg[0][0] == seg[1][0] or seg[0][1] == seg[1][1]

vh_line_segments = list(filter(lambda seg: is_vert_horiz(seg), line_segments))

# count overlapping segments
# use a dict instead of a sparse grid

def constant_factory(value):
    return lambda: 0
p1_grid = defaultdict(constant_factory('<missing>'))
for seg in vh_line_segments:
    for point in getVHSegmentPoints(seg):
        p1_grid[point] += 1


def print_dict_grid(dict_grid):
    for y in range(0, 10):
        line = ""
        for x in range(0, 10):
            line += str(dict_grid[(x, y)])
        print(line)

count = len(list(filter(lambda v: v>=2, p1_grid.values())))
print("part 1:", count)

# part 2

def getDiagSegmentPoints(seg):
    points = []
    seg.sort(key=lambda p: p[0]) # sort points by x
    ydir = 1
    i = 0
    if seg[0][1] > seg[1][1]:
        ydir = -1
        i = seg[1][0] - seg[0][0]
    y = min(seg[0][1], seg[1][1])

    for x in range(seg[0][0], seg[1][0]+1):
        # print(x, y, i, ydir)
        points.append((x, y+i))
        i+=ydir
    return points

d_line_segments = list(filter(lambda seg: not is_vert_horiz(seg), line_segments))

p2_grid = defaultdict(constant_factory('<missing>'))
for seg in d_line_segments:
    for point in getDiagSegmentPoints(seg):
        p2_grid[point] += 1
# # add values from part 1
for k, v in p1_grid.items():
    p2_grid[k] += v

print_dict_grid(p2_grid)
count = len(list(filter(lambda v: v>=2, p2_grid.values())))
print("part 2:", count)
# print(getDiagSegmentPoints([ (0,0),  (4, 4) ]))
# print(getDiagSegmentPoints([ (6, 4),  (2, 0) ]))
# print(getDiagSegmentPoints([ (0, 4),  (4, 0) ]))
# print(getDiagSegmentPoints([ (8,0),  (0,8) ]))
# print(getDiagSegmentPoints([ (6, 4),  (2, 0) ]))
# print(getDiagSegmentPoints([ (0,0),  (8, 8) ]))
# print(getDiagSegmentPoints([ (5, 5),  (8, 2) ]))
