
def get_result(part_id):
    match part_id:
        case 1: return part_1()
        case 2: return part_2()
        case _: return None


def part_1():
    rules: {int: [int]} = {}
    all_updates_pages: [[int]] = []

    with open('inputs/day_05.txt') as file:
        reading_rules = True

        for line in file:
            if line == '\n':
                reading_rules = False
                continue
            if reading_rules:
                pages = line.replace('\n', '').split('|')

                if int(pages[0]) not in rules:
                    rules[int(pages[0])] = []

                rules[int(pages[0])].append(int(pages[1]))
            else:
                pages = line.replace('\n', '').split(',')
                all_updates_pages.append(list(map(int, pages)))

    sum_of_middle_pages = 0

    for update_pages in all_updates_pages:
        correct_order = True
        middle_page = update_pages[int(len(update_pages) / 2)]

        while len(update_pages) > 1:
            page = update_pages.pop()  # default pop - last element
            # which means last page of update manual
            # using it as key in rules, we get a list of pages that should be after this one
            # if any of pages before popped are in this list, this means wrong order

            if page not in rules:
                continue

            for prev_page in update_pages:
                if prev_page in rules[page]:
                    correct_order = False
                    break

            if not correct_order:
                break

        if correct_order:
            sum_of_middle_pages += middle_page

    return sum_of_middle_pages


def part_2():
    rules: {int: [int]} = {}
    all_updates_pages: [[int]] = []

    with open('inputs/day_05.txt') as file:
        reading_rules = True

        for line in file:
            if line == '\n':
                reading_rules = False
                continue
            if reading_rules:
                pages = line.replace('\n', '').split('|')

                if int(pages[0]) not in rules:
                    rules[int(pages[0])] = []

                rules[int(pages[0])].append(int(pages[1]))
            else:
                pages = line.replace('\n', '').split(',')
                all_updates_pages.append(list(map(int, pages)))

    sum_of_middle_pages = 0

    for update_pages in all_updates_pages:
        correct_order = True
        copy_of_update_pages = update_pages.copy()

        while len(copy_of_update_pages) > 1:
            page = copy_of_update_pages.pop()  # default pop - last element
            # which means last page of update manual
            # using it as key in rules, we get a list of pages that should be after this one
            # if any of pages before popped are in this list, this means wrong order

            if page not in rules:
                continue

            for prev_page in copy_of_update_pages:
                if prev_page in rules[page]:
                    correct_order = False
                    break

            if not correct_order:
                break

        if not correct_order:
            # order them correctly
            # we have rules: [page]: [pages that should be after key]

            for i in range(len(update_pages) - 1):
                for j in range(len(update_pages) - 1):
                    # check if update_pages[j] should be after update_pages[j + 1]
                    if update_pages[j + 1] in rules and update_pages[j] in rules[update_pages[j + 1]]:
                        temp = update_pages[j]
                        update_pages[j] = update_pages[j + 1]
                        update_pages[j + 1] = temp
                        continue
                    # check if update_pages[j + 1] should be before update_pages[j]

            sum_of_middle_pages += update_pages[int(len(update_pages) / 2)]

    return sum_of_middle_pages  # 6237 too high
