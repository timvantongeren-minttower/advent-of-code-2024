from dataclasses import dataclass
import io


@dataclass(eq=True, frozen=True)
class Tile:
    x: int
    y: int


@dataclass
class Map:
    walls: set[Tile]
    deer: Tile
    target: Tile


def parse_map(lines: list[str]) -> Map:
    walls = set()
    deer = None
    target = None
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            match char:
                case "#":
                    walls.add(Tile(x, y))
                case "S":
                    deer = Tile(x, y)
                case "E":
                    target = Tile(x, y)

    if deer is None:
        raise ValueError("Couldn't find deer")
    if target is None:
        raise ValueError("Couldn't find target")

    return Map(walls, deer, target)


def get_answer_to_part_1(input_stream: io.StringIO) -> int:
    lines = input_stream.readlines()


def get_answer_to_part_2(input_stream: io.StringIO) -> int:
    pass
