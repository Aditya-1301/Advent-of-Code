def read1(file):
    try:
        i = 0
        lists = []
        gamma, epsilon = "", ""
        while i < 12:
            f = open(file)
            list = []
            for line in f:
                list.append(line[i])
            lists.append(list)
            gamma += max(set(list), key=list.count)
            epsilon += min(set(list), key=list.count)
            i += 1
        print("Gamma:" + gamma)
        print("Epsilon:" + epsilon)
        print("Power Consumption:" + str(int(gamma, 2)*int(epsilon, 2)))
    except:
        raise FileNotFoundError

def read2(file):
    f = open(file)
    lists = []
    for line in f:
        lists.append(line.removesuffix("\n"))
    o =oxygen_rating(lists, 0)
    c =co2_rating(lists, 0)
    print(int(c[0],2)*int(o[0],2))

def o2Bit(lists, i):
    oneCount = [int(list[i]) for list in lists if list[i] == "1"]
    zeroCount = [int(list[i]) for list in lists if list[i] == "0"]
    if (len(oneCount) > len(zeroCount)):
        bit = "1"
    elif (len(oneCount) < len(zeroCount)):
        bit = "0"
    else:
        bit = "1"
    new_lists = [list for list in lists if list[i] == bit]
    return new_lists

def co2Bit(lists, i):
    oneCount = [int(list[i]) for list in lists if list[i] == "1"]
    zeroCount = [int(list[i]) for list in lists if list[i] == "0"]
    if (len(oneCount) < len(zeroCount)):
        bit = "1"
    elif (len(oneCount) > len(zeroCount)):
        bit = "0"
    else:
        bit = "0"
    new_lists = [list for list in lists if list[i] == bit]
    return new_lists

def oxygen_rating(lists, i):
    if len(lists) == 1:
        return lists
    else:
        if i < len(lists[0]):
            lists = o2Bit(lists, i)
            return oxygen_rating(lists, i + 1)
        else:
            return lists

def co2_rating(lists, i):
    if len(lists) == 1:
        return lists
    else:
        if i < len(lists[0]):
            lists = co2Bit(lists, i)
            return co2_rating(lists, i + 1)
        else:
            return lists

if __name__ == "__main__":
    file = "input3.txt"
    #read1(file)
    read2(file)


