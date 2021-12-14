from typing import List, Dict
from collections import Counter

with open('src/data/ad8.txt') as file:
    data = file.read().strip().split("\n")


lines = (l.split(" | ") for l in data)
# count = 0
# for l in lines:
#     print(l)
#     for digit in l[1].split(' '):
#         print(digit)
#         if len(digit) <=4 or len(digit) ==7:
#             count += 1
# print("part 1", count)

def seg_subtraction(d1, d2):
    s1 = set(d1)
    s2 = set(d2)
    return "".join(s1-s2)


def digit_to_number(known_digits, digit):
    if len(digit) == 2:
        return '1'
    if len(digit) == 4:
        return '4'
    if len(digit) == 3:
        return '7'
    if len(digit) == 7:
        return '8'
    try:
        if len(seg_subtraction(digit, known_digits['1'])) == 3:
            return '3'
        if len(seg_subtraction(digit, known_digits['7'])) == 4:
            return '6'
        if len(seg_subtraction(digit, known_digits['6'])) == 0:
            return '5'
        if len(seg_subtraction(digit, known_digits['5'])) == 1:
            return '9'
        if len(seg_subtraction(digit, known_digits['3'])) == 2:
            return '0'
        if len(seg_subtraction(digit, known_digits['3'])) == 1:
            return '2'
    except KeyError:
        return None
    return None


def convert(line):
    known_digits:Dict[str,str] = dict()
    while len(known_digits) < 10:
        for digit in line[0].split(" "):
            if digit not in known_digits.values():
                n = digit_to_number(known_digits, digit)
                if n:
                    known_digits[n] = "".join(sorted(digit))
    out = ""
    for d in line[1].split(" "):
        d = "".join(sorted(d))
        out += list(known_digits.keys())[list(known_digits.values()).index(d)]

    return out
    # return "".join[known_digits[digit] for digit in line[1].split(" ")]



count = 0
for l in lines:
    count += int(convert(l))
#     for digit in l[1].split(' '):
#         print(digit)
#         if len(digit) <=4 or len(digit) ==7:
#             count += 1
# print("part 1", count)
print("part 2", count)
