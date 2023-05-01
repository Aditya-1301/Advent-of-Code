def read1(file):
    try:
        f = open(file)
        count = 0
        list = []
        #i = 0
        for line in f:
            list.append(int(line))
        i = 0
        while(i < len(list) - 1):
            if list[i] < list[i+1]:
                count += 1
            i += 1
        print(count)
    except:
        raise FileNotFoundError

def read2(file):
    try:
        f = open(file)
        count = 0
        list = []
        #i = 0
        for line in f:
            list.append(int(line))
        i = 0
        while(i < (len(list) - 5)):
            sum1 = list[i] + list[i+1] + list[i+2]
            sum2 = list[i+3] + list[i+4] + list[i+5]
            if (sum1 < sum2):
            # if list[i] < list[i+3]:
                count += 1
            i += 1
        print(count)
    except:
        raise FileNotFoundError


if __name__ == "__main__":
    file = "input1.txt"
    read1(file)
    read2(file)
