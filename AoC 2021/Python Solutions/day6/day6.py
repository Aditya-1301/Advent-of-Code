def lantern(state, n):
    if (n == 0):
        return len(state)
    else:
        s1 = [e for e in state]
        for i in range(0, state.count(0)):
            s1.append(8)
        # print(s1)
        # print("state len:" + str(len(state)))
        # print("s1 len:" + str(len(s1)))
        if len(state) == len(s1):
            s1 = decrement(s1, len(s1))
            #print(s1)
            return lantern(s1, n - 1)
        elif len(s1) > len(state):
            s1 = decrement(s1, len(state))
            #print(s1)
            return lantern(s1, n - 1)


def decrement(state, n):
    list = []
    l = len(state)
    for j in range(0, n):
        if state[j] == 0:
            list.append(6)
        else:
            list.append(state[j] - 1)
    for i in range(len(list), l):
        list.append(8)
    return list

def to_map(state):
    counts = dict()
    for i in state:
        counts[i] = counts.get(i, 0) + 1
    return counts

def lantern2(map, n):
    if (n == 0):
        return sum(map.values())
    else:
        v = map.get(0, 0)
        map1 = decrement2(map)
        if v > 0:
            map1.update({8: v})
        return lantern2(map1, n-1)

def decrement2(map):
    map1 = dict()
    for k, v in map.items():
        if k == 0:
            x = map1.get(6, 0)
            map1.update({6: v+x})
        else:
            x = map1.get(k-1, 0)
            map1.update({k-1: v+x})
    return map1


if __name__ == "__main__":
    state = [3, 4, 3, 1, 2]
    state2 = [2, 3, 1, 3, 4, 4, 1, 5, 2, 3, 1, 1, 4, 5, 5, 3, 5, 5, 4, 1, 2, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 4, 1, 3, 1,
              4, 1, 1, 4, 1, 3, 4, 5, 1, 1, 5, 3, 4, 3, 4, 1, 5, 1, 3, 1, 1, 1, 3, 5, 3, 2, 3, 1, 5, 2, 2, 1, 1, 4, 1,
              1, 2, 2, 2, 2, 3, 2, 1, 2, 5, 4, 1, 1, 1, 5, 5, 3, 1, 3, 2, 2, 2, 5, 1, 5, 2, 4, 1, 1, 3, 3, 5, 2, 3, 1,
              2, 1, 5, 1, 4, 3, 5, 2, 1, 5, 3, 4, 4, 5, 3, 1, 2, 4, 3, 4, 1, 3, 1, 1, 2, 5, 4, 3, 5, 3, 2, 1, 4, 1, 4,
              4, 2, 3, 1, 1, 2, 1, 1, 3, 3, 3, 1, 1, 2, 2, 1, 1, 1, 5, 1, 5, 1, 4, 5, 1, 5, 2, 4, 3, 1, 1, 3, 2, 2, 1,
              4, 3, 1, 1, 1, 3, 3, 3, 4, 5, 2, 3, 3, 1, 3, 1, 4, 1, 1, 1, 2, 5, 1, 4, 1, 2, 4, 5, 4, 1, 5, 1, 5, 5, 1,
              5, 5, 2, 5, 5, 1, 4, 5, 1, 1, 3, 2, 5, 5, 5, 4, 3, 2, 5, 4, 1, 1, 2, 4, 4, 1, 1, 1, 3, 2, 1, 1, 2, 1, 2,
              2, 3, 4, 5, 4, 1, 4, 5, 1, 1, 5, 5, 1, 4, 1, 4, 4, 1, 5, 3, 1, 4, 3, 5, 3, 1, 3, 1, 4, 2, 4, 5, 1, 4, 1,
              2, 4, 1, 2, 5, 1, 1, 5, 1, 1, 3, 1, 1, 2, 3, 4, 2, 4, 3, 1]
    map = to_map(state2)
    print(map)
    print("\n\n")
    print(lantern2(map, 256))
