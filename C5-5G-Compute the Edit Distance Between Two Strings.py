#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.06.26

def edit_distance(seq1, seq2):
    distance = [[0 for _ in range(len(seq2)+1)] for i in range(len(seq1)+1)]
    for i in range(1, len(seq1)+1):
        distance[i][0] = distance[i-1][0] + 1
    for j in range(1, len(seq2)+1):
        distance[0][j] = distance[0][j-1] + 1
    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):
            if seq1[i-1] == seq2[j-1]:
                distance[i][j] = min(distance[i-1][j]+1, distance[i][j-1]+1,
                                     distance[i-1][j-1])
            else:
                distance[i][j] = min(distance[i-1][j]+1, distance[i][j-1]+1,
                                     distance[i-1][j-1]+1)
    return distance[len(seq1)][len(seq2)]

with open('rosalind_ba5g.txt', 'r') as fbj:
    lines = fbj.readlines()
    seq1, seq2 = lines[0].strip(), lines[1].strip()
    dist = edit_distance(seq1, seq2)
    print(dist)