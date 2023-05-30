def read_file(file):
    f = open(file)
    trees = []
    for i in f:
        tree = []
        for j in i:
            if j != "\n":
                tree.append(int(j))
        trees.append(tree)
    print(trees)

    for i in range(len(trees)):
        for j in range(len(trees[0])):
            if (i, j) == (0, 0):
                None
            #elif (i,j) == (0, len(trees))



if __name__ == "__main__":
    read_file("input8.1.txt")
