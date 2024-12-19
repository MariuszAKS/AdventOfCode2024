from Lib import queue as q

# up right(east) down left (clockwise +1, counter -1)
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
score_additions = [1, 1001, 2001, 1001]

maze_score: [[int]] = []
maze_walk: [[bool]] = []
maze_dir_id: [[int]] = []
path_tiles: [[int]] = []
start: [int] = []
end: [int] = []
best_end_score: int = -1

bfs_queue = q.Queue()


def get_result(part_id):
    match part_id:
        case 1: return part_1()
        case 2: return part_2()
        case _: return None


def part_1():
    with open('inputs/day_16.txt') as file:
        y = 0
        for line in file:
            line = line.replace('\n', '')
            maze_score.append([-1 for _ in range(len(line))])
            maze_dir_id.append([-1 for _ in range(len(line))])

            if (x := line.find('S')) != -1:
                global start
                start = [y, x]
                maze_score[y][x] = 0
                maze_dir_id[y][x] = 1
            if (x := line.find('E')) != -1:
                global end
                end = [y, x]

            maze_walk.append([True for _ in range(len(line))])
            for x in range(len(line)):
                if line[x] == '#':
                    maze_walk[y][x] = False

            y += 1

    bfs_queue.put(start)
    while not bfs_queue.empty():
        part_1_bfs()

    for row in maze_score:
        for c in row:
            print(str(c).ljust(5, ' '), end=' ')
        print('\n')

    return maze_score[end[0]][end[1]]


def part_2():
    with open('inputs/day_16.txt') as file:
        y = 0
        for line in file:
            line = line.replace('\n', '')
            maze_score.append([-1 for _ in range(len(line))])
            maze_dir_id.append([-1 for _ in range(len(line))])

            if (x := line.find('S')) != -1:
                global start
                start = [y, x]
                maze_score[y][x] = 0
                maze_dir_id[y][x] = 1
            if (x := line.find('E')) != -1:
                global end
                end = [y, x]

            maze_walk.append([True for _ in range(len(line))])
            for x in range(len(line)):
                if line[x] == '#':
                    maze_walk[y][x] = False

            y += 1
        global path_tiles
        path_tiles = []

    bfs_queue.put(start)
    while not bfs_queue.empty():
        part_1_bfs()

    global best_end_score
    best_end_score = maze_score[end[0]][end[1]]

    recursive_traverse([start], start, 0, 1)

    return len(path_tiles) + 1


def recursive_traverse(current_path, current_position, current_score, current_direction_id):
    # It will recursively walk through maze, adding tiles that are on paths resulting in best result
    # current_path - path that it already took
    # current position - position in the maze (tile coords)
    # current_score - score to be at current_position
    # current_direction - direction in which we were facing when entering current tile (id)

    # if current_position = end
    #   return current_score = end_best_score

    # result = False
    # for each direction (directions[+i] % 4) try to go
    # if new_position walkable and (maze_score = -1 or new_score < maze_score)
    #   then result = result or traverse(new_position, new_score, new_direction)
    #   if result true, on best path, so add current tile to path (if not already there)

    # return result
    # if any way there was a valid path, it will be True

    if current_position == end:
        return current_score == maze_score[end[0]][end[1]]

    part_of_valid_path = False

    for i in range(4):
        if i == 2:
            continue

        new_direction_id = (current_direction_id + i) % 4
        new_position = [
            current_position[0] + directions[new_direction_id][0],
            current_position[1] + directions[new_direction_id][1]
        ]
        new_score = current_score + score_additions[i]

        if maze_walk[new_position[0]][new_position[1]] and new_position not in current_path:
            current_path.append(new_position)
            traverse_result = recursive_traverse(current_path, new_position, new_score, new_direction_id)
            current_path.pop()

            part_of_valid_path = part_of_valid_path or traverse_result

            if traverse_result and current_position not in path_tiles:
                path_tiles.append(current_position)

    return part_of_valid_path


def part_1_bfs():
    # BFS
    # queue for storing next to check positions
    # when going to position, add all possible next positions to queue
    # do this based on this position value and values of next ones

    # if next one -1 => not visited, so add, if next < next from here, also add
    # check all directions
    # if wall, don't
    # else if score -1, add to queue
    #       if score > new_score, add to queue

    pos = bfs_queue.get()
    pos_score = maze_score[pos[0]][pos[1]]

    if pos == end:
        return

    direction_id = maze_dir_id[pos[0]][pos[1]]

    for i in range(4):
        if i == 2:
            continue

        new_direction_id = (direction_id + i) % 4
        direction = directions[new_direction_id]
        new_pos = [pos[0] + direction[0], pos[1] + direction[1]]

        if maze_walk[new_pos[0]][new_pos[1]]:
            old_score = maze_score[new_pos[0]][new_pos[1]]
            new_score = pos_score + score_additions[i]

            if old_score == -1 or old_score > new_score:
                maze_score[new_pos[0]][new_pos[1]] = new_score
                maze_dir_id[new_pos[0]][new_pos[1]] = new_direction_id
                bfs_queue.put(new_pos)


# def part_2_follow_best_paths():
#     # could come to this place only from positions with score equal to:
#     # this - 1
#     # this - 1001
#     # this - 2001
#     # possible other edge cases, to be absolutely sure, I'd need directions, but let's try it anyway
#
#     tiles_to_sit = 0
#     pos = bfs_queue.get()
#     t_score = maze_score[pos[0]][pos[1]]
#
#     if pos == start:
#         return 0
#
#     for i in range(4):
#         new_pos = [pos[0] + directions[i][0], pos[1] + directions[i][1]]
#         can_walk = maze_walk[new_pos[0]][new_pos[1]]
#         not_visited = not visited[new_pos[0]][new_pos[1]]
#         score = maze_score[new_pos[0]][new_pos[1]]
#         if can_walk and not_visited and (t_score - 1 == score or t_score - 1001 == score or t_score - 2001 == score):
#             visited[new_pos[0]][new_pos[1]] = True
#             tiles_to_sit += 1
#             bfs_queue.put(new_pos)
#
#     return tiles_to_sit
