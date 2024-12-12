
def get_result(part_id):
    match part_id:
        case 1: return part_1()
        case 2: return part_2()
        case _: return None


def part_1():
    plot_map: [[str]] = []
    visited_mask: [[bool]] = []
    fence_cost_sum = 0

    with open('inputs/day_12.txt') as file:
        for line in file:
            line = line.replace('\n', '')
            plot_map.append(list(line))
            visited_mask.append([False for v in range(len(line))])

    for y in range(len(plot_map)):
        for x in range(len(plot_map[0])):
            if not visited_mask[y][x]:
                (perimeter, area) = calc_fence_cost(plot_map, y, x, visited_mask)
                # print(f'{plot_map[y][x]} {perimeter} {area}')
                fence_cost_sum += perimeter * area

    return fence_cost_sum


def part_2():
    plot_map: [[str]] = []
    visited_mask: [[bool]] = []
    fence_cost_sum = 0

    with open('inputs/day_12.txt') as file:
        for line in file:
            line = line.replace('\n', '')
            plot_map.append(list(line))
            visited_mask.append([False for v in range(len(line))])

    for y in range(len(plot_map)):
        for x in range(len(plot_map[0])):
            if not visited_mask[y][x]:
                # print(plot_map[y][x])
                area_mask: [[bool]] = [[False for x in range(len(plot_map[0]))] for y in range(len(plot_map))]
                area = calc_area(plot_map, y, x, visited_mask, area_mask)
                sides = count_sides(plot_map, area_mask)
                fence_cost_sum += area * sides
                # print(f'area:{area} sides:{sides} cost:{fence_cost_sum}\n')

    return fence_cost_sum


def calc_fence_cost(plot_map, y, x, visited_mask) -> (int, int):
    if visited_mask[y][x]:
        return 0, 0

    visited_mask[y][x] = True
    this_perimeter = 0
    this_area = 1

    if y - 1 >= 0 and plot_map[y - 1][x] == plot_map[y][x]:
        (perimeter, area) = calc_fence_cost(plot_map, y - 1, x, visited_mask)
        this_perimeter += perimeter
        this_area += area
    else:
        this_perimeter += 1

    if x - 1 >= 0 and plot_map[y][x - 1] == plot_map[y][x]:
        (perimeter, area) = calc_fence_cost(plot_map, y, x - 1, visited_mask)
        this_perimeter += perimeter
        this_area += area
    else:
        this_perimeter += 1

    if y + 1 < len(plot_map) and plot_map[y + 1][x] == plot_map[y][x]:
        (perimeter, area) = calc_fence_cost(plot_map, y + 1, x, visited_mask)
        this_perimeter += perimeter
        this_area += area
    else:
        this_perimeter += 1

    if x + 1 < len(plot_map[0]) and plot_map[y][x + 1] == plot_map[y][x]:
        (perimeter, area) = calc_fence_cost(plot_map, y, x + 1, visited_mask)
        this_perimeter += perimeter
        this_area += area
    else:
        this_perimeter += 1

    return this_perimeter, this_area


def calc_area(plot_map, y, x, visited_mask, area_mask):
    if visited_mask[y][x]:
        return 0

    visited_mask[y][x] = True
    area_mask[y][x] = True
    area = 1

    if y - 1 >= 0 and plot_map[y - 1][x] == plot_map[y][x]:
        area += calc_area(plot_map, y - 1, x, visited_mask, area_mask)

    if x - 1 >= 0 and plot_map[y][x - 1] == plot_map[y][x]:
        area += calc_area(plot_map, y, x - 1, visited_mask, area_mask)

    if y + 1 < len(plot_map) and plot_map[y + 1][x] == plot_map[y][x]:
        area += calc_area(plot_map, y + 1, x, visited_mask, area_mask)

    if x + 1 < len(plot_map[0]) and plot_map[y][x + 1] == plot_map[y][x]:
        area += calc_area(plot_map, y, x + 1, visited_mask, area_mask)

    return area


def count_sides(plot_map, area_mask):
    # counting sides:
    # first I would need area calculated separately and a mask for this set of plots
    # then go from most left part and get a list of all plots on this x
    # the remove all plots with y that appeared on previous list (first empty)
    # the go through this list (should be sorted) and while they differ by 1 on y, just go
    # when difference is bigger or went to the end, add a side and keep going
    # do this for all directions

    # print(area_mask)

    sides = 0

    # borders
    top = len(plot_map)
    left = len(plot_map[0])
    bottom = -1
    right = -1

    for y in range(len(plot_map)):
        for x in range(len(plot_map[0])):
            if area_mask[y][x]:
                if y < top: top = y
                if x < left: left = x
                if y > bottom: bottom = y
                if x > right: right = x

    # print(f'top:{top} left:{left} bottom:{bottom} right{right}')

    prev_line: [(int, int)]
    curr_line: [(int, int)] = []
    curr_line_raw: [(int, int)] = []

    # from left to right
    for x in range(left, right + 1):
        prev_line = curr_line_raw
        curr_line = []
        curr_line_raw = []

        for y in range(top, bottom + 1):
            if area_mask[y][x]:
                curr_line_raw.append((y, x))

        if len(prev_line) > 0:
            for curr_tuple_raw in curr_line_raw:
                found = False
                for prev_tuple in prev_line:
                    if curr_tuple_raw[0] == prev_tuple[0]:
                        found = True
                        break
                if not found:
                    curr_line.append(curr_tuple_raw)
        else:
            curr_line = curr_line_raw

        if len(curr_line) == 1:
            sides += 1
        elif len(curr_line) > 1:
            for curr_line_id in range(1, len(curr_line)):
                if curr_line[curr_line_id][0] - curr_line[curr_line_id - 1][0] != 1:
                    sides += 1
            sides += 1
    # print(sides)

    curr_line_raw = []

    # from right to left
    for x in range(right, left - 1, -1):
        prev_line = curr_line_raw
        curr_line = []
        curr_line_raw = []

        for y in range(top, bottom + 1):
            if area_mask[y][x]:
                curr_line_raw.append((y, x))

        if len(prev_line) > 0:
            for curr_tuple_raw in curr_line_raw:
                found = False
                for prev_tuple in prev_line:
                    if curr_tuple_raw[0] == prev_tuple[0]:
                        found = True
                        break
                if not found:
                    curr_line.append(curr_tuple_raw)
        else:
            curr_line = curr_line_raw

        if len(curr_line) == 1:
            sides += 1
        elif len(curr_line) > 1:
            for curr_line_id in range(1, len(curr_line)):
                if curr_line[curr_line_id][0] - curr_line[curr_line_id - 1][0] != 1:
                    sides += 1
            sides += 1
    # print(sides)

    curr_line_raw = []

    # top to bottom
    for y in range(top, bottom + 1):
        prev_line = curr_line_raw
        curr_line = []
        curr_line_raw = []

        for x in range(left, right + 1):
            if area_mask[y][x]:
                curr_line_raw.append((y, x))

        if len(prev_line) > 0:
            for curr_tuple_raw in curr_line_raw:
                found = False
                for prev_tuple in prev_line:
                    if curr_tuple_raw[1] == prev_tuple[1]:
                        found = True
                        break
                if not found:
                    curr_line.append(curr_tuple_raw)
        else:
            curr_line = curr_line_raw

        if len(curr_line) == 1:
            sides += 1
        elif len(curr_line) > 1:
            for curr_line_id in range(1, len(curr_line)):
                if curr_line[curr_line_id][1] - curr_line[curr_line_id - 1][1] != 1:
                    sides += 1
            sides += 1
    # print(sides)

    curr_line_raw = []

    # bottom to top
    for y in range(bottom, top - 1, -1):
        prev_line = curr_line_raw
        curr_line = []
        curr_line_raw = []

        for x in range(left, right + 1):
            if area_mask[y][x]:
                curr_line_raw.append((y, x))

        if len(prev_line) > 0:
            for curr_tuple_raw in curr_line_raw:
                found = False
                for prev_tuple in prev_line:
                    if curr_tuple_raw[1] == prev_tuple[1]:
                        found = True
                        break
                if not found:
                    curr_line.append(curr_tuple_raw)
        else:
            curr_line = curr_line_raw

        if len(curr_line) == 1:
            sides += 1
        elif len(curr_line) > 1:
            for curr_line_id in range(1, len(curr_line)):
                if curr_line[curr_line_id][1] - curr_line[curr_line_id - 1][1] != 1:
                    sides += 1
            sides += 1
    # print(sides)

    return sides
