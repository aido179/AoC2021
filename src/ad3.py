from typing import List

with open('src/data/ad3.txt') as file:
    data = file.read().strip().split("\n")

def get_most_common_bits(datalist):
    # find most common bits by adding up all bits in each position, and checking if
    # the total is greater than half of the lenth of the data
    totals = [0]*len(datalist[0])
    for line in datalist:
        for pos, ch in enumerate(line):
            totals[pos] += int(ch)
    most_common_bits = list(map(lambda count: int((len(datalist)/2)-count < 0), totals))
    return int("".join(str(i) for i in most_common_bits), 2)

def invert_bits(num:int)->int:
    # invert the bits using a bitwise xor:  bit^1.
    return int(num ^ (2**(len(format(num, 'b'))))-1)

p1_mcb = get_most_common_bits(data)
p1_lcb = invert_bits(p1_mcb)

print("Part 1", p1_mcb*p1_lcb)

# Part 2

def filter_leave_one(call, input_list):
    # I think I'm overcomplicating this...
    l = input_list.copy()
    remove_indexes:List[int] = []
    for i, v in enumerate(l):
        if not call(v) and len(remove_indexes)+1 < len(l):
            remove_indexes.append(i)
    out = []
    for i, v in enumerate(l):
        if i not in remove_indexes:
            out.append(v)
    return out

# reimlementing invert_bits using strings because handling leading 0's is causing issues.
def invert_bits_str(bin:str)->str:
    # invert the bits using str replacements
    return bin.replace("0", "x").replace("1", "0").replace("x", "1")
# poor man's unit tests
# print(invert_bits_str("00000"))
# print(invert_bits_str("11111"))
# print(invert_bits_str("110011"))
# print(invert_bits_str("001100"))

def get_most_common_bits_str(datalist:List[str])->str:
    # find most common bits by adding up all bits in each position, and checking if
    # the total is greater than half of the lenth of the data
    totals = [0]*len(datalist[0])
    for line in datalist:
        for pos, ch in enumerate(line):
            totals[pos] += int(ch)
    most_common_bits = list(map(lambda count: int((len(datalist)/2)-count <= 0), totals))
    return "".join(str(i) for i in most_common_bits)

# compare the new implementations to the old
# mcb_str = get_most_common_bits_str(data)
# lcb_str = invert_bits_str(mcb_str)
# print(p1_mcb, p1_lcb, int(mcb_str, 2), int(lcb_str, 2))

# for posterity, my old version used something like:
# divisor = 2**(bit_len-filter_bit_pos)
# check_qty = divisor/2
# filter_leave_one(lambda n: (int(n, 2)%divisor)>check_qty, datalist)

def O2Filter(datalist:List[str])->str:
    bit_len = len(datalist[0])
    for filter_bit_pos in range(0, bit_len):
        mcb = get_most_common_bits_str(datalist)
        filter_bit = mcb[filter_bit_pos]
        datalist = filter_leave_one(lambda n: n[filter_bit_pos] == filter_bit, datalist)
    return datalist[0]

def CO2Filter(datalist:List[str])->str:
    bit_len = len(datalist[0])
    for filter_bit_pos in range(0, bit_len):
        lcb = invert_bits_str(get_most_common_bits_str(datalist))
        filter_bit = lcb[filter_bit_pos]
        datalist = filter_leave_one(lambda n: n[filter_bit_pos] == filter_bit, datalist)
    return datalist[0]

# tst = ['00100',
# '11110',
# '10110',
# '10111',
# '10101',
# '01111',
# '00111',
# '11100',
# '10000',
# '11001',
# '00010',
# '01010']
#
# res = O2Filter(tst)
# print(res, int(res, 2))
# res = CO2Filter(tst)
# print(res, int(res, 2))

p2_a = int(O2Filter(data), 2)
p2_b = int(CO2Filter(data), 2)
print("Part 2: ", p2_a*p2_b)
