import math
def is_prime(n):
    n_root = int(math.sqrt(n))
    for i in range(2,n_root):
        if(n%i == 0):
            return False
        else:
            continue
    return True

#list = [i for i in range(2,449) if is_prime(i)]

matrix = [
            [1,2,3],
            [4,5,6],
            [7,7,7]
         ]

matrix2 = [[1,2,3],[2,1,3],[3,2,1]]
matrix3 = [[1,2,3],[2,3,1],[3,2,1]]
matrix4 = [[1,2,3],[1,3,4],[1,4,3]]

def columncheck(matrix):
    for i in range(0, len(matrix)):
        setI = []
        for j in range(0, len(matrix[0])):
            setI.append(matrix[j][i])
        if len(set(setI)) == 1:
            return True
        else:
            continue
    return False

def rowcheck(matrix):
    for i in matrix:
        if(len(set(i)) == 1):
            return True
        else:
            continue
    return False

def diagonacheck(matrix):
    diagonal = []
    diagonal2 = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if(i == j):
                diagonal.append(matrix[i][j])
                if(j == len(matrix[0]) - i - 1):
                    diagonal2.append(matrix[i][j])
            elif(j == len(matrix[0]) - i - 1):
                print(str(i) + " " + str(j))
                diagonal2.append(matrix[i][j])
    if len(set(diagonal)) == 1:
        return True
    elif len(set(diagonal2)) == 1:
        return True
    else:
        return False

print(columncheck(matrix4))

