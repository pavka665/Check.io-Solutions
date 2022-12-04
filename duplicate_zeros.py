from typing import Iterable


def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    l = []
    for item in donuts:
        if item == 0:
            l.append(item)
            l.append(0)
        else:
            l.append(item)
    return l



print(duplicate_zeros([0, 0, 0, 0]))
print(duplicate_zeros([100, 10, 0, 101, 1000]))