
def get_result(part_id):
    match part_id:
        case 1: return part_1()
        case 2: return part_2()
        case _: return None


def part_1():
    disk_map: [int] = []

    with open('inputs/day_09.txt') as file:
        for c in file.readline().replace('\n', ''):
            disk_map.append(int(c))

    # print(disk_map)

    blocks: [int] = []
    is_file = True
    file_id = 0

    for representation in disk_map:
        if is_file:
            for i in range(representation):
                blocks.append(file_id)
            file_id += 1
        else:
            for i in range(representation):
                blocks.append(-1)
        is_file = not is_file

    # print(blocks)

    left = 0
    right = len(blocks) - 1

    while True:
        while blocks[left] != -1:
            left += 1
        while blocks[right] == -1:
            right -= 1

        if left >= right:
            break

        temp = blocks[left]
        blocks[left] = blocks[right]
        blocks[right] = temp

    # print(blocks)

    checksum = 0

    for i in range(len(blocks)):
        if blocks[i] == -1:
            break

        checksum += i * blocks[i]

    return checksum


def part_2():
    disk_map: [int] = []

    with open('inputs/day_09.txt') as file:
        for c in file.readline().replace('\n', ''):
            disk_map.append(int(c))

    # print(disk_map)

    blocks: [int] = []
    is_file = True
    file_id = 0

    for representation in disk_map:
        if is_file:
            for i in range(representation):
                blocks.append(file_id)
            file_id += 1
        else:
            for i in range(representation):
                blocks.append(-1)
        is_file = not is_file

    # print(blocks)

    file_start_position = len(blocks) - 1

    for file_id in range(blocks[-1], -1, -1):
        print(file_id)
        # find end of file position (right)
        while file_start_position - 1 >= 0 and blocks[file_start_position] != file_id:
            file_start_position -= 1

        # get position of start of file and get length
        file_length = 1
        while file_start_position - 1 >= 0 and blocks[file_start_position - 1] == file_id:
            file_start_position -= 1
            file_length += 1

        # print(f"{file_start_position} {file_length}")

        # look for spaces of at least same length as file (remember index of spaces start
        free_space_start_position = -1
        free_space_length = 0

        while free_space_start_position < len(blocks) and free_space_length < file_length:
            free_space_start_position += 1
            while free_space_start_position < len(blocks) and blocks[free_space_start_position] != -1:
                free_space_start_position += 1

            free_space_length = 1
            free_space_end_position = free_space_start_position
            while free_space_end_position + 1 < len(blocks) and blocks[free_space_end_position + 1] == -1:
                free_space_end_position += 1
                free_space_length += 1

        # print(f"{free_space_start_position} {free_space_length}")

        # move whole file if found such space
        if free_space_start_position < file_start_position and free_space_length >= file_length:
            for i in range(file_length):
                blocks[free_space_start_position + i] = file_id
                blocks[file_start_position + i] = -1

    # print(blocks)

    checksum = 0

    for i in range(len(blocks)):
        if blocks[i] == -1:
            continue

        checksum += i * blocks[i]

    return checksum
