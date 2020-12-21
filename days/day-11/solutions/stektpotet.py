import copy
import sys

from tqdm import tqdm


def board_read():
    b = [[0 if e == '#' else (1 if e == 'L' else 2) for e in f'.{line}.'] for line in sys.stdin.read().split('\n')[:-1]]
    yield [2] * len(b[0])
    for l in b:
        yield l
    yield [2] * len(b[0])

if __name__ == '__main__':
    frame = list(board_read())

    # for row in frame[1:-1]:
    #     for col in row[1:-1]:
    #         print('#' if col == 0 else ('L' if col == 1 else '.'), end='')
    #     print()
    # for i in range(1000):
    #     n_frame = copy.deepcopy(frame)
    #     for y, row in enumerate(frame[1:-1], start=1):
    #         for x, _ in enumerate(row[1:-1], start=1):
    #             if frame[y][x] == 2: # floor
    #                 continue
    #
    #             adj_occ = map(lambda e: e == 0, (*frame[y-1][x-1:x+2], frame[y][x-1], frame[y][x+1],*frame[y+1][x-1:x+2]))
    #             if frame[y][x]: # empty
    #                 if not any(adj_occ):
    #                     n_frame[y][x] = 0
    #                     continue
    #
    #             if sum(adj_occ) >= 4:
    #                 n_frame[y][x] = 1
    #     frame = n_frame
    #
    #     if i % 100 == 0:
    #         count = 0
    #         for row in frame[1:-1]:
    #             for col in row[1:-1]:
    #                 if col == 0:
    #                     count += 1
    #             #     print('#' if col == 0 else ('L' if col == 1 else '.'), end='')
    #             # print()
    #         print(count)
    #

    magic_number = 2183

    for i in tqdm(range(1000)):
        n_frame = copy.deepcopy(frame)
        for y, row in enumerate(frame[1:-1], start=1):
            for x, _ in enumerate(row[1:-1], start=1):
                if frame[y][x] == 2: # floor
                    continue

                adj_empty = [1, 1, 1,
                             1,    1,
                             1, 1, 1]

                for s in range(max(len(frame), len(frame[0]))):
                    if y - s > 0:
                        adj_empty[1] |= frame[y - s][x] != 0
                        if x - s > 0:
                            adj_empty[0] &= frame[y - s][x - s] != 0
                        if x + s < len(frame[0])-1:
                            adj_empty[2] &= frame[y - s][x + s] != 0

                    if x-s > 0:
                        adj_empty[3] &= frame[y][x - s] != 0
                    if x + s < len(frame[0])-1:
                        adj_empty[4] &= frame[y][x + s] != 0

                    if y - s < len(frame) - 1:
                        adj_empty[6] &= frame[y - s][x] != 0
                        if x - s > 0:
                            adj_empty[5] &= frame[y - s][x - s] != 0
                        if x + s < len(frame[0])-1:
                            adj_empty[7] &= frame[y - s][x + s] != 0

                    if sum(adj_empty) <= 4: # at least 4 adjacent are not empty
                        break

                if frame[y][x]: # empty
                    if all(adj_empty):
                        n_frame[y][x] = 0
                        continue

                if sum(adj_empty) <= 4:
                    n_frame[y][x] = 1
        frame = n_frame

        if i % 100 == 0:
            count = 0
            for row in frame[1:-1]:
                for col in row[1:-1]:
                    if col == 0:
                        count += 1
                #     print('#' if col == 0 else ('L' if col == 1 else '.'), end='')
                # print()
            print(count)


import fileinput
import itertools as it  # noqa

from copy import deepcopy


def isvalid(row, col):
    return 0 <= row < ROWS and 0 <= col < COLUMNS


def neighbours1(r, c):
    return [(r - 1, c - 1), (r - 1, c + 1), (r, c - 1), (r + 1, c),
            (r + 1, c + 1), (r + 1, c - 1), (r, c + 1), (r - 1, c)]


def neighbours2(row, col):
    n = []
    for delta_r, delta_c in neighbours1(0, 0):
        for k in it.count(1):
            r = row + k * delta_r
            c = col + k * delta_c
            if isvalid(r, c):
                if data[r][c] != '.':
                    n.append((r, c))
                    break
            else:
                break
    return n


start = [[c for c in l] for l in fileinput.input()]

ROWS, COLUMNS = len(start), len(start[0])

for neighbours, adjecent in [(neighbours1, 4), (neighbours2, 5)]:
    data = start
    for episode in it.count():
        data_ = deepcopy(data)
        for i, row in enumerate(data):
            for j, seat in enumerate(row):
                if seat == 'L' and all(data[x][y] != '#'
                                       for x, y in neighbours(i, j)
                                       if isvalid(x, y)):
                    data_[i][j] = '#'

                elif seat == '#' and sum(data[x][y] == '#'
                                         for x, y in neighbours(i, j)
                                         if isvalid(x, y)) >= adjecent:
                    data_[i][j] = 'L'

        if data == data_:
            print(sum(c == '#' for row in data_ for c in row))
            break

        data = data_
