def read1(file):
    try:
        f = open(file)
        x = 0
        y = 0
        for line in f:
            num = [int(s) for s in line.split() if s.isdigit()]
            if line.startswith("forward"):
                x += num[0]
            elif line.startswith("up"):
                y -= num[0]
            elif line.startswith("down"):
                y += num[0]
        print(x*y)

    except:
        raise FileNotFoundError

def read2(file):
    try:
        f = open(file)
        x = 0
        y = 0
        aim = 0
        for line in f:
            num = [int(s) for s in line.split() if s.isdigit()]
            if line.startswith("forward"):
                x += num[0]
                y += aim*num[0]
            elif line.startswith("up"):
                aim -= num[0]
            elif line.startswith("down"):
                aim += num[0]
        print(x*y)

    except:
        raise FileNotFoundError

if __name__ == "__main__":
    file = "input2.txt"
    print(read1(file))
    print(read2(file))