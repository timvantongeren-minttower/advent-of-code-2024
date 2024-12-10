from dataclasses import dataclass
import io

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


@dataclass
class PeakCounter:
    counter: int = 0

    def add(self):
        self.counter += 1


def explore(
    starting_location: tuple[int, int], the_map: list[list[int]], peak_counter: PeakCounter
):
    n, m = len(the_map), len(the_map[0])
    current_height = the_map[starting_location[0]][starting_location[1]]
    for direction in directions:
        next_location = (starting_location[0] + direction[0], starting_location[1] + direction[1])
        if not (0 <= next_location[0] <= n - 1) or not (0 <= next_location[1] <= m - 1):
            continue
        next_height = the_map[next_location[0]][next_location[1]]
        if not (next_height - current_height) == 1:
            continue
        elif next_height == 9:
            peak_counter.add()
            continue
        else:
            explore(next_location, the_map, peak_counter)


def get_answer_to_part_1(input_stream: io.StringIO) -> int:
    lines = input_stream.readlines()
    the_map = [[int(i) for i in line.replace("\n", "")] for line in lines]
    n, m = len(the_map), len(the_map[0])
    trailheads = [(i, j) for i in range(n) for j in range(m) if the_map[i][j] == 0]
    total = 0
    for trailhead in trailheads:
        peak_counter = PeakCounter()
        explore(trailhead, the_map, peak_counter)
        total += peak_counter.counter
        print(trailhead, peak_counter.counter)
    return total


def get_answer_to_part_2(input_stream: io.StringIO) -> int:
    pass
