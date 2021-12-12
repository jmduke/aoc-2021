from collections import defaultdict
from typing import Dict, Iterable, List

Cave = str
Input = List[List[Cave]]
Graph = Dict[Cave, List[Cave]]

def is_small(cave: str) -> bool:
    return cave.lower() == cave

def contains_duplicates(path: List[Cave]) -> bool:
    return len(set(path)) != len(path)

def construct_graph(input: Input) -> Graph:
    graph = defaultdict(list)
    for [a, b] in input:
        graph[a].append(b)
        graph[b].append(a)
    return graph

def potential_paths(path: List[Cave], current: Cave, graph: Graph) -> Iterable[List[Cave]]:
    potential_caves = graph[current]
    for cave in potential_caves:
        if cave == "end":
            yield path + [cave]
        elif is_small(cave):
            if cave not in path:
                yield from potential_paths(path + [cave], cave, graph)
            elif not contains_duplicates([cave for cave in path if is_small(cave)]) and cave not in ("start", "end"):
                yield from potential_paths(path + [cave], cave, graph)
        else:
            yield from potential_paths(path + [cave], cave, graph)

def job(input: Input) -> int:
    graph = construct_graph(input)
    paths = potential_paths(["start"], "start", graph)
    unique_paths = set([
        ",".join(path) for path in paths
    ])
    return len(unique_paths)

def main(filename: str) -> int:
    with open(filename) as f:
        return job([s.strip().split("-") for s in f.readlines()])


print(main('12-0.txt'))
print(main('12-1.txt'))
print(main('12-2.txt'))