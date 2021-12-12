from typing import List
from collections import Counter

with open('src/data/ad6.txt') as file:
    data = [int(x) for x in file.read().strip().split(",")]

# print(data)
# print(len(data))

def iterate(fish_list):
    out:List[int] = fish_list.copy()
    new = []
    for i, v in enumerate(fish_list):
        if v == 0:
            out[i] = 6
            new.append(8)
        else:
            out[i] = v-1
    return out+new

# part 1
# for i in range(0,80):
#     data =  iterate(data)
#     print(len(data))
#     count = Counter(data)
#     print([(i, count[i]) for i in sorted(count)], count.total())

def iterate_better(fish_counter):
    new_counter:Counter[int] = fish_counter.copy()
    new_counter[8] = fish_counter[0]
    for i in range(1, 9):
            new_counter[i-1] = fish_counter[i]
    new_counter[6] = new_counter[6] + fish_counter[0]

    return new_counter


# # part 2

count = Counter(data)
for i in range(0,256):
    print(i)
    count =  iterate_better(count)
    print([count[i] for i in sorted(count)], count.total())

print(count.total())
