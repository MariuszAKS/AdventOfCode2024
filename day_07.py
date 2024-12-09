
def get_result(part_id):
    match part_id:
        case 1: return part_1()
        case 2: return part_2()
        case _: return None


def part_1():
    total_calibration_result = 0

    with open('inputs/day_07.txt') as file:
        for line in file:
            separator_position = line.find(':')
            test_result = int(line[:separator_position])
            numbers_list = list(map(int, line[separator_position + 2:].replace('\n', '').split(' ')))

            if can_calculate(numbers_list[0], numbers_list, 1, test_result):
                total_calibration_result += test_result

    return total_calibration_result


def part_2():
    total_calibration_result = 0

    with open('inputs/day_07.txt') as file:
        for line in file:
            separator_position = line.find(':')
            test_result = int(line[:separator_position])
            numbers_list = list(map(int, line[separator_position + 2:].replace('\n', '').split(' ')))

            if can_calculate2(numbers_list[0], numbers_list, 1, test_result):
                total_calibration_result += test_result

    return total_calibration_result  # 20668480737670 - too low


def can_calculate(current_result, numbers_list, i, test_result):
    if i == len(numbers_list):
        return current_result == test_result

    addition = can_calculate(current_result + numbers_list[i], numbers_list, i + 1, test_result)
    multiplication = can_calculate(current_result * numbers_list[i], numbers_list, i + 1, test_result)

    return addition or multiplication


def can_calculate2(current_result, numbers_list, i, test_result):
    if i == len(numbers_list):
        return current_result == test_result

    addition = can_calculate2(current_result + numbers_list[i], numbers_list, i + 1, test_result)
    multiplication = can_calculate2(current_result * numbers_list[i], numbers_list, i + 1, test_result)
    concatenation = can_calculate2(int(str(current_result) + str(numbers_list[i])), numbers_list, i + 1, test_result)

    return addition or multiplication or concatenation
