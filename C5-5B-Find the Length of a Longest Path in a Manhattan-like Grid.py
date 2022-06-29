#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.06.09

def dp_road(m, n, down, right):
    road = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        road[i][0] = road[i-1][0] + down[i-1][0]
    for j in range(1, n+1):
        road[0][j] = road[0][j-1] + right[0][j-1]
    for i in range(1, m+1):
        for j in range(1, n+1):
            road[i][j] = max(road[i-1][j]+down[i-1][j],
                             road[i][j-1]+right[i][j-1])
    return road[m][n]

with open('rosalind_ba5b.txt', 'r') as fbj:
    lines = fbj.readlines()
    m, n = map(int, lines[0].strip().split(' '))
    down, right = [], []
    for i in range(1, m+1):
        down.append(list(map(int, lines[i].strip().split(' '))))
    for i in range(m+2, len(lines)):
        right.append(list(map(int, lines[i].strip().split(' '))))
    print(dp_road(m, n, down, right))