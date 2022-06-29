#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.06.10

def longest_path(p, q):
    # path_weight[i][j]代表i,j 位置的weight
    path_weight = [[0 for i in range(len(q)+1)] for j in range(len(p)+1)]
    for i in range(1, len(p)+1):
        for j in range(1, len(q)+1):
            if p[i-1] == q[j-1]:
                path_weight[i][j] = path_weight[i-1][j-1]+1
            else:
                path_weight[i][j] = max((path_weight[i][j-1], path_weight[i-1][j]))
    i, j = len(p), len(q)
    lcs = ''
    while i > 0 and j > 0:
        if path_weight[i][j] == path_weight[i-1][j-1]+1:
            lcs = p[i-1] + lcs
            i -= 1
            j -= 1
        elif path_weight[i][j] == path_weight[i-1][j]:
            i -= 1
        elif path_weight[i][j] == path_weight[i][j-1]:
            j -= 1
    return lcs, len(lcs)

with open('test.txt', 'r') as fbj:
    lines = fbj.readlines()
    p, q = list(lines[0].strip()), list(lines[1].strip())
    print(longest_path(p, q))