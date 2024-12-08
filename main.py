import day_01


def get_result(day_id, part_id):
    match day_id:
        case 1: return day_01.get_result(part_id)
        case _: return None


if __name__ == '__main__':
    day = 1
    part = 2
    print(f'Result for day {day} part {part}: {get_result(day, part)}')
