from dataclasses import dataclass
from enum import Enum
import io
from turtle import position

directions_in_order = [
    (-1, 0),  # up
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
]


@dataclass
class Guard:
    position: tuple[int, int]
    direction_index: int = 0

    def next_position(self) -> tuple[int, int]:
        x = self.position[0] + directions_in_order[self.direction_index][0]
        y = self.position[1] + directions_in_order[self.direction_index][1]
        return (x, y)

    def move(self):
        self.position = self.next_position()

    def turn(self):
        if self.direction_index == len(directions_in_order) - 1:
            self.direction_index = 0
        else:
            self.direction_index += 1


def guard_is_within_bounds(guard: Guard, max_x: int, max_y: int) -> bool:
    return (
        guard.position[0] >= 0
        and guard.position[1] >= 0
        and guard.position[0] < max_x
        and guard.position[1] < max_y
    )


def get_answer_to_part_1(input_stream: io.StringIO) -> int:
    lines = input_stream.readlines()

    initial_guard_position = None
    obstacles: set[tuple[int, int]] = set()
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "^":
                initial_guard_position = (i, j)
            elif char == "#":
                obstacles.add((i, j))

    if not initial_guard_position:
        raise ValueError("Did not find initial guard position")
    guard = Guard(initial_guard_position)

    positions_covered: set[tuple[int, int]] = set()
    while guard_is_within_bounds(guard, len(lines), len(line)):
        positions_covered.add(guard.position)
        while guard.next_position() in obstacles:
            guard.turn()
        guard.move()

    return len(positions_covered)


def get_answer_to_part_2(input_stream: io.StringIO) -> int:
    pass
