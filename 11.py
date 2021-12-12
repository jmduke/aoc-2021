from typing import Iterable, Iterator, List, Optional, Tuple


SIZE = 10

def adjacencies(i: int) -> List[int]:
    return [
        j 
        for j 
        in [
            i - 11 if i % 10 > 0 else None,
            i - 10,
            i - 9 if i % 10 < 9 else None,
            i - 1 if i % 10 > 0 else None,
            i + 1 if i % 10 < 9 else None,
            i + 9 if i % 10 > 0 else None,
            i + 10,
            i + 11 if i % 10 < 9 else None,
        ]
        if j is not None and j >= 0 and j < SIZE * SIZE
    ]


def flatten(l: List[Iterable]) -> List:
    return [item for sublist in l for item in sublist]


def iterate(levels: List[int]) -> List[int]:
    # Initial iteration.
    levels = [l + 1 for l in levels]
    
    # Resolve any flashes.
    while any([l > 9 for l in levels]):
        flashes = [i for i, l in enumerate(levels) if l > 9]
        indices = flatten([adjacencies(flash) for flash in flashes])
        for index in indices:
            levels[index] += 1
        for index in flashes:
            levels[index] = float('-inf')
    
    for i in range(len(levels)):
        if levels[i] == float('-inf'):
            levels[i] = 0
    
    return levels


def job(lines: List[List[int]]) -> int:
    levels = flatten(lines)
    iterations = 0
    number_of_zeroes = 0
    while number_of_zeroes != SIZE * SIZE:
        levels = iterate(levels)
        number_of_zeroes = len([l for l in levels if l == 0])
        iterations += 1
    return iterations

def main(filename: str) -> int:
    with open(filename) as f:
        return job([list(map(int, s.strip())) for s in f.readlines()])


print(main('11-1.txt'))
print(main('11-2.txt'))