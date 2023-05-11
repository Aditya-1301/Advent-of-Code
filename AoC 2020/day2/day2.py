from enum import Enum


def read_file(file, mode):
    f = open(file)
    dic = []
    passwords = []
    for i in f:
        dic1 = [i.split(" ")[1].replace(":", ""), i.split(" ")[0].split("-")[0], i.split(" ")[0].split("-")[1]]
        dic.append(dic1)
        passwords.append(i.split(" ")[2].replace("\n", ""))
    valid = 0
    if mode == "part1":
        for i, j in zip(dic, passwords):
            print(f"{i} {j}")
        for i, j in zip(dic, passwords):
            if int(i[1]) <= j.count(i[0]) <= int(i[2]):
                valid += 1
        return valid
    elif mode == "part2":
        for i, j in zip(dic, passwords):
            # print(f"{j[int(i[1]) - 1]} {i} {j}")
            if int(j[int(i[1]) - 1] == i[0]) ^ int(j[int(i[2]) - 1] == i[0]):
                valid += 1
        return valid


if __name__ == "__main__":
    print(f" PART 1: {read_file('input2.txt', 'part1')}")
    print(f" PART 2: {read_file('input2.txt', 'part2')}")
