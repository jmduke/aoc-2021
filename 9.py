from typing import Iterator, List, Tuple


Point = Tuple[int, int]
Heightmap = List[List[int]]

def adjacencies(heightmap: Heightmap, point: Point) -> Iterator[Point]:
    (x, y) = point
    if x > 0:
        yield (x - 1, y)
    if x < len(heightmap) - 1:
        yield (x + 1, y)
    if y > 0:
        yield (x, y - 1)
    if y < len(heightmap[0]) - 1:
        yield (x, y + 1)


def find_low_points(heightmap: Heightmap) -> Iterator[Point]:
    for x in range(len(heightmap)):
        for y in range(len(heightmap[0])):
            if min(heightmap[x][y] for x, y in adjacencies(heightmap, (x, y))) > heightmap[x][y]:
                yield (x, y)


def calculate_basin(heightmap: Heightmap, point: Point) -> int:
    points_in_basin = [point]
    points_to_evaluate = [point]
    while points_to_evaluate:
        p = points_to_evaluate.pop()
        current_height = heightmap[p[0]][p[1]]
        for adj in adjacencies(heightmap, p):
            height = heightmap[adj[0]][adj[1]]
            if adj not in points_in_basin and height > current_height and height < 9:
                points_in_basin.append(adj)
                points_to_evaluate.append(adj)
    return len(points_in_basin)

def job(heightmap: Heightmap) -> int:
    low_points = find_low_points(heightmap)
    basins = sorted([
        calculate_basin(heightmap, point)
        for point in low_points
    ], reverse=True)
    return basins[0] * basins[1] * basins[2]

def main(filename: str) -> int:
    with open(filename) as f:
        heightmap = [list(map(int, s.strip())) for s in f.readlines()]
        return job(heightmap)


print(main('9-1.txt'))
print(main('9-2.txt'))