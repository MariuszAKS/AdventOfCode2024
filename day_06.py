
def get_result(part_id):
    match part_id:
        case 1: return part_1()
        case 2: return part_2()
        case _: return None


def part_1():
    lab_map: [[str]] = []
    guard_position: [int, int] = []

    with open('inputs/day_06.txt') as file:
        y = 0
        for line in file:
            if (x := line.find('^')) != -1:
                guard_position = [y, x]
                line = line.replace('^', '.')

            lab_map.append(list(line.replace('\n', '')))
            y += 1

    if not guard_position:
        return -1

    # ^ - current guard position
    # # - obstructions
    # . - walkable (also X)
    # guard algo: if sth in front, turn right, otherwise forward

    lab_map_height = len(lab_map)
    lab_map_width = len(lab_map[0])

    guard_direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # [y, x]
    guard_direction_id = 0  # 0-up, 1-right, 2-down, 3-left

    distinct_positions_count = 1

    while True:
        y_check = guard_position[0] + guard_direction[guard_direction_id][0]
        x_check = guard_position[1] + guard_direction[guard_direction_id][1]

        if y_check < 0 or y_check > lab_map_height - 1 or x_check < 0 or x_check > lab_map_width - 1:
            break

        is_obstructed = lab_map[y_check][x_check] == '#'
        is_walkable = lab_map[y_check][x_check] == '.' or lab_map[y_check][x_check] == 'X'
        is_new = lab_map[y_check][x_check] == '.'

        if is_obstructed:
            guard_direction_id = (guard_direction_id + 1) % 4
            continue

        if is_walkable:
            guard_position = [
                guard_position[0] + guard_direction[guard_direction_id][0],
                guard_position[1] + guard_direction[guard_direction_id][1]
            ]
            if is_new:
                lab_map[y_check][x_check] = 'X'
                distinct_positions_count += 1

    return distinct_positions_count


def part_2():
    lab_map: [[str]] = []
    start_guard_position: [int, int] = []

    with open('inputs/day_06.txt') as file:
        y = 0
        for line in file:
            if (x := line.find('^')) != -1:
                start_guard_position = [y, x]
                line = line.replace('^', '.')

            lab_map.append(list(line.replace('\n', '')))
            y += 1

    if not start_guard_position:
        return -1

    # ^ - current guard position
    # # - obstructions
    # . - walkable (also X)
    # guard algo: if sth in front, turn right, otherwise forward

    lab_map_height = len(lab_map)
    lab_map_width = len(lab_map[0])

    guard_direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # [y, x]
    # guard_direction_id = 0  # 0-up, 1-right, 2-down, 3-left

    positions_for_obstructions = 0

    for y in range(lab_map_height):
        print(f"{y}/{lab_map_height}")

        for x in range(lab_map_width):
            if lab_map[y][x] == '#' or (y == start_guard_position[0] and x == start_guard_position[1]):
                continue

            guard_position = start_guard_position.copy()
            guard_direction_id = 0

            walked_again_counter = 0
            distinct_visited = 1

            # Placing the obstruction
            lab_map[y][x] = '#'

            while True:
                y_check = guard_position[0] + guard_direction[guard_direction_id][0]
                x_check = guard_position[1] + guard_direction[guard_direction_id][1]

                if y_check < 0 or y_check > lab_map_height - 1 or x_check < 0 or x_check > lab_map_width - 1:
                    break

                is_obstructed = lab_map[y_check][x_check] == '#'
                is_walkable = lab_map[y_check][x_check] == '.' or lab_map[y_check][x_check] == 'X'
                is_new = lab_map[y_check][x_check] == '.'

                if is_obstructed:
                    guard_direction_id = (guard_direction_id + 1) % 4
                    continue

                if is_walkable:
                    guard_position = [
                        guard_position[0] + guard_direction[guard_direction_id][0],
                        guard_position[1] + guard_direction[guard_direction_id][1]
                    ]
                    if is_new:
                        lab_map[y_check][x_check] = 'X'
                        walked_again_counter = 0
                        distinct_visited += 1
                    else:
                        walked_again_counter += 1

                    if walked_again_counter == distinct_visited:
                        break

            if walked_again_counter == distinct_visited:
                positions_for_obstructions += 1

            # Reset the map
            for i in range(len(lab_map)):
                lab_map[i] = list(''.join(lab_map[i]).replace('X', '.'))
            lab_map[y][x] = '.'

    return positions_for_obstructions
