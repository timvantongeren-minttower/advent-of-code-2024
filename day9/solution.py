import io

EMPTY = -1


def get_answer_to_part_1(input_stream: io.StringIO) -> int:
    current_file_id = 0
    filemap = []
    currently_reading_file_block = True
    for char in input_stream.read():
        block_length = int(char)
        if currently_reading_file_block:
            filemap.extend([current_file_id] * block_length)
            current_file_id += 1
            currently_reading_file_block = False
        else:
            filemap.extend([EMPTY] * block_length)
            currently_reading_file_block = True

    N = len(filemap)
    start_index = 0
    end_index = N - 1
    while start_index < end_index:
        start_num = filemap[start_index]
        if start_num != EMPTY:
            start_index += 1
            continue

        end_num = filemap[end_index]
        if end_num == EMPTY:
            end_index -= 1
            continue

        # move
        filemap[start_index] = end_num
        filemap[end_index] = EMPTY

        start_index += 1
        end_index -= 1

    return sum([i * n for i, n in enumerate(filemap) if n != EMPTY])


def get_answer_to_part_2(input_stream: io.StringIO) -> int:
    pass
