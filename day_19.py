
def get_result(part_id):
    match part_id:
        case 1: return part_1()
        case 2: return part_2()
        case _: return None


def part_1():
    patterns: set[str] = set()
    pattern_max_length = -1
    designs: [str] = []

    with open('inputs/day_19.txt') as file:
        patterns = set(file.readline().removesuffix('\n').split(', '))
        file.readline()
        designs = list(map(lambda x: x.removesuffix('\n'), file.readlines()))

    for pt in patterns:
        pattern_max_length = max(pattern_max_length, len(pt))

    # Remove redundant patterns
    patterns_revised = set()

    for pt_len in range(1, pattern_max_length):
        patterns_of_length = []
        patterns_not_redundant = set()

        # Gather patterns of specified length
        for pt in patterns:
            if len(pt) == pt_len:
                patterns_of_length.append(pt)

        # Store patterns that aren't redundant
        for pt in patterns_of_length:
            if not check_design(pt, patterns_revised, pt_len - 1):
                patterns_not_redundant.add(pt)

        # Move those not redundant to result set
        for pt in patterns_not_redundant:
            patterns_revised.add(pt)

    for pt in patterns_revised:
        pattern_max_length = max(pattern_max_length, len(pt))

    # Check designs
    possible_designs_count = 0

    for i in range(len(designs)):
        print(str(i) + '/' + str(len(designs) - 1))
        possible_designs_count += 1 if check_design(designs[i], patterns_revised, pattern_max_length) else 0

    return possible_designs_count


def part_2():
    patterns: set[str] = set()
    pattern_max_length = -1
    designs: [str] = []

    with open('inputs/day_19.txt') as file:
        patterns = set(file.readline().removesuffix('\n').split(', '))
        file.readline()
        designs = list(map(lambda x: x.removesuffix('\n'), file.readlines()))

    for pt in patterns:
        pattern_max_length = max(pattern_max_length, len(pt))

    # Remove redundant patterns
    patterns_revised = set()

    for pt_len in range(1, pattern_max_length):
        patterns_of_length = []
        patterns_not_redundant = set()

        # Gather patterns of specified length
        for pt in patterns:
            if len(pt) == pt_len:
                patterns_of_length.append(pt)

        # Store patterns that aren't redundant
        for pt in patterns_of_length:
            if not check_design(pt, patterns_revised, pt_len - 1):
                patterns_not_redundant.add(pt)

        # Move those not redundant to result set
        for pt in patterns_not_redundant:
            patterns_revised.add(pt)

    # Count possible arrangements
    possible_arrangements_count = 0



    # Threw out bwu, check why



    for i in range(len(designs)):
        print(str(i) + '/' + str(len(designs) - 1))
        if check_design(designs[i], patterns_revised, pattern_max_length):
            pos_arr = count_possible_arrangements(designs[i], patterns)
            possible_arrangements_count += pos_arr
            print(str(pos_arr))
            print()

    return possible_arrangements_count


def check_design(design: str, patterns: set[str], pattern_max_length: int):
    # checks designs from start_index (if none can fit, return false)
    # end index points outside the checked substring (start_index for next one)

    if design == '':
        return True

    design_possible = False

    for end_index in range(pattern_max_length, -1, -1):
        print(str(design[:end_index]), end='')
        if design[:end_index] in patterns:
            print(' found in ', end='')
            print(patterns)
            if check_design(design[end_index:], patterns, pattern_max_length):
                design_possible = True
                break
        print(' not found in ', end='')
        print(patterns)

    return design_possible


def count_possible_arrangements(design: str, patterns: set[str]):
    # Only called on those with possible arrangements
    # Check if a pattern is a prefix, if so, then
    #   call function with design without prefix
    # If design len = 0, return 0
    # Add up all possible arrangements

    # print(design)

    if len(design) == 0:
        return 1

    arrangements = 0

    for pt in patterns:
        if (new_design := design.removeprefix(pt)) != design:
            arrangements += count_possible_arrangements(new_design, patterns)

    return arrangements
