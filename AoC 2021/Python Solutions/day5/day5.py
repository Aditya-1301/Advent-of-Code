def read1(file, flag):
    try:
        f = open(file)
        temp = []
        valves = []
        for f1 in f:
            [head, tail] = f1.split(" -> ")
            [x1, y1] = head.split(",")
            [x2, y2] = tail.split(",")
            y = "".join(str(i) for i in y2 if str(i) != "\n")
            if x1 == x2 or y1 == y:
                temp.append(str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y))
        for i in temp:
            temp = i.split(",")
            valves.append([int(j) for j in temp])
        return valves
    except:
        raise FileNotFoundError

def read2(file):
    try:
        f = open(file)
        temp = []
        valves = []
        for f1 in f:
            [head, tail] = f1.split(" -> ")
            [x1, y1] = head.split(",")
            [x2, y2] = tail.split(",")
            y = "".join(str(i) for i in y2 if str(i) != "\n")
            temp.append(str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y))
        for i in temp:
            temp = i.split(",")
            valves.append([int(j) for j in temp])
        return valves
    except:
        raise FileNotFoundError


def fill_matrix(valves, matrix):
    for i in valves:
        [x1, y1, x2, y2] = i
        print(i)
        if x1 == x2:
            if y2 > y1:
                for j in range(y1, y2 + 1):
                    matrix[x1][j] += 1
            else:
                for j in range(y2, y1 + 1):
                    matrix[x1][j] += 1
        elif y1 == y2:
            if x2 > x1:
                for j in range(x1, x2 + 1):
                    matrix[j][y1] += 1
            else:
                for j in range(x2, x1 + 1):
                    matrix[j][y1] += 1
        elif diagonal_check(x1, x2, y1, y2):
            if (x1 > x2):
                if (y1 > y2):
                    for i in range(x2, x1 + 1):
                        for j in range(y2, y1 + 1):
                            if diagonal_check(x1, i, y1, j):
                                matrix[i][j] += 1
                else:
                    for i in range(x2, x1 + 1):
                        for j in range(y1, y2 + 1):
                            if diagonal_check(x1, i, y1, j):
                                matrix[i][j] += 1
            else:
                if (y1 > y2):
                    for i in range(x1, x2 + 1):
                        for j in range(y2, y1 + 1):
                            if diagonal_check(x1, i, y1, j):
                                matrix[i][j] += 1
                else:
                    for i in range(x1, x2 + 1):
                        for j in range(y1, y2 + 1):
                            if diagonal_check(x1, i, y1, j):
                                matrix[i][j] += 1
    return matrix

def diagonal_check(x1, x2, y1, y2):
    if (abs(x2 - x1) == abs(y2 - y1)):
        return True
    else:
        return False

if __name__ == "__main__":
    file = "input5.txt"
    valves = read2(file)
    matrix = ([[0 for col in range(1000)] for row in range(1000)])
    new = fill_matrix(valves, matrix)
    c = 0
    for i in new:
        for j in i:
            if j >= 2:
                c += 1
    print(c)
