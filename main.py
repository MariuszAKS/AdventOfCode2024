import day_01
import day_02
import day_03
import day_04
import day_05
import day_06
import day_07
import day_08
import day_09
# import day_10
# import day_12
# import day_13
# import day_14
# import day_15
# import day_16
# import day_17
# import day_18
# import day_19
# import day_20
# import day_21
# import day_22
# import day_23
# import day_24
# import day_25


def get_result(day_id, part_id):
    match day_id:
        case 1: return day_01.get_result(part_id)
        case 2: return day_02.get_result(part_id)
        case 3: return day_03.get_result(part_id)
        case 4: return day_04.get_result(part_id)
        case 5: return day_05.get_result(part_id)
        case 6: return day_06.get_result(part_id)
        case 7: return day_07.get_result(part_id)
        case 8: return day_08.get_result(part_id)
        case 9: return day_09.get_result(part_id)
        # case 10: return day_10.get_result(part_id)
        # case 11: return day_11.get_result(part_id)
        # case 12: return day_12.get_result(part_id)
        # case 13: return day_13.get_result(part_id)
        # case 14: return day_14.get_result(part_id)
        # case 15: return day_15.get_result(part_id)
        # case 16: return day_16.get_result(part_id)
        # case 17: return day_17.get_result(part_id)
        # case 18: return day_18.get_result(part_id)
        # case 19: return day_19.get_result(part_id)
        # case 20: return day_20.get_result(part_id)
        # case 21: return day_21.get_result(part_id)
        # case 22: return day_22.get_result(part_id)
        # case 23: return day_23.get_result(part_id)
        # case 24: return day_24.get_result(part_id)
        # case 25: return day_25.get_result(part_id)
        case _: return None


if __name__ == '__main__':
    day = 8
    part = 2
    print(f'Result for day {day} part {part}: {get_result(day, part)}')
