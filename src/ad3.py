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


def O2Filter(datalist:List[str])->str:
    bit_len = len(datalist[0])
    for filter_bit_pos in range(0, bit_len):
        mcb = str(format(get_most_common_bits(datalist), 'b')).zfill(bit_len)
        filter_bit = mcb[filter_bit_pos]
        divisor = 2**(bit_len-filter_bit_pos)
        check_qty = divisor/2
        if int(filter_bit):
            datalist = filter_leave_one(lambda n: (int(n, 2)%divisor)>check_qty, datalist)
        else:
            datalist = filter_leave_one(lambda n: (int(n, 2)%divisor)<=check_qty, datalist)
    return datalist[0]

def CO2Filter(datalist:List[str])->str:
    bit_len = len(datalist[0])
    for filter_bit_pos in range(0, bit_len):
        print("")
        print(bin(get_most_common_bits(datalist)))
        lcb = invert_bits(get_most_common_bits(datalist))
        filter_bit = format(lcb,'b').zfill(bit_len)[filter_bit_pos]
        print(f"lcb: {format(lcb,'b').zfill(bit_len)}[{filter_bit_pos}] = {filter_bit}")
        print(datalist)
        divisor = 2**(bit_len-filter_bit_pos)
        check_qty = divisor/2
        if int(filter_bit):
            datalist = filter_leave_one(lambda n: (int(n, 2)%divisor)>=check_qty, datalist)
        else:
            datalist = filter_leave_one(lambda n: (int(n, 2)%divisor)<check_qty, datalist)
    return datalist[0]

tst = ['00100',
'11110',
'10110',
'10111',
'10101',
'01111',
'00111',
'11100',
'10000',
'11001',
'00010',
'01010']


# res = O2Filter(tst)
# print(res)
res = CO2Filter(tst)
print(res)
