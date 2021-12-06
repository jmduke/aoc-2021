from typing import List

def is_board_solved(board: List[List[int]], known_numbers: List[int]) -> bool:
    for line in board + list(zip(*board)):
        if all(number in known_numbers for number in line):
            return True
    return False

def flatten(l: List[List[int]]) -> List[int]:
    return [item for sublist in l for item in sublist]

def calculate_board_score(board: List[List[int]], known_numbers) -> int:
    return sum(cell for cell in flatten(board) if cell not in known_numbers) * known_numbers[-1]

def job(numbers: List[int], boards: List[List[List[int]]]) -> int:
    for i in range(len(numbers)):
        known_numbers = numbers[:i]
        if len(boards) == 1:
            [board] = boards
            if is_board_solved(board, known_numbers):
                return calculate_board_score(board, known_numbers)
        else:
            boards = [board for board in boards if not is_board_solved(board, known_numbers)]

def parse_board(board: str) -> List[List[int]]:
    return [list(map(int, row.strip().lstrip().split())) for row in board.split("\n")]

def main(filename: str) -> int:
    with open(filename) as f:
        raw_inputs = f.read().split("\n\n")
        numbers, boards = raw_inputs[0].split(","), raw_inputs[1:]
        return job([int(number) for number in numbers], [parse_board(board) for board in boards])
    
print(main('4-1.txt'))
print(main('4-2.txt'))