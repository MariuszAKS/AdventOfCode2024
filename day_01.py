
def get_result(part_id):
    match part_id:
        case 1: return part_1()
        case 2: return part_2()
        case _: return None


def part_1():
    with open('inputs/day_01.txt', 'r') as file:
        left_array: list[int] = []
        right_array: list[int] = []
        sum_apart: int = 0

        for line in file:
            elements: list[str] = line.split('   ')
            left_array.append(int(elements[0]))
            right_array.append(int(elements[1]))

        left_array.sort()
        right_array.sort()

        for i in range(len(left_array)):
            sum_apart += abs(left_array[i] - right_array[i])

    return sum_apart


def part_2():
    left_set = set()
    right_counts = {}
    similarity_score = 0

    with open('inputs/day_01.txt', 'r') as file:
        for line in file:
            elements = line.split('   ')
            left = int(elements[0])
            right = int(elements[1])

            left_set.add(left)

            if right in right_counts:
                right_counts[right] += 1
            else:
                right_counts[right] = 1

    for left in left_set:
        if left in right_counts:
            similarity_score += left * right_counts[left]

    return similarity_score
