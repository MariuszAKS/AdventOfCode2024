
trail_map: [[int]] = []


def get_result(part_id):
    match part_id:
        case 1: return part_1()
        case 2: return part_2()
        case _: return None


def part_1():
    sum_of_scores = 0

    with open('inputs/day_10.txt') as file:
        for line in file:
            trail_map.append(list(map(int, list(line.replace('\n', '')))))

    map_height = len(trail_map)
    map_width = len(trail_map[0])

    for y in range(map_height):
        for x in range(map_width):
            if trail_map[y][x] == 0:
                end_positions = traverse_map([y, x])
                sum_of_scores += len(end_positions)

    return sum_of_scores


def part_2():
    sum_of_ratings = 0

    with open('inputs/day_10.txt') as file:
        for line in file:
            trail_map.append(list(map(int, list(line.replace('\n', '')))))

    map_height = len(trail_map)
    map_width = len(trail_map[0])

    for y in range(map_height):
        for x in range(map_width):
            if trail_map[y][x] == 0:
                sum_of_ratings += traverse_map2([y, x])

    return sum_of_ratings


def traverse_map(position):
    if trail_map[position[0]][position[1]] == 9:
        return {(position[0], position[1])}

    end_positions = set()

    if position[0] + 1 < len(trail_map) and trail_map[position[0] + 1][position[1]] == trail_map[position[0]][position[1]] + 1:
        end_positions.update(traverse_map([position[0] + 1, position[1]]))
    if position[1] + 1 < len(trail_map[0]) and trail_map[position[0]][position[1] + 1] == trail_map[position[0]][position[1]] + 1:
        end_positions.update(traverse_map([position[0], position[1] + 1]))

    if position[0] - 1 >= 0 and trail_map[position[0] - 1][position[1]] == trail_map[position[0]][position[1]] + 1:
        end_positions.update(traverse_map([position[0] - 1, position[1]]))
    if position[1] - 1 >= 0 and trail_map[position[0]][position[1] - 1] == trail_map[position[0]][position[1]] + 1:
        end_positions.update(traverse_map([position[0], position[1] - 1]))

    return end_positions


def traverse_map2(position):
    if trail_map[position[0]][position[1]] == 9:
        return 1

    rating = 0

    if position[0] + 1 < len(trail_map) and trail_map[position[0] + 1][position[1]] == trail_map[position[0]][position[1]] + 1:
        rating += traverse_map2([position[0] + 1, position[1]])
    if position[1] + 1 < len(trail_map[0]) and trail_map[position[0]][position[1] + 1] == trail_map[position[0]][position[1]] + 1:
        rating += traverse_map2([position[0], position[1] + 1])

    if position[0] - 1 >= 0 and trail_map[position[0] - 1][position[1]] == trail_map[position[0]][position[1]] + 1:
        rating += traverse_map2([position[0] - 1, position[1]])
    if position[1] - 1 >= 0 and trail_map[position[0]][position[1] - 1] == trail_map[position[0]][position[1]] + 1:
        rating += traverse_map2([position[0], position[1] - 1])

    return rating
