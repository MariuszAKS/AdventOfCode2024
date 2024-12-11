
def get_result(part_id):
    match part_id:
        case 1: return part_1()
        case 2: return part_2()
        case _: return None


def part_1():
    stones: [int] = []

    with open('inputs/day_11.txt') as file:
        stones = list(map(int, file.readline().split(' ')))

    # print(stones)

    for blink in range(25):
        for i in range(len(stones) - 1, -1, -1):  # for each stone separate operation, even if they have same number
            if stones[i] == 0:
                stones[i] = 1
                continue

            digits_count = len(str(stones[i]))
            if digits_count % 2 == 0:
                left = int(str(stones[i])[:int(digits_count / 2)])
                right = int(str(stones[i])[int(digits_count / 2):])

                stones[i] = right
                stones.insert(i, left)  # heavy operation
            else:
                stones[i] = 2024 * stones[i]
        # print(f'Blink {blink + 1}: {stones}')
        # print(blink)

    return len(stones)


def part_2():
    stones: dict[int, int] = {}
    new_stones: dict[int, int] = {}
    # instead of list and iterating through it, decided to have dictionaries: {stone_number: stone_count}
    # this way for every stone with same number there is one operation performed, also no inserting

    with open('inputs/day_11.txt') as file:
        input_stones = list(map(int, file.readline().split(' ')))

        for x in input_stones:
            new_stones[x] = stones.get(x, 0) + 1

    # print(new_stones)

    for blink in range(75):
        stones_keys = new_stones.keys()
        stones = new_stones
        new_stones = {}

        for stone_number in stones_keys:
            if stone_number == 0:
                new_stones[1] = new_stones.get(1, 0) + stones[stone_number]
            else:
                str_stone_number = str(stone_number)
                digits_count = len(str_stone_number)

                if digits_count % 2 == 0:
                    left = int(str_stone_number[:int(digits_count / 2)])
                    right = int(str_stone_number[int(digits_count / 2):])

                    new_stones[left] = new_stones.get(left, 0) + stones[stone_number]
                    new_stones[right] = new_stones.get(right, 0) + stones[stone_number]
                else:
                    new_number = stone_number * 2024
                    new_stones[new_number] = new_stones.get(new_number, 0) + stones[stone_number]

        # print(new_stones)
        # print(blink)

    sum_of_stones = 0

    for stone in new_stones:
        sum_of_stones += new_stones[stone]

    return sum_of_stones
