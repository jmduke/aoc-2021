from typing import List, Tuple


DIRECTION_TO_OPERATOR = {
    "forward": lambda depth, position, aim, distance: (depth + (aim * distance), position + distance, aim),
    "down": lambda depth, position, aim, distance: (depth, position, aim + distance),
    "up": lambda depth, position, aim, distance: (depth, position, aim - distance),
}

def operate(inputs: List[Tuple[str, int]]) -> int:
    depth, position, aim = 0, 0, 0
    for (direction, distance) in inputs:
        depth, position, aim = DIRECTION_TO_OPERATOR[direction](depth, position, aim, distance)
    return abs(depth * position)

def main(filename: str) -> int:
    with open(filename) as f:
        inputs = [line.split() for line in f]
        return operate([(direction, int(distance)) for (direction, distance) in inputs])
    
print(main('2-1.txt'))
print(main('2-2.txt'))