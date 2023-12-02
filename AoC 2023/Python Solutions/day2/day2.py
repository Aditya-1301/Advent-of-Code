import re


def read_file():
    f = open("input2.txt")
    x = [re.sub(r"Game \d*:|\n|\s", "", i) for i in f]
    y = [re.split(r";", i) for i in x]
    z = [[sub_str.split(',') for sub_str in inner_list] for inner_list in y]
    print("P1:", part1(z))


def read_file_test_input(a):
    x = [re.sub(r"Game \d*:|\n|\s", "", i) for i in a]
    y = [re.split(r";", i) for i in x]
    z = [[sub_str.split(',') for sub_str in inner_list] for inner_list in y]
    print("P1:", part1(z))


def part1(inputs):
    count = 0
    redL, greenL, blueL = 12, 13, 14
    for a, i in enumerate(inputs):
        print(a, i)
        bools = []
        reds = []
        blues = []
        greens = []
        for j in i:
            for k in j:
                match = re.match(r'(\d+)(red|blue|green)', k)
                if match:
                    number, color = match.groups()
                    number = int(number)
                    if color == 'red':
                        reds.append(number)
                        bools.append(True) if number <= redL else bools.append(False)
                    elif color == 'blue':
                        blues.append(number)
                        bools.append(True) if number <= blueL else bools.append(False)
                    elif color == 'green':
                        greens.append(number)
                        bools.append(True) if number <= greenL else bools.append(False)
        if all(bools):
            count += (a+1)
    return count


if __name__ == "__main__":
    i = \
        [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        ]
    read_file()
