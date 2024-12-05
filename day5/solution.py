from collections import defaultdict
from dataclasses import dataclass
import io


@dataclass
class RuleBook:
    have_to_be_befores: dict[int, set[int]]
    have_to_be_afters: dict[int, set[int]]


def parse_rules(rulebook_lines: list[str]) -> RuleBook:
    rules = RuleBook(defaultdict(set), defaultdict(set))
    for line in rulebook_lines:
        line = line.replace("\n", "").strip()
        b, a = line.split("|")
        before, after = int(b), int(a)
        rules.have_to_be_afters[before].add(after)
        rules.have_to_be_befores[after].add(before)
    return rules


assert parse_rules(["1|2 \n"]) == RuleBook(have_to_be_befores={2: {1}}, have_to_be_afters={1: {2}})


def parse_updates(update_lines: list[str]) -> list[list[int]]:
    updates = []
    for line in update_lines:
        line = line.replace("\n", "")
        updates.append([int(i) for i in line.split(",")])
    return updates


assert parse_updates(["1,2\n"]) == [[1, 2]]


def is_even(num: int) -> bool:
    return num % 2 == 0


assert is_even(14)
assert not is_even(13)


def get_answer_to_part_1(input_stream: io.StringIO) -> int:
    lines = input_stream.readlines()
    index_of_sep = lines.index("\n")
    rulebook_lines = lines[:index_of_sep]
    update_lines = lines[index_of_sep + 1 :]

    rules = parse_rules(rulebook_lines)
    updates = parse_updates(update_lines)

    sum_of_valid_middles = 0
    for update in updates:
        for i in range(len(update)):
            if i == 0:
                before = []
            else:
                before = update[:i]

            if i == len(update):
                after = []
            else:
                after = update[i + 1 :]

            num = update[i]

            if any([a in rules.have_to_be_befores[num] for a in after]) or any(
                [b in rules.have_to_be_afters[num] for b in before]
            ):
                break
        else:
            # is valid
            if is_even(len(update)):
                raise ValueError("Even length array has no middle")
            else:
                middle_index = int(len(update) / 2 - 0.5)
                middle = update[middle_index]
                sum_of_valid_middles += middle

    return sum_of_valid_middles


def get_answer_to_part_2(input_stream: io.StringIO) -> int:
    pass
