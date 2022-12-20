def pascal_triangle(n):
    bigarray = []
    if (n <= 0):
        bigarray.append([])
    for i in range(n):
        tmp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                tmp.append(1)
            else:
                tmp.append(bigarray[i - 1][j - 1] + bigarray[i - 1][j])
        bigarray.append(tmp)
    return bigarray
