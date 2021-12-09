from typing import List

def cost(distance: int) -> int:
    if distance == 0:
        return 0
    return int((distance * (distance + 1)) / 2)

def job(positions: List[int]) -> int:
    return min([
        sum([cost(abs(position - potential_midpoint)) for position in positions])
        for potential_midpoint in range(min(positions), max(positions))
    ])

def main(filename: str) -> int:
    with open(filename) as f:
        raw_positions = f.read().split(",")
        return job([int(position) for position in raw_positions])


print(main('7-1.txt'))
print(main('7-2.txt'))