#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.13

def hamming_distance(p, q):
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist += 1
    return dist

with open('rosalind_ba1g.txt', 'r') as fbj:
    lines = fbj.readlines()
    p = lines[0].strip()
    q = lines[1].strip()
    print(hamming_distance(p, q))
