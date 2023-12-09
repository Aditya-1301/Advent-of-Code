test_input = [
    '0 3 6 9 12 15\n',
    '1 3 6 10 15 21\n',
    '10 13 16 21 30 45\n'
]

f = open("input9.txt")

test_in = [i.split("\n")[0] for i in f]  # For testing change to `test_input` instead
t_inputs = [list(map(int, i.split())) for i in test_in]


def recursive_difference(acc: list, arr: list):
    # print(acc)
    if len(arr) <= 1 or arr.count(arr[0]) == len(arr):
        return acc
    else:
        difs = [arr[j + 1] - arr[j] for j in range(len(arr) - 1)]
        acc.append(difs)
        return recursive_difference(acc, difs)


all_difs = []
all_vals = []

for i in t_inputs:
    rd = recursive_difference([], i)
    # print("rd", rd)
    all_difs.append(rd)
    rd.insert(0, i)
    print("vrd", rd)
    all_vals.append(rd)
    # print("all differences:", all_difs)
    # print("all values:", all_vals)

sum_all = 0

for i in all_vals:
    sum_i = 0
    for j in i:
        sum_i += j[len(j) - 1]
    # print(sum_i)
    sum_all += sum_i

sum_prev = 0

# for i in all_vals:
#     sum_j = 0
#     for k in range(len(i)):
#         sum_j += ()
#
# print("Sum:", sum_all)
