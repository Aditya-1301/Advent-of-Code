import re


def read_file():
    f = open("input2.txt")
    x = [re.sub(r"Game \d*:|\n|\s", "", i) for i in f]
    y = [re.split(r";", i) for i in x]
    z = [[sub_str.split(',') for sub_str in inner_list] for inner_list in y]
    print("[P1, P2] =", solution(z))


def read_file_test_input(a):
    x = [re.sub(r"Game \d*:|\n|\s", "", i) for i in a]
    y = [re.split(r";", i) for i in x]
    z = [[sub_str.split(',') for sub_str in inner_list] for inner_list in y]
    print("[P1, P2] =", solution(z))


def solution(inputs):
    count = 0
    red_l, green_l, blue_l = 12, 13, 14
    power = []
    for a, i in enumerate(inputs):
        # print(a, i)
        bools, reds, blues, greens = [], [], [], []
        for j in i:
            for k in j:
                match = re.match(r'(\d+)(red|blue|green)', k)
                if match:
                    number, color = match.groups()
                    number = int(number)
                    if color == 'red':
                        reds.append(number)
                        bools.append(True) if number <= red_l else bools.append(False)
                    elif color == 'blue':
                        blues.append(number)
                        bools.append(True) if number <= blue_l else bools.append(False)
                    elif color == 'green':
                        greens.append(number)
                        bools.append(True) if number <= green_l else bools.append(False)
        # print("MAX :", max(reds), max(blues), max(greens),max(reds)*max(blues)*max(greens) )
        power.append(max(reds)*max(blues)*max(greens))
        if all(bools):
            count += (a+1)
    return [count, sum(power)]


if __name__ == "__main__":
    test_input = \
        [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        ]
    read_file()
