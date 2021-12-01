import itertools
import collections
from typing import Tuple, Generator, List, Any, Deque, Iterable

with open('src/data/ad1.txt') as file:
    data = file.read().strip().split("\n")

# Part 1
print(sum(map(lambda p: p[0]<p[1], itertools.pairwise(data)))+1)

# Part 2

# Version 1 - This works, but it's obviously pretty nasty
def triplewise(iterable:List[Any]) -> Generator[Tuple[int, int, int], None, None]:
    "Return overlapping triplets from an iterable"
    # triplewise('ABCDEFG') -> ABC BCD CDE DEF EFG
    for (a, _), (b, c) in itertools.pairwise(itertools.pairwise(iterable)):
        yield int(a), int(b), int(c)
print("Part 2 (version 1)", sum(map(lambda p: p[0]<p[1], itertools.pairwise(map(lambda t: sum(t), triplewise(data))))))


# Version 2 - This versions should be a lot more readable, testable and composable...
# But to be honest, I only got v1 working after I got this working because I had a stupid off-by-one error above.
def rollingSum(data:Iterable[int], window_len:int) -> Iterable[int]:
    out:List[int] = []
    window:Deque[int] = collections.deque([], window_len)
    for val in [int(v) for v in data]:
        window.append(val)
        # Don't output until the window is full
        if len(window) == window_len:
            out.append(sum(window))
    return out

def countIncreases(data:Iterable[int]) -> int:
    return sum(map(lambda p: p[0]<p[1], itertools.pairwise(data)))


intdata = [int(d) for d in data]
print("Part 2 (version 2)", countIncreases(rollingSum(intdata, 3)))
