import math


def read_file():
    f = open("input4.txt")
    inputs, new_inputs = [], []
    for i in f:
        inputs.append([i[i.index(":") + 1:i.index("|") - 1], i[i.index("|") + 1:i.index("\n")]])
    for [i, j] in inputs:
        i1 = [int(k) for k in i.split(" ") if k != ""]
        j1 = [int(k) for k in j.split(" ") if k != ""]
        new_inputs.append([set(i1), set(j1)])
    part1(new_inputs)
    part2(new_inputs)


def part1(new_inputs):
    points = []
    for [i, j] in new_inputs:
        k = i.intersection(j)  # To check for matches between the winning and my numbers
        if len(k) == 0:
            points.append(0)
        else:
            points.append(math.pow(2, len(k) - 1))
            # len(k) - 1 is done to remove the 1 extra match from an empty value in both sets i and j
    print(points)
    print("P1:", int(sum(points)))


def part2(new_inputs):
    new_inputs2 = [[i, j, 1] for [i, j] in new_inputs]
    # every card has at least 1 copy ; 3rd entry signifies number of copies of the cards
    for i, [j, k, l] in enumerate(new_inputs2):
        matches = j.intersection(k)
        if len(matches) == 0:
            continue
        else:
            if i != len(new_inputs2) - 1:
                i1 = i+1
                # print("i:", i, "| matches:", len(matches), "| copies:", l)
                while i1 <= i + len(matches):
                    new_inputs2[i1][2] += l
                    # print("Card:", i1+1, ":", new_inputs2[i1][2])
                    i1 += 1
    copies = sum([k for [i,j,k] in new_inputs2])
    print("P2:", copies)


if __name__ == "__main__":
    test = \
        [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\n",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\n",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11\n",
        ]
    read_file()
