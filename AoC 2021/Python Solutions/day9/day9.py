def readFile(file):
    try:
        f = open(file)
        h_matrix = []
        for i in f:
            h_list = []
            for j in i:
                if j != "\n":
                    h_list.append(int(j))
            h_matrix.append(h_list)
        return h_matrix
    except:
        raise FileNotFoundError


def valid_coord(x, y, width, height):
    if 0 <= x < width:
        if 0 <= y < height:
            return True
    return False


def adjPoints(x, y, h_matrix):
    w = len(h_matrix)
    h = len(h_matrix[0])
    if 0 < x < w and 0 < y < h:
        return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    elif y == 0 and 0 < x < w:
        return [(x - 1, y), (x + 1, y), (x, y + 1)]
    elif y == h - 1 and 0 < x < w:
        return [(x - 1, y), (x + 1, y), (x, y - 1)]
    elif x == 0 and 0 < y < h:
        return [(x + 1, y), (x, y - 1), (x, y + 1)]
    elif x == w - 1 and 0 < y < h:
        return [(x - 1, y), (x, y - 1), (x, y + 1)]
    elif x == 0 and y == 0:
        return [(x + 1, y), (x, y + 1)]
    elif x == w - 1 and y == 0:
        return [(x - 1, y), (x, y + 1)]
    elif x == 0 and y == h - 1:
        return [(x + 1, y), (x, y - 1)]
    elif x == w - 1 and y == h - 1:
        return [(x - 1, y), (x, y - 1)]


def low_points_in_matrix(h_matrix):
    width = len(h_matrix)
    height = len(h_matrix[0])
    list_of_lows = []
    for i in range(0, width, 1):
        for j in range(0, height, 1):
            h = h_matrix[i][j]
            adjacent_points = adjPoints(i, j, h_matrix)
            temp = []
            for adjacent_pointX, adjacent_pointY in adjacent_points:
                if valid_coord(adjacent_pointX, adjacent_pointY, width, height):
                    temp.append(h_matrix[adjacent_pointX][adjacent_pointY])
            if all(b > h for b in temp):
                list_of_lows.append(h)
    return list_of_lows


def part1():
    list_of_lows = low_points_in_matrix(h_matrix)
    sum_of_elements = 0
    for lol in list_of_lows:
        sum_of_elements += lol + 1
    print("Sum of all low points in the given Input :", sum_of_elements)


def basin_sizes(score, visited_list, stack, x, y):
    h0 = h_matrix[x][y]
    visited_list.append((x, y))
    adjacent_points = adjPoints(x, y, h_matrix)

    # for (i, j) in adjacent_points:
    #     if valid_coord(i, j , len(h_matrix), len(h_matrix[0])):
    #         if (i, j) not in visited_list and (i,j) not in stack:
    #
    #
    None

def part2():
    list = []
    width = len(h_matrix)
    height = len(h_matrix[0])
    list_of_lows = low_points_in_matrix(h_matrix)
    for i in range(0, width, 1):
        for j in range(0, height, 1):
            if (i, j) in list_of_lows:
                list.append(basin_sizes(1,[],[],i,j))


if __name__ == "__main__":
    h_matrix = readFile("input9.txt")
    low_points_in_matrix(h_matrix)
