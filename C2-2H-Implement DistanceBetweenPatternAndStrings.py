#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.23

def hamming_distance(p, q):
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist += 1
    return dist

def distance_pattern_string(pattern, dna):
    """计算一个pattern到dna中所有序列的最小距离"""
    k = len(pattern)
    dist = 0
    for i in range(len(dna)):
        dist_dna = float('inf')
        for j in range(len(dna[i])-k+1):
            if hamming_distance(pattern, dna[i][j:j+k]) < dist_dna:
                dist_dna = hamming_distance(pattern, dna[i][j:j+k])
        dist += dist_dna
    return dist

with open('rosalind_ba2h.txt', 'r') as fbj:
    lines = fbj.readlines()
    pattern = lines[0].strip()
    dna = lines[1].strip().split(' ')
    print(distance_pattern_string(pattern, dna))