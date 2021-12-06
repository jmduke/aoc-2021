from dataclasses import dataclass
from typing import Counter, Iterable, List


@dataclass
class Point:
    x: int
    y: int

    def __hash__(self) -> int:
        return f"{self.x},{self.y}".__hash__()


@dataclass
class Line:
    start: Point
    end: Point

    @property
    def diagonal(self) -> bool:
        return not(
            (self.start.x == self.end.x) or (self.start.y == self.end.y)
        )

    def points_covered(self) -> Iterable[Point]:
        tracer = Point(self.start.x, self.start.y)
        distance = (self.end.x - self.start.x, self.end.y - self.start.y)
        while distance[0] != 0 or distance[1] != 0:
            yield tracer
            if distance[0] > 0:
                tracer = Point(tracer.x + 1, tracer.y)
                distance = (distance[0] - 1, distance[1])
            elif distance[0] < 0:
                tracer = Point(tracer.x - 1, tracer.y)
                distance = (distance[0] + 1, distance[1])
            if distance[1] > 0:
                tracer = Point(tracer.x, tracer.y + 1)
                distance = (distance[0], distance[1] - 1)
            elif distance[1] < 0:
                tracer = Point(tracer.x, tracer.y - 1)
                distance = (distance[0], distance[1] + 1)
        yield tracer


def flatten(l: List[Iterable]) -> List:
    return [item for sublist in l for item in sublist]


def job(lines: List[Line]) -> int:
    covered_points = Counter(flatten([line.points_covered() for line in lines]))
    return len([point for point, count in covered_points.items() if count > 1])


def parse_line(line: str) -> Line:
    start, end = line.split(" -> ")
    start_x, start_y = start.split(",")
    end_x, end_y = end.split(",")
    return Line(
        start=Point(int(start_x), int(start_y)),
        end=Point(int(end_x), int(end_y)),
    )

def main(filename: str) -> int:
    with open(filename) as f:
        raw_lines = f.read().split("\n")
        lines = [parse_line(line) for line in raw_lines]
        return job(lines)


print(main('5-1.txt'))
print(main('5-2.txt'))