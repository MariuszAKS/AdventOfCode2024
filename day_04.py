
def get_result(part_id):
    match part_id:
        case 1: return part_1()
        case 2: return part_2()
        case _: return None


def part_1():
    lines = []

    with open('inputs/day_04.txt') as file:
        for line in file:
            lines.append(line.replace('\n', ''))

    xmax_counter = 0

    # left to right
    for line in lines:
        position = 0
        while (position := line.find('XMAS', position)) != -1:
            xmax_counter += 1
            position += 4

    # right to left
    for line in lines:
        position = 0
        while (position := line.find('SAMX', position)) != -1:
            xmax_counter += 1
            position += 4

    columns = len(lines[0])
    rows = len(lines)

    # top <-> bottom
    for y in range(columns):
        for x in range(rows):
            potential_xmas = ''.join([line[y] for line in lines[x:x+4]])
            if potential_xmas == 'XMAS' or potential_xmas == 'SAMX':
                xmax_counter += 1

    # top-left <-> bottom-right
    for x in range(rows):
        for y in range(columns):
            if x + 3 < rows and y + 3 < columns:
                potential_xmas = lines[x][y]
                for i in range(1, 4):
                    potential_xmas += lines[x + i][y + i]
                if potential_xmas == 'XMAS' or potential_xmas == 'SAMX':
                    xmax_counter += 1

    # bottom-left <-> top-right
    for x in range(rows):
        for y in range(columns):
            if x + 3 < rows and y - 3 >= 0:
                potential_xmas = lines[x][y]
                for i in range(1, 4):
                    potential_xmas += lines[x + i][y - i]
                if potential_xmas == 'XMAS' or potential_xmas == 'SAMX':
                    xmax_counter += 1

    return xmax_counter


def part_2():
    lines = []
    x_max_counter = 0

    with open('inputs/day_04.txt') as file:
        for line in file:
            lines.append(line.replace('\n', ''))

    columns = len(lines[0])
    rows = len(lines)

    for y in range(columns - 2):
        for x in range(rows - 2):
            fragment = []
            for row in range(x, x+3):
                fragment.append(lines[row][y:y+3])
            if check(fragment):
                x_max_counter += 1

    return x_max_counter


def check(fragment):
    # [[_,_,_],[_,_,_][_,_,_]]
    if fragment[1][1] != 'A':
        return False

    if fragment[0][0] == fragment[0][2] == 'M' and fragment[2][0] == fragment[2][2] == 'S':
        return True
    if fragment[0][0] == fragment[0][2] == 'S' and fragment[2][0] == fragment[2][2] == 'M':
        return True

    if fragment[0][0] == fragment[2][0] == 'M' and fragment[0][2] == fragment[2][2] == 'S':
        return True
    if fragment[0][0] == fragment[2][0] == 'S' and fragment[0][2] == fragment[2][2] == 'M':
        return True

    return False
