def read_file():
    f = open("input1.txt")
    list1 = []
    for i in f:
        list1.append(int(i.strip("\n")))
    set1 = set(list1)
    flag1 = flag2 = False
    for i in set1:
        for j in set1:
            if i + j == 2020 and i != j and flag1 is False:
                print(i * j)
                flag1 = True
    for i in set1:
        for j in set1:
            for k in set1:
                if i + j + k == 2020 and i != j and j != k and k != i and flag2 is False:
                    print(i * j * k)
                    flag2 = True


read_file()
