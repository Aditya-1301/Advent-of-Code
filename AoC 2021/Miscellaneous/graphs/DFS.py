def dfs_recursive(graph, v, visited):
    visited.append(v)
    print(v, end=" ")
    if graph.get(v) is not None:
        for i in graph[v]:
            if i not in visited:
                dfs_recursive(graph, i, visited)


def dfs_iterative(graph, v, visited):
    stack = [v]
    while len(stack):
        s = stack[-1]
        stack.pop()
        if s not in visited:
            print(s, end=" ")
            visited.append(s)

        if graph.get(s):
            for i in graph[s]:
                if i not in visited:
                    stack.append(i)


def bfs_iterative(graph, v, visited):
    queue = [v]
    while len(queue):
        s = queue[0]
        queue.pop(0)
        if s not in visited:
            print(s, end=" ")
            visited.append(s)

        if graph.get(s):
            for i in graph[s]:
                if i not in visited:
                    queue.append(i)


def is_valid(x,y, matrix, visited):
    Rows = len(matrix[0])
    Columns = len(matrix)

    if x < 0 or y < 0 or x >= Rows or y >= Columns or visited[x][y]:
        return False
    return True


def dfs_in_matrix(matrix, x, y, visited):
    stack = [[x,y]]
    dRow = [0, 1, 0, -1]
    dCol = [-1, 0, 1, 0]
    while len(stack):
        current = stack[-1]
        stack.pop()
        row = current[0]
        column = current[1]
        if is_valid(row, column, matrix, visited):
            visited[row][column] = True
            print(matrix[row][column], end=" ")
            for i in range(4):
                adjX = row + dRow[i]
                adjY = column + dCol[i]
                stack.append([adjX,adjY])

if __name__ == "__main__":
    graph = {
        1: [2, 7, 8],
        2: [3, 6],
        3: [4, 5],
        8: [9, 12],
        9: [10, 11]
    }
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    visited_for_matrix = [[False for i in range(len(matrix))] for j in range(len(matrix[0]))]
    # print(graph)
    map = {}
    for i in graph:
        # print(i)
        i_count = map.get(i, 0)
        if i_count == 0:
            map.update({i: 1})
        for j in graph.get(i):
            j_count = map.get(j, 0)
            if j_count == 0:
                map.update({j: 1})
    # print(map)
    print("Size of Graph: ", sum(map.values()))
    dfs_recursive(graph, 1, [])
    print()
    dfs_iterative(graph, 1, [])
    print()
    bfs_iterative(graph, 1, [])
    print()
    dfs_in_matrix(matrix, 0, 0, visited_for_matrix)




# graph2 = {
#         1: [2, 3, 4],
#         2: [1, 5, 6],
#         3: [1, 7, 8],
#         4: [1, 9, 10],
#         5: [2, 11, 12],
#         6: [2, 13, 14],
#         7: [3, 15, 16],
#         8: [3, 17, 18],
#         9: [4, 19, 20],
#         10: [4, 21, 22],
#         11: [5, 23, 24],
#         12: [5, 25, 26],
#         13: [6, 27, 28],
#         14: [6, 29, 30],
#         15: [7, 31, 32],
#         16: [7, 33, 34],
#         17: [8, 35, 36],
#         18: [8, 37, 38],
#         19: [9, 39, 40],
#         20: [9, 41, 42],
#         21: [10, 43, 44],
#         22: [10, 45, 46],
#         23: [11, 47, 48],
#         24: [11, 49, 50],
#         25: [12, 51, 52],
#         26: [12, 53, 54],
#         27: [13, 55, 56],
#         28: [13, 57, 58],
#         29: [14, 59, 60],
#         30: [14, 61, 62],
#         31: [15, 63, 64],
#         32: [15, 65, 66],
#         33: [16, 67, 68],
#         34: [16, 69, 70],
#         35: [17, 71, 72],
#         36: [17, 73, 74],
#         37: [18, 75, 76],
#         38: [18, 77, 78],
#         39: [19, 79, 80],
#         40: [19, 81, 82],
#         41: [20, 83, 84],
#         42: [20, 85, 86],
#         43: [21, 87, 88],
#         44: [21, 89, 90],
#         45: [22, 91, 92],
#         46: [22, 93, 94],
#         47: [23, 95, 96],
#         48: [23, 97, 98],
#         49: [24, 99, 100],
#         50: [24, 101, 102],
#         51: [25, 103, 104],
#         52: [25, 105, 106],
#         53: [26, 107, 108],
#         54: [26, 109, 110],
#         55: [27, 111, 112],
#         56: [27, 113, 114],
#         57: [28, 115, 116]
#     }
