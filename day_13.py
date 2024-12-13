
BIG = 10000000000000


def get_result(part_id):
    match part_id:
        case 1: return part_1()
        case 2: return part_2()
        case _: return None


def part_1():
    prize_pos: [[int]] = []
    a_shift: [[int]] = []
    b_shift: [[int]] = []
    # [y, x]
    a_cost = 3
    b_cost = 1

    # max_total_prizes = 0
    min_total_tokens = 0

    with open('inputs/day_13.txt') as file:
        for line in file:
            a_shift.append([
                int(line.split()[3].replace('Y+', '')),
                int(line.split()[2].replace('X+', '')[:-1])
            ])
            line = file.readline()
            b_shift.append([
                int(line.split()[3].replace('Y+', '')),
                int(line.split()[2].replace('X+', '')[:-1])
            ])
            line = file.readline()
            prize_pos.append([
                int(line.split()[2].replace('Y=', '')),
                int(line.split()[1].replace('X=', '')[:-1])
            ])
            file.readline()

        # print(prize_pos)
        # print(a_shift)
        # print(b_shift)

    # button is pressed max 100 times
    # let's go with y-coord and x will be checked after
    # we could set 100 presses of A button and then decrease until we are below or equal y coord of prize
    # then we set amount of presses of B, so we are on prize y coord
    #   if not gone over, go back to A presses
    #   if 100 presses of B not enough, we can't get prize
    #   if on y coord, see if x aligns
    #       then check if better option (cost) and if so, set as such

    # changed so that b_presses is calculated, and if result is int, combination is possible

    for i in range(len(prize_pos)):
        a_presses = 100
        lowest_cost = 100 * a_cost + 100 * b_cost + 1

        while a_presses >= 0:
            total_a_shift_y = a_presses * a_shift[i][0]
            if total_a_shift_y <= prize_pos[i][0]:
                b_presses = (prize_pos[i][0] - total_a_shift_y) / b_shift[i][0]

                if b_presses == int(b_presses):
                    if prize_pos[i][1] == a_presses * a_shift[i][1] + b_presses * b_shift[i][1]:
                        lowest_cost = min(lowest_cost, a_presses * a_cost + b_presses * b_cost)

            a_presses -= 1

        if lowest_cost != 100 * a_cost + 100 * b_cost + 1:
            min_total_tokens += int(lowest_cost)

    return min_total_tokens


def part_2():
    prize_pos: [[int]] = []
    a_shift: [[int]] = []
    b_shift: [[int]] = []
    # [y, x]
    a_cost = 3
    b_cost = 1

    # max_total_prizes = 0
    min_total_tokens = 0

    with open('inputs/day_13.txt') as file:
        for line in file:
            a_shift.append([
                int(line.split()[3].replace('Y+', '')),
                int(line.split()[2].replace('X+', '')[:-1])
            ])
            line = file.readline()
            b_shift.append([
                int(line.split()[3].replace('Y+', '')),
                int(line.split()[2].replace('X+', '')[:-1])
            ])
            line = file.readline()
            prize_pos.append([
                int(line.split()[2].replace('Y=', '')) + BIG,
                int(line.split()[1].replace('X=', '')[:-1]) + BIG
            ])
            file.readline()

        # print(prize_pos)
        # print(a_shift)
        # print(b_shift)

    # A = a_presses, B = b_presses (variables)
    # [ya, xa] - a_shift, [yb, xb] - b_shift
    # [yp, xp] - prize_pos

    # A * ya + B * yb = yp
    # A * xa + B * xb = xp
    # two variables, two equations => one solution

    # A = (yp - Byb) / ya
    # (yp - Byb)xa / ya + Bxb = xp
    # (yp - Byb)xa / ya + Bxbya / ya = xp
    # (yp - Byb)xa + Bxbya = xpya
    # ypxa - Bybxa + Bxbya = xpya
    # Bxbya - Bybxa + ypxa = xpya
    # B(xbya - ybxa) = xpya - ypxa
    # B = (yaxp - ypxa) / (yaxb - ybxa)
    # A = (yp - Byb) / ya
    #     (yaxb yp - yayb xp) / (yaxb - ybxa)
    # A = (ypxb - ybxp) / (yaxb - ybxa)

    for i in range(len(prize_pos)):
        [yp, xp] = prize_pos[i]
        [ya, xa] = a_shift[i]
        [yb, xb] = b_shift[i]

        a_presses = (yp * xb - yb * xp) / (ya * xb - yb * xa)
        b_presses = (ya * xp - yp * xa) / (ya * xb - yb * xa)

        if a_presses == int(a_presses) and b_presses == int(b_presses):
            min_total_tokens += int(a_presses * a_cost + b_presses * b_cost)

    return min_total_tokens
