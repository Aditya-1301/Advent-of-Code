import numpy as np


def read_file(file, mode):
    f = open(file)
    tree_count = 0
    grid = [[char for char in line if char != "\n"] * 120 for line in f]
    i = j = k = 0
    i_j_values = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    if mode == 1:
        while i < len(grid) and j < len(grid[0]):
            if grid[i][j] == "#":
                tree_count += 1
            j += 3
            i += 1
        print(tree_count)
    elif mode == 2:
        trees = []
        while k < len(i_j_values):
            inc_i = i_j_values[k][0]
            inc_j = i_j_values[k][1]
            while i < len(grid) and j < len(grid[0]):
                if grid[i][j] == "#":
                    tree_count += 1
                j += inc_i
                i += inc_j
            trees.append(tree_count)
            tree_count = i = j = 0
            k += 1
        print(trees)
        print(np.prod(trees))


if __name__ == "__main__":
    read_file("input3.txt", 1)
    read_file("input3.txt", 2)
