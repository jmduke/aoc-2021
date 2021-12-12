from typing import Iterable, Iterator, List, Optional, Tuple


CHARACTER_TO_SCORE = {
    ")" : 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

OPENER_TO_CLOSER = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
    "<" : ">",
}


def find_completion(line: str) -> str:
    stack = []
    for char in line:
        if char in OPENER_TO_CLOSER.keys():
            stack.append(char)
        elif char in OPENER_TO_CLOSER.values():
            if not stack or OPENER_TO_CLOSER[stack.pop()] != char:
                return ""
    return "".join([OPENER_TO_CLOSER[char] for char in reversed(stack)])


def score(missing_characters: str) -> int:
    s = 0
    for char in missing_characters:
        s *= 5
        s += CHARACTER_TO_SCORE[char]
    return s

def job(lines: Iterable[str]) -> int:
    sorted_scores = [score(find_completion(line)) for line in lines]
    sorted_scores = sorted([score for score in sorted_scores if score])
    return sorted_scores[int(len(sorted_scores) / 2)]


def main(filename: str) -> int:
    with open(filename) as f:
        return job(f.readlines())


print(main('10-1.txt'))
print(main('10-2.txt'))