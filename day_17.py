
register_a = 0
register_b = 0
register_c = 0
program: [] = []


def get_result(part_id):
    match part_id:
        case 1: return part_1()
        case 2: return part_2()
        case _: return None


def part_1():
    global register_a
    global register_b
    global register_c
    global program

    with open('inputs/day_17.txt') as file:
        register_a = int(file.readline().replace('Register A: ', ''))
        register_b = int(file.readline().replace('Register B: ', ''))
        register_c = int(file.readline().replace('Register C: ', ''))
        file.readline()

        program = list(map(int, file.readline().replace('Program: ', '').split(',')))

    # print(register_a)
    # print(register_b)
    # print(register_c)
    # print(program)

    return run_program(0)


def part_2():
    global register_a
    global register_b
    global register_c
    global program

    with open('inputs/day_17.txt') as file:
        register_a = int(file.readline().replace('Register A: ', ''))
        register_b = int(file.readline().replace('Register B: ', ''))
        register_c = int(file.readline().replace('Register C: ', ''))
        file.readline()

        program = list(map(int, file.readline().replace('Program: ', '').split(',')))

    # print(register_a)
    # print(register_b)
    # print(register_c)
    # print(program)

    # goal = str(program).replace(' ', '').removeprefix('[').removesuffix(']')

    for i in range(100):
        if i % 8 == 0:
            print('')

        register_a = i
        print(f'{i}: {run_program(0)}')

    return -1


def run_program(pointer):
    global register_a
    global register_b
    global register_c
    global program

    reg_a = register_a
    reg_b = register_b
    reg_c = register_c

    result = ''

    while pointer < len(program):
        opcode = program[pointer]
        operand_literal = program[pointer + 1]
        operand_combo = get_combo(operand_literal, reg_a, reg_b, reg_c)

        match opcode:
            case 0:
                reg_a = int(reg_a / (2 ** operand_combo))
            case 1:
                reg_b = reg_b ^ operand_literal
            case 2:
                reg_b = operand_combo % 8
            case 3:
                if reg_a != 0:
                    pointer = operand_literal - 2
            case 4:
                reg_b = reg_b ^ reg_c
            case 5:
                result += f'{operand_combo % 8},'
            case 6:
                reg_b = int(reg_a / (2 ** operand_combo))
            case 7:
                reg_c = int(reg_a / (2 ** operand_combo))

        pointer += 2

    return result.removesuffix(',')


def get_combo(operand, reg_a, reg_b, reg_c):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return reg_a
        case 5:
            return reg_b
        case 6:
            return reg_c
        case _:
            print('Error: operand = ' + str(operand))
            return False
