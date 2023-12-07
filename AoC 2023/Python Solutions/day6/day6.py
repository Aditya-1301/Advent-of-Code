from math import prod

if __name__ == "__main__":
    inputs_1 = [
        "Time:        55     99     97     93",
        "Distance:   401   1485   2274   1405"
    ]

    test = [
        "Time:      7  15   30",
        "Distance:  9  40  200"
    ]

    inputs_2 = {55999793: 401148522741405}
    test_2 = {71530: 940200}

    inputs1 = [int(j) for i in inputs_1 for j in i.split(" ") if j != "" and j.isnumeric()]
    inputs2 = [int(j) for i in test for j in i.split(" ") if j != "" and j.isnumeric()]
    time_to_dist_map1, time_to_dist_map2 = {}, {}
    l1, l2 = len(inputs1) // 2, len(inputs2) // 2
    for i in range(l1):
        time_to_dist_map1[inputs1[i]] = inputs1[i + l1]
    for i in range(l2):
        time_to_dist_map2[inputs2[i]] = inputs2[i + l2]
    print(time_to_dist_map1, time_to_dist_map2)

    counts = []
    for i in inputs_2:
        count = []
        for j in range(i):
            dist = (i - j) * j
            if dist > inputs_2[i]:
                count.append(dist)
        counts.append(len(count))
    print(prod(counts), counts)
