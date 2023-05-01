def solution():
    num_map = {
        2: 1,
        3: 7,
        4: 4,
        7: 8
    }
    num_map2 = {'cagedb': 0, 'ab': 1, 'gcdfa': 2, 'fbcad': 3, 'eafb': 4, 'cdfbe': 5, 'cdfgeb': 6, 'dab': 7,
                'acedgfb': 8, 'cefabd': 9}
    inv_map = {0: 'cagedb', 1: 'ab', 2: 'gcdfa', 3: 'fbcad', 4: 'eafb', 5: 'cdfbe', 6: 'cdfgeb', 7: 'dab',
               8: 'acedgfb', 9: 'cefabd'}
    #inv_map = {v: k for k, v in num_map2.items()}
    num_list = [
        [set(inv_map.get(0, 0)),0],
        [set(inv_map.get(1, 0)),1],
        [set(inv_map.get(2, 0)),2],
        [set(inv_map.get(3, 0)),3],
        [set(inv_map.get(4, 0)),4],
        [set(inv_map.get(5, 0)),5],
        [set(inv_map.get(6, 0)),6],
        [set(inv_map.get(7, 0)),7],
        [set(inv_map.get(8, 0)),8],
        [set(inv_map.get(9, 0)),9]
    ]
    f = open("input8.txt")
    inputValues = []
    for i in f:
        inputValues.append(i[i.index("|") + 2:-1])
    print(inputValues)
    parsedStrings = []
    for j in inputValues:
        parsedStrings.append(j.split(" "))
    sumVal = 0
    print(parsedStrings)
    for i in parsedStrings:
        for j in i:
            n = num_map.get(len(j), 0)
            if (n != 0):
                sumVal += 1
    sumVal1 = 0
    for i in parsedStrings:
        # j0 = set(i[0])
        # j1 = set[i[1]]
        # j2 = set(i[2])
        # j3 = set(i[3])
        for j in i:
            n = num_map.get(len(j), 0)
            for k in num_list:
                if(n!=0 and set(j)==k[0]):
                    print(k[1])
        # print(j0)
        # print(j1)
        # print(j2)
        # print(j3)
        # print("=-=-=-=-=-=-=-=-=-=-")
    print(sumVal)

# def setCheck(list):
#     l1 = num_map2.keys()
#     for i in l1:
#         print(set(i))
#         set(list)
#         if (set(list) == set(i)):
#             return num_map2.get(i)
#         else:
#             return 0

if __name__ == "__main__":
    solution()

    # sumVal1 = 0
    # print(sumVal1)