import matplotlib.pyplot as plt
from dataclasses import dataclass
from enum import Enum, auto
import io


class Tile(Enum):
    WALL = auto()
    CRATE = auto()
    AIR = auto()
    SHARK = auto()


def parse_warehouse(warehouse_lines: list[str]) -> list[list[Tile]]:
    warehouse: list[list[Tile]] = []
    for line in warehouse_lines:
        this_line = []
        for char in line:
            match char:
                case "#":
                    this_line.append(Tile.WALL)
                case ".":
                    this_line.append(Tile.AIR)
                case "O":
                    this_line.append(Tile.CRATE)
                case "@":
                    this_line.append(Tile.SHARK)
                case "\n":
                    pass
                case _:
                    raise ValueError(f"Unknown symbol {char}")
        warehouse.append(this_line)
    return warehouse


@dataclass
class Direction:
    x: int
    y: int


def parse_moves(move_lines: list[str]) -> list[Direction]:
    moves: list[Direction] = []
    for line in move_lines:
        for char in line:
            match char:
                case "<":
                    moves.append(Direction(0, -1))
                case "^":
                    moves.append(Direction(-1, 0))
                case ">":
                    moves.append(Direction(0, 1))
                case "v":
                    moves.append(Direction(1, 0))
                case "\n":
                    pass
                case _:
                    raise ValueError(f"Unknown move {char}")
    return moves


@dataclass
class Location:
    x: int
    y: int


def find_shark(warehouse: list[list[Tile]]) -> Location:
    for x in range(len(warehouse)):
        for y in range(len(warehouse[0])):
            if warehouse[x][y] == Tile.SHARK:
                return Location(x, y)
    raise ValueError("Can't find shark")


def get_gps_coordinates(warehouse: list[list[Tile]]) -> int:
    coordinate_sum = 0
    for x, row in enumerate(warehouse):
        for y, tile in enumerate(row):
            if tile == Tile.CRATE:
                coords = 100 * x + y
                coordinate_sum += coords
    return coordinate_sum


def get_answer_to_part_1(input_stream: io.StringIO) -> int:
    lines = input_stream.readlines()
    empty_line = lines.index("\n")
    warehouse_lines = lines[:empty_line]
    move_lines = lines[empty_line + 1 :]

    warehouse = parse_warehouse(warehouse_lines)
    moves = parse_moves(move_lines)

    shark_location = find_shark(warehouse)
    for move in moves:
        end_of_straight = Location(shark_location.x, shark_location.y)
        # plt.imshow([[t.value for t in row] for row in warehouse])
        # plt.show()
        while warehouse[end_of_straight.x][end_of_straight.y] in [Tile.SHARK, Tile.CRATE]:
            end_of_straight.x += move.x
            end_of_straight.y += move.y
        # At this point we're looking at either air or wall
        if warehouse[end_of_straight.x][end_of_straight.y] == Tile.WALL:
            continue

        # Now we have air at the end of a straight, so it can be pushed.
        # That means that everything from the shark location to
        # the end of straight - 1 move moves 1 tile in the location of the move.
        while end_of_straight.x != shark_location.x or end_of_straight.y != shark_location.y:
            warehouse[end_of_straight.x][end_of_straight.y] = warehouse[end_of_straight.x - move.x][
                end_of_straight.y - move.y
            ]
            end_of_straight.x -= move.x
            end_of_straight.y -= move.y

        # Then as we moved the original location of the share becomes air
        warehouse[shark_location.x][shark_location.y] = Tile.AIR

        # And lastly we need to move the pointer to the shark location
        shark_location.x += move.x
        shark_location.y += move.y

    return get_gps_coordinates(warehouse)


def get_answer_to_part_2(input_stream: io.StringIO) -> int:
    pass
