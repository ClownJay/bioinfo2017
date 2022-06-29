#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.23

def reconstruct_genome(pattern):
    genome = pattern[0]
    for i in range(1, len(pattern)):
        genome += pattern[i][-1]
    return genome

with open('rosalind_ba3b.txt', 'r') as fbj:
    lines = fbj.readlines()
    pattern = []
    for i in range(len(lines)):
        pattern.append(lines[i].strip())
    print(reconstruct_genome(pattern))