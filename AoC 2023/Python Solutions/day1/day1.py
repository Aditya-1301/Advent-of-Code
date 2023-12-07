def read_file():
    f = open("input1_1.txt")
    test = [
        "two1nine\n",
        "eightwothree\n",
        "abcone2threexyz\n",
        "xtwone3four\n",
        "4nineeightseven2\n",
        "zoneight234\n",
        "7pqrstsixteen\n",
    ]
    calibration_numbers_1 = part_1([], f)
    print("PART1:", sum(calibration_numbers_1))
    inputs = [i.split("\\")[0] for i in f]
    print(sum(part_2(inputs)))


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


def word_to_num(input_str):
    number_words = {
        "twone": "21e",
        "sevenine": "79e",
        "oneight": "18t",
        "fiveight": "58t",
        "threeight": "38t",
        "eightwo": "82o",
        "one": "1e",
        "two": "2o",
        "three": "3e",
        "four": "4r",
        "five": "5e",
        "six": "6x",
        "seven": "7n",
        "eight": "8t",
        "nine": "9e",
    }

    for word, digit in number_words.items():
        input_str = input_str.replace(word, digit)
    return input_str


def part_2(inputs):
    output = []
    for i in inputs:
        output.append(word_to_num(i))
    return part_1([], output)


if __name__ == "__main__":
    read_file()