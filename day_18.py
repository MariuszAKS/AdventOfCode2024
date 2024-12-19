from Lib import queue as q

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def get_result(part_id):
    match part_id:
        case 1: return part_1()
        case 2: return part_2()
        case _: return None


def part_1():
    queue_corrupted: [int, int] = []
    grid_size = 71
    grid_distance_from_start = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    grid_walkable: [[bool]] = [[True for _ in range(grid_size)] for _ in range(grid_size)]
    grid_visited: [[bool]] = [[False for _ in range(grid_size)] for _ in range(grid_size)]
    start_position = [0, 0]
    end_position = [grid_size - 1, grid_size - 1]

    with open('inputs/day_18.txt') as file:
        for line in file:
            queue_corrupted.append(list(map(int, line.split(','))))

    # corrupt tiles on a grid
    for i in range(1024):
        grid_walkable[queue_corrupted[i][1]][queue_corrupted[i][0]] = False

    bfs_queue = [start_position]
    bfs_queue_distance = [0]
    grid_visited[0][0] = True

    while len(bfs_queue) > 0:
        pos = bfs_queue.pop(0)
        distance = bfs_queue_distance.pop(0)

        if pos == end_position:
            if grid_distance_from_start[end_position[0]][end_position[1]] > distance:
                grid_distance_from_start[end_position[0]][end_position[1]] = distance
                continue

        for i in range(4):
            new_pos = [pos[0] + directions[i][0], pos[1] + directions[i][1]]

            if 0 <= new_pos[0] < grid_size and 0 <= new_pos[1] < grid_size:
                walkable = grid_walkable[new_pos[0]][new_pos[1]]
                not_visited = not grid_visited[new_pos[0]][new_pos[1]]

                if walkable and not_visited:
                    grid_visited[new_pos[0]][new_pos[1]] = True
                    grid_distance_from_start[new_pos[0]][new_pos[1]] = distance + 1

                    bfs_queue.append(new_pos)
                    bfs_queue_distance.append(distance + 1)

    for row in grid_distance_from_start:
        for c in row:
            print(str(c).ljust(4, ' '), end='')
        print('')

    return grid_distance_from_start[end_position[0]][end_position[1]]


def part_2():
    queue_corrupted: [int, int] = []
    grid_size = 71

    start_position = [0, 0]
    end_position = [grid_size - 1, grid_size - 1]

    with open('inputs/day_18.txt') as file:
        for line in file:
            queue_corrupted.append(list(map(int, line.split(','))))

    for j in range(2925, len(queue_corrupted)):
        print(j)
        grid_distance_from_start = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        grid_walkable: [[bool]] = [[True for _ in range(grid_size)] for _ in range(grid_size)]
        grid_visited: [[bool]] = [[False for _ in range(grid_size)] for _ in range(grid_size)]

        for i in range(1024):
            grid_walkable[queue_corrupted[i][1]][queue_corrupted[i][0]] = False
        for i in range(1024, j+1):
            grid_walkable[queue_corrupted[i][1]][queue_corrupted[i][0]] = False

        bfs_queue = [start_position]
        bfs_queue_distance = [0]
        grid_visited[0][0] = True

        while len(bfs_queue) > 0:
            pos = bfs_queue.pop(0)
            distance = bfs_queue_distance.pop(0)

            if pos == end_position:
                grid_distance_from_start[end_position[0]][end_position[1]] = distance
                break

            for i in range(4):
                new_pos = [pos[0] + directions[i][0], pos[1] + directions[i][1]]

                if 0 <= new_pos[0] < grid_size and 0 <= new_pos[1] < grid_size:
                    walkable = grid_walkable[new_pos[0]][new_pos[1]]
                    not_visited = not grid_visited[new_pos[0]][new_pos[1]]

                    if walkable and not_visited:
                        grid_visited[new_pos[0]][new_pos[1]] = True
                        grid_distance_from_start[new_pos[0]][new_pos[1]] = distance + 1

                        bfs_queue.append(new_pos)
                        bfs_queue_distance.append(distance + 1)

        if grid_distance_from_start[end_position[0]][end_position[1]] == 0:
            for row in grid_distance_from_start:
                for c in row:
                    print(str(c).ljust(4, ' '), end='')
                print('')
            return queue_corrupted[j]

    return -1

