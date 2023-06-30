f = open("input8_example.txt")
list = []
for i in f:
    list.append([int(j) for j in i if j != '\n'])
    visible_count = 0
for i in range(0, len(list), 1):
    for j in range(1, len(list) - 1, 1):
        if i == 0:
            if list[i][j - 1] < list[i][j] > list[i][j + 1] and list[i][j + 1] < list[i][j]:
                visible_count += 1
        if i == len(list) - 1:
            if list[i][j - 1] < list[i][j] > list[i][j + 1] and list[i][j - 1] < list[i][j]:
                visible_count += 1
        if j == 0:
            if list[i][j - 1] < list[i][j] > list[i][j + 1] and list[i][j + 1] < list[i][j]:
                visible_count += 1
        if j == len(list[0]) - 1:
            if list[i][j - 1] < list[i][j] > list[i][j + 1] and list[i][j - 1] < list[i][j]:
                visible_count += 1

for i in range(1, len(list) - 1, 1):
    for j in range(1, len(list[0]) - 1, 1):
        if list[i - 1][j] < list[i][j] > list[i + 1][j] and list[i][j - 1] < list[i][j] > list[i][j + 1]:
            visible_count += 1
if list[0][1] < list[0][0] > list[1][0]:
    visible_count += 1
if list[0][len(list[0]) - 2] < list[0][len(list[0]) - 1] > list[1][len(list[0]) - 1]:
    visible_count += 1
if list[len(list) - 2][0] < list[len(list) - 1][0] > list[len(list) - 1][1]:
    visible_count += 1
if list[len(list) - 2][len(list[0]) - 1] < list[len(list) - 1][len(list[0]) - 1] > list[len(list) - 2][
    len(list[0]) - 1]:
    visible_count += 1

print(visible_count)
