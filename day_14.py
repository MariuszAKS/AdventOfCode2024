
def get_result(part_id):
    match part_id:
        case 1: return part_1()
        case 2: return part_2()
        case _: return None


def part_1():
    robots_pos: [[int]] = []
    robots_vel: [[int]] = []
    map_height = 103
    map_width = 101

    with open('inputs/day_14.txt') as file:
        for line in file:
            fragments = line.replace('\n', '').replace('p=', '').replace('v=', '').replace(',', ' ').split(' ')
            robots_pos.append([int(fragments[1]), int(fragments[0])])
            robots_vel.append([int(fragments[3]), int(fragments[2])])

    for sec in range(100):
        for robot_id in range(len(robots_pos)):
            robots_pos[robot_id][0] = (robots_pos[robot_id][0] + robots_vel[robot_id][0]) % map_height
            robots_pos[robot_id][1] = (robots_pos[robot_id][1] + robots_vel[robot_id][1]) % map_width

    # print(robots_pos)

    robots_top_left = 0
    robots_top_right = 0
    robots_bottom_left = 0
    robots_bottom_right = 0

    top_max_y = int(map_height / 2)
    left_max_x = int(map_width / 2)

    for robot in robots_pos:
        if robot[0] < top_max_y:
            if robot[1] < left_max_x:
                robots_top_left += 1
            elif robot[1] > left_max_x:
                robots_top_right += 1
        elif robot[0] > top_max_y:
            if robot[1] < left_max_x:
                robots_bottom_left += 1
            elif robot[1] > left_max_x:
                robots_bottom_right += 1

    # print(robots_top_left)
    # print(robots_top_right)
    # print(robots_bottom_left)
    # print(robots_bottom_right)

    return robots_top_left * robots_top_right * robots_bottom_left * robots_bottom_right


def part_2():
    robots_map: [[str]] = []

    robots_pos: [[int]] = []
    robots_vel: [[int]] = []
    map_height = 103
    map_width = 101

    for _ in range(map_height):
        row = ['.' for _ in range(map_width)]
        robots_map.append(row)

    with open('inputs/day_14.txt') as file:
        for line in file:
            fragments = line.replace('\n', '').replace('p=', '').replace('v=', '').replace(',', ' ').split(' ')
            robots_pos.append([int(fragments[1]), int(fragments[0])])
            robots_vel.append([int(fragments[3]), int(fragments[2])])

    with open('outputs/day_14_2.txt', 'w') as file:
        for sec in range(10000):
            print(sec)
            clear_map(robots_map)

            for robot_id in range(len(robots_pos)):
                robots_pos[robot_id][0] = (robots_pos[robot_id][0] + robots_vel[robot_id][0]) % map_height
                robots_pos[robot_id][1] = (robots_pos[robot_id][1] + robots_vel[robot_id][1]) % map_width
                robots_map[robots_pos[robot_id][0]][robots_pos[robot_id][1]] = 'X'

            print_map_to_file(robots_map, sec, file)

    # print(robots_pos)

    pass


def clear_map(robots_map: [[str]]):
    for y in range(len(robots_map)):
        for x in range(len(robots_map[0])):
            robots_map[y][x] = '.'


def print_map_to_file(robots_map: [[str]], sec, file):
    found_line_of_5 = False
    for row_list in robots_map:
        if ''.join(row_list).find('XXXXX') != -1:
            found_line_of_5 = True
            break

    if found_line_of_5:
        file.write(str(sec + 1) + '\n')

        for y in range(len(robots_map)):
            file.write(''.join(robots_map[y]) + '\n')
        file.write('\n\n')
