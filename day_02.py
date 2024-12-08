
def get_result(part_id):
    match part_id:
        case 1: return part_1()
        case 2: return part_2()
        case _: return None


def part_1():
    safe_reports_count = 0

    with open('inputs/day_02.txt') as file:
        for line in file:
            elements_str = line.split(' ')
            elements = list(map(int, elements_str))

            increasing = elements[0] < elements[1]
            is_safe = True

            for i in range(1, len(elements)):
                if increasing and elements[i - 1] > elements[i]:
                    is_safe = False
                    break
                if not increasing and elements[i - 1] < elements[i]:
                    is_safe = False
                    break
                if abs(elements[i] - elements[i - 1]) not in range(1, 4):
                    is_safe = False
                    break

            if is_safe:
                safe_reports_count += 1

    return safe_reports_count


def part_2():
    safe_reports_count = 0

    with open('inputs/day_02.txt') as file:
        for line in file:
            elements_str = line.split(' ')
            elements = list(map(int, elements_str))

            # element on i position ommited (when -1, none ommited)
            for x in range(-1, len(elements)):
                elements_copy = list(elements.copy())
                elements_copy.pop(x)

                # k is so that when it should be increasing, it will check i-1 > i, but when not, will reverse check
                k = 1 if elements_copy[0] < elements_copy[1] else -1
                is_safe = True

                for i in range(1, len(elements_copy)):
                    wrong_order = k * elements_copy[i - 1] > k * elements_copy[i]
                    too_different = abs(elements_copy[i] - elements_copy[i - 1]) not in range(1, 4)

                    if wrong_order or too_different:
                        is_safe = False
                        break

                if is_safe:
                    safe_reports_count += 1
                    break

    return safe_reports_count
