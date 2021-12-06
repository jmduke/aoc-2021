from typing import List

def iterate(matrix: List[str], mode, index = 0) -> str:
    if len(matrix) == 1:
        return matrix[0]

    column = [row[index] for row in matrix]
    ones, zeroes = len([c for c in column if c == "1"]), len([c for c in column if c == "0"])
    if mode == "gamma":
        value = "1" if ones >= zeroes else "0"
    else:
        value = "0" if ones >= zeroes else "1"
    return iterate([row for row in matrix if row[index] == value], mode, index + 1)
    

def operate(matrix: List[str]) -> int:
    return int(iterate(matrix, "gamma"), 2) * int(iterate(matrix, "epsilon"), 2)

def main(filename: str) -> int:
    with open(filename) as f:
        matrix = [line.strip() for line in f.readlines()]
        return operate(matrix)
    
print(main('3-1.txt'))
print(main('3-2.txt'))