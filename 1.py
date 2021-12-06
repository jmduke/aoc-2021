# 1.py

from typing import List

def deltas(input: List[int]) -> List[int]:
    return [input[i] - input[i-1] for i in range(1, len(input))]

def collate(input: List[int]) -> List[int]:
    return [input[i] + input[i+1] + input[i+2] for i in range(0, len(input) - 2)]

def main(input: List[int]) -> int:
    return len([d for d in deltas(collate(input)) if d > 0])

def parse_file(filename: str) -> List[int]:
    with open(filename) as f:
        return [int(line.strip()) for line in f]

print(main(parse_file('1-1.txt')))
print(main(parse_file('1-2.txt')))