import re
from typing import List


def check(file):
    f = open(file)
    input_values = []
    temp = []
    for i in f:
        if i.strip() != "":
            temp.append(i.strip("\n").split(" "))
        else:
            input_values.append([j for i1 in temp for j in i1])
            temp = []
    print(input_values)
    valid_count = 0
    for i in input_values:
        # if matches_requirements(i):
        #     valid_count += 1
        if matches_requirements_2(i):
            valid_count += 1
    print(valid_count)


def matches_requirements(r_fields: List[str]):
    req = {
        "byr:": None,
        "iyr:": None,
        "eyr:": None,
        "hgt:": None,
        "hcl:": None,
        "ecl:": None,
        "pid:": None,
        "cid:": None
    }
    for i in r_fields:
        if req[i[0:4]] is None:
            req[i[0:4]] = 1
    return all(values for values in list(req.values())[:-1])


def matches_requirements_2(r_fields: List[str]):
    req = {
        "byr:": None,
        "iyr:": None,
        "eyr:": None,
        "hgt:": None,
        "hcl:": None,
        "ecl:": None,
        "pid:": None,
        "cid:": None
    }
    for i in r_fields:
        if i[0:4] == 'byr:' and 1920 <= int(i[4:]) <= 2002:
            req['byr:'] = 1
        elif i[0:4] == 'iyr:' and 2010 <= int(i[4:]) <= 2020:
            req['iyr:'] = 1
        elif i[0:4] == 'eyr:' and 2020 <= int(i[4:]) <= 2030:
            req['eyr:'] = 1
        elif i[0:4] == 'hgt:':
            if (i[-2:] == 'cm' and 150 <= int(i[4:-2]) <= 193) or (i[-2:] == 'in' and 59 <= int(i[4:-2]) <= 76):
                req['hgt:'] = 1
        elif i[0:4] == 'hcl:' and re.match(r"#([0-9a-f]{6})", i[4:]):
            req['hcl:'] = 1
        elif i[0:4] == 'ecl:' and i[4:] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
            req['ecl:'] = 1
        elif i[0:4] == 'pid:' and re.match(r"\b0*[0-9]{1,9}\b", i[4:]):
            req['pid:'] = 1
        elif i[0:4] == 'cid:':
            req['cid:'] = 1

    return all(values for values in list(req.values())[:-1])


if __name__ == "__main__":
    file = "input4.txt"
    check(file)
