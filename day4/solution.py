import io

directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

chars = ["X", "M", "A", "S"]


def get_answer_to_part_1(input_stream: io.StringIO) -> int:
    lines = [l.replace("\n", "") for l in input_stream.readlines()]

    N, K = len(lines), len(lines[0])
    n_xmas = 0
    for i in range(N):
        for j in range(K):
            for d in directions:
                for char_index in range(len(chars)):
                    if i + d[0] * char_index >= N or i + d[0] * char_index < 0:
                        break
                    if j + d[1] * char_index >= K or j + d[1] * char_index < 0:
                        break
                    this_char = lines[i + d[0] * char_index][j + d[1] * char_index]
                    char_to_look_for = chars[char_index]
                    if this_char != char_to_look_for:
                        break
                else:
                    if char_index == len(chars) - 1:
                        # print(f"Found XMAS starting at {i,j}, going {d}")
                        n_xmas += 1
    return n_xmas


def get_answer_to_part_2(input_stream: io.StringIO) -> int:
    pass
