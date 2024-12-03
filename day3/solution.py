import io
import re


def parse_tuple_from_operation(operation: str) -> tuple[int, int]:
    a, b = operation.replace("mul(", "").replace(")", "").split(",")
    return (int(a), int(b))


assert parse_tuple_from_operation("mul(5,64)") == (5, 64)
assert parse_tuple_from_operation("mul(2,4)") == (2, 4)


def parse_mul_instructions_from_line(line: str) -> list[tuple[int, int]]:
    regex_pattern = r"mul\([0-9]*,[0-9]*\)"
    matches = re.findall(regex_pattern, line)
    return [parse_tuple_from_operation(o) for o in matches]


assert parse_mul_instructions_from_line(r"xmul(2,4)%&mu") == [(2, 4)]


def get_answer_to_part_1(input_stream: io.StringIO) -> int:
    lines = input_stream.readlines()
    operations = []
    for line in lines:
        operations.extend(parse_mul_instructions_from_line(line))
    return sum(a * b for a, b in operations)


def get_answer_to_part_2(input_stream: io.StringIO) -> int:
    pass
