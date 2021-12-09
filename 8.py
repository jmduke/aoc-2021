from dataclasses import dataclass
from itertools import permutations
from random import shuffle
from typing import Dict, Iterable, Iterator, List


@dataclass
class Sample:
    signals: List[str]
    output: List[str]


CANONICAL_SEGMENT_TO_DIGIT = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9"
}

SEGMENTS = "abcdefg"

def flatten(l: List[Iterable]) -> List:
    return [item for sublist in l for item in sublist]


def all_potential_mappings() -> Iterator[Dict[str, str]]:
    for permutation in permutations(SEGMENTS):
        yield dict(zip(permutation, SEGMENTS))


def value_for_malformed_digit(mapping: Dict[str, str], digit: str) -> str:
    return CANONICAL_SEGMENT_TO_DIGIT.get("".join(sorted([mapping[segment] for segment in digit])), "")


def find_mapping(signals: List[str]) -> Dict[str, str]:
    for potential_mapping in all_potential_mappings():
        if all(map(lambda signal: value_for_malformed_digit(potential_mapping, signal) != "", signals)):
            return potential_mapping

def score_for_sample(sample: Sample) -> int:
    malformed_digit_to_canonical_digit = find_mapping(sample.signals)
    output = "".join(value_for_malformed_digit(malformed_digit_to_canonical_digit, digit) for digit in sample.output)
    return int(output)

def job(samples: List[Sample]) -> int:
    return sum(score_for_sample(sample) for sample in samples)

def parse_line(line: str) -> Sample:
    return Sample(
        line.split(" | ")[0].split(" "),
        line.split(" | ")[1].strip().split(" ")
    )

def main(filename: str) -> int:
    with open(filename) as f:
        raw_inputs = f.readlines()
        return job(map(parse_line, raw_inputs))


print(main('8-1.txt'))
print(main('8-2.txt'))