
def get_result(part_id):
    match part_id:
        case 1: return part_1()
        case 2: return part_2()
        case _: return None


def part_1():
    antennas: {str: list[list[int]]} = {}
    antinodes = set()
    map_height = 0
    map_width = 0

    with open('inputs/day_08.txt') as file:
        y = 0

        for line in file:
            line = line.replace('\n', '')

            if map_width == 0:
                map_width = len(line)

            for x in range(len(line)):
                if line[x] != '.':
                    antennas[line[x]] = antennas.get(line[x], [])
                    antennas[line[x]].append([y, x])
            y += 1
        map_height = y

    frequencies = list(antennas.keys())

    for freq in frequencies:
        for i in range(len(antennas[freq])):
            for j in range(i + 1, len(antennas[freq])):
                pos1 = antennas[freq][i]
                pos2 = antennas[freq][j]

                y_shift = pos2[0] - pos1[0]
                x_shift = pos2[1] - pos1[1]

                new_y = pos2[0] + y_shift
                new_x = pos2[1] + x_shift

                if 0 <= new_y < map_height and 0 <= new_x < map_width:
                    antinodes.add((new_y, new_x))

                new_y = pos1[0] - y_shift
                new_x = pos1[1] - x_shift

                if 0 <= new_y < map_height and 0 <= new_x < map_width:
                    antinodes.add((new_y, new_x))

    return len(antinodes)


def part_2():
    antennas: {str: list[list[int]]} = {}
    antinodes = set()
    map_height = 0
    map_width = 0

    with open('inputs/day_08.txt') as file:
        y = 0

        for line in file:
            line = line.replace('\n', '')

            if map_width == 0:
                map_width = len(line)

            for x in range(len(line)):
                if line[x] != '.':
                    antennas[line[x]] = antennas.get(line[x], [])
                    antennas[line[x]].append([y, x])
            y += 1
        map_height = y

    frequencies = list(antennas.keys())

    for freq in frequencies:
        for i in range(len(antennas[freq])):
            for j in range(i + 1, len(antennas[freq])):
                pos1 = antennas[freq][i]
                pos2 = antennas[freq][j]

                y_shift = pos2[0] - pos1[0]
                x_shift = pos2[1] - pos1[1]

                new_y = pos1[0]
                new_x = pos1[1]

                while 0 <= new_y < map_height and 0 <= new_x < map_width:
                    antinodes.add((new_y, new_x))
                    new_y = new_y + y_shift
                    new_x = new_x + x_shift

                new_y = pos1[0] - y_shift
                new_x = pos1[1] - x_shift

                while 0 <= new_y < map_height and 0 <= new_x < map_width:
                    antinodes.add((new_y, new_x))
                    new_y = new_y - y_shift
                    new_x = new_x - x_shift

    return len(antinodes)  # 899 - too low
