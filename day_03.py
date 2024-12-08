
def get_result(part_id):
    match part_id:
        case 1: return part_1()
        case 2: return part_2()
        case _: return None


def part_1():
    sum_of_operations = 0

    with open('inputs/day_03.txt', 'r') as file:
        for line in file:
            position = 0

            while (position := line.find('mul(', position)) != -1:
                position += 4

                if not line[position].isnumeric():
                    continue

                counter = 0
                left = 0

                while counter < 3 and line[position].isnumeric():
                    left = left * 10 + int(line[position])
                    position += 1
                    counter += 1

                if line[position] != ',':
                    continue
                position += 1
                if not line[position].isnumeric():
                    continue

                counter = 0
                right = 0

                while counter < 3 and line[position].isnumeric():
                    right = right * 10 + int(line[position])
                    position += 1
                    counter += 1

                if line[position] != ')':
                    continue
                position += 1

                sum_of_operations += left * right

    return sum_of_operations


def part_2(): # 24341329
    sum_of_operations = 0

    with open('inputs/day_03.txt', 'r') as file:
        accept_mul = True

        for line in file:
            position = 0

            while True:
                position_mul = line.find('mul(', position)
                position_do = line.find('do()', position)
                position_dont = line.find('don\'t()', position)

                if position_mul == -1:
                    break

                if position_do != -1 and position_do < position_mul:
                    accept_mul = True
                    position = position_do + 4
                    continue

                if position_dont != -1 and position_dont < position_mul:
                    accept_mul = False
                    position = position_dont + 7
                    continue

                position = position_mul
                position += 4

                if not accept_mul:
                    continue

                if not line[position].isnumeric():
                    continue

                counter = 0
                left = 0

                while counter < 3 and line[position].isnumeric():
                    left = left * 10 + int(line[position])
                    position += 1
                    counter += 1

                if line[position] != ',':
                    continue
                position += 1
                if not line[position].isnumeric():
                    continue

                counter = 0
                right = 0

                while counter < 3 and line[position].isnumeric():
                    right = right * 10 + int(line[position])
                    position += 1
                    counter += 1

                if line[position] != ')':
                    continue
                position += 1

                sum_of_operations += left * right

    return sum_of_operations
