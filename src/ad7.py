from typing import List
from collections import Counter

with open('src/data/ad7.txt') as file:
    data = [int(x) for x in file.read().strip().split(",")]

# part 1 is the median
point = sorted(data)[len(data)//2]
p1 = sum([abs(point-i) for i in data])
print("part 1", p1)


# part 2
# Average apparently gets close, but not exact.
# the fuel consumption is a triangle number

def triangleNumberSum(n):
    return (n*(n+1))/2

# brute force it
min_val = sum([triangleNumberSum(abs(0-i)) for i in data])
for i in range(0, max(data)):
    new_min = sum([triangleNumberSum(abs(n-i)) for n in data])
    min_val = min(min_val, new_min)

print("Part 2", min_val)
