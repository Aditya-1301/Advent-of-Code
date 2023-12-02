def read_file():
    f = open("input1_1.txt")
    calibration_numbers_1 = part_1([], f)
    print("PART1:", sum(calibration_numbers_1))
    # inputs = [i for i in f]
    # calibration_numbers_2 = part_2(inputs)
    # print("PART2:", sum(calibration_numbers_2))


def part_1(calibration_numbers, f):
    for i in f:
        digits = []
        for j in i:
            if j.isdigit():
                digits.append(int(j))
        if len(digits) == 1:
            calibration_numbers.append(digits[0] * 10 + digits[0])
        else:
            calibration_numbers.append(digits[0] * 10 + digits[len(digits) - 1])
    return calibration_numbers


# def word_to_num(i, output):
#     number_in_letters = {
#         "one": 1,
#         "two": 2,
#         "three": 3,
#         "four": 4,
#         "five": 5,
#         "six": 6,
#         "seven": 7,
#         "eight": 8,
#         "nine": 9,
#         "twone": 21,
#         "sevenine": 79,
#         "oneight": 18,
#         "fiveight": 58,
#         "threeight": 38,
#         "twoneight": 218,
#         "eightwo": 82
#     }
#     for j in number_in_letters:
#         list = []
#         if j.isnumeric():
#             list.append(str(j))
#         if j in i:
#             # i = i.replace(j, str(number_in_letters[j]))
#             list.append(str(number_in_letters[j]))
#         print(list)
#     output.append(i)
#
#
# def part_2(inputs):
#     output = []
#     for i in inputs:
#         word_to_num(i, output)
#     print(output)
#     return part_1([], output)


if __name__ == "__main__":
    read_file()
