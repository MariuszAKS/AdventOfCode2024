
def get_result(part_id):
    match part_id:
        case 1: return part_1()
        case 2: return part_2()
        case _: return None


def part_1():
    warehouse_map: [[str]] = []
    robot_pos: [int] = [-1, -1]

    moves: [str] = []

    with open('inputs/day_15.txt') as file:
        row = 0
        while (line := file.readline()) != '\n':
            if (robot_col := line.find('@')) != -1:
                robot_pos = [row, robot_col]

            warehouse_map.append(list(line.replace('\n', '').replace('@', '.')))
            row += 1

        for line in file:
            moves.extend(list(line.replace('\n', '')))

    for move in moves:
        direction = [0, 0]

        match move:
            case '<': direction = [0, -1]
            case '>': direction = [0, 1]
            case '^': direction = [-1, 0]
            case 'v': direction = [1, 0]

        check_pos = [robot_pos[0] + direction[0], robot_pos[1] + direction[1]]

        if warehouse_map[check_pos[0]][check_pos[1]] == '#':
            pass
        elif warehouse_map[check_pos[0]][check_pos[1]] == '.':
            robot_pos = check_pos
        else:
            if try_push_crates(warehouse_map, check_pos, direction):
                robot_pos = [check_pos[0], check_pos[1]]

    print(robot_pos)
    for row in warehouse_map:
        print(''.join(row))

    gps_sum = 0

    for row in range(len(warehouse_map)):
        for col in range(len(warehouse_map[0])):
            if warehouse_map[row][col] == 'O':
                gps_sum += 100 * row + col

    return gps_sum


def part_2():
    warehouse_map: [[str]] = []
    robot_pos: [int] = [-1, -1]

    moves: [str] = []

    with open('inputs/day_15.txt') as file:
        row = 0
        while (line := file.readline()) != '\n':
            if (robot_col := line.find('@')) != -1:
                robot_pos = [row, robot_col * 2]

            line = line.replace('\n', '').replace('@', '.')
            line = line.replace('#', '__').replace('_', '#')
            line = line.replace('.', '__').replace('_', '.')
            line = line.replace('O', '[]')

            warehouse_map.append(list(line))
            row += 1

        for line in file:
            moves.extend(list(line.replace('\n', '')))

    # print(robot_pos)

    for move in moves:
        direction = [0, 0]

        match move:
            case '<':
                direction = [0, -1]
            case '>':
                direction = [0, 1]
            case '^':
                direction = [-1, 0]
            case 'v':
                direction = [1, 0]

        check_pos = [robot_pos[0] + direction[0], robot_pos[1] + direction[1]]

        if warehouse_map[check_pos[0]][check_pos[1]] == '#':
            pass
        elif warehouse_map[check_pos[0]][check_pos[1]] == '.':
            robot_pos = check_pos
        else:
            if direction[0] == 0:
                if try_push_crates_horizontally(warehouse_map, check_pos, direction[1]):
                    robot_pos = check_pos
            else:
                if warehouse_map[check_pos[0]][check_pos[1]] == '[':
                    if try_push_crates_vertically(warehouse_map, [check_pos], direction[0]):
                        robot_pos = check_pos
                else:
                    if try_push_crates_vertically(warehouse_map, [[check_pos[0], check_pos[1] - 1]], direction[0]):
                        robot_pos = check_pos

        # for row in warehouse_map:
        #     print(''.join(row))
        # print(f'{move} {robot_pos}')
        # print('\n')

    gps_sum = 0

    for row in range(len(warehouse_map)):
        for col in range(len(warehouse_map[0])):
            if warehouse_map[row][col] == '[':
                gps_sum += 100 * row + col

    return gps_sum # 1609139 - too high


def try_push_crates(warehouse_map, position, direction):
    if warehouse_map[position[0]][position[1]] == '#':
        return False
    elif warehouse_map[position[0]][position[1]] == '.':
        return True

    new_position = [position[0] + direction[0], position[1] + direction[1]]
    can_push = try_push_crates(warehouse_map, new_position, direction)

    if can_push:
        warehouse_map[position[0] + direction[0]][position[1] + direction[1]] = 'O'
        warehouse_map[position[0]][position[1]] = '.'

    return can_push


def try_push_crates_horizontally(warehouse_map, position, direction):
    if warehouse_map[position[0]][position[1]] == '#':
        return False
    elif warehouse_map[position[0]][position[1]] == '.':
        return True

    new_position = [position[0], position[1] + direction]
    can_push = try_push_crates_horizontally(warehouse_map, new_position, direction)

    if can_push:
        warehouse_map[new_position[0]][new_position[1]] = warehouse_map[position[0]][position[1]]
        warehouse_map[position[0]][position[1]] = '.'

    return can_push


def try_push_crates_vertically(warehouse_map, crate_left_positions, direction):
    if len(crate_left_positions) == 0:
        return True

    can_push = True
    new_crate_left_positions = []

    for left_pos in crate_left_positions:
        check_space = warehouse_map[left_pos[0] + direction][left_pos[1]]

        if check_space == '#':
            can_push = False
            break
        elif check_space == '[':
            new_crate_left_positions.append([left_pos[0] + direction, left_pos[1]])
        elif check_space == ']':
            new_crate_left_positions.append([left_pos[0] + direction, left_pos[1] - 1])

        check_space = warehouse_map[left_pos[0] + direction][left_pos[1] + 1]

        if check_space == '#':
            can_push = False
            break
        elif check_space == '[':
            new_crate_left_positions.append([left_pos[0] + direction, left_pos[1] + 1])

    if can_push and (can_push := try_push_crates_vertically(warehouse_map, new_crate_left_positions, direction)):
        for left_pos in crate_left_positions:
            warehouse_map[left_pos[0]][left_pos[1]] = '.'
            warehouse_map[left_pos[0]][left_pos[1] + 1] = '.'
            warehouse_map[left_pos[0] + direction][left_pos[1]] = '['
            warehouse_map[left_pos[0] + direction][left_pos[1] + 1] = ']'

    return can_push
