#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.18

def profile_kmer(text, k, profile):
    dic = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    ans = ''
    prob = -1
    for i in range(len(text) - k + 1):
        prob_i = 1
        for j in range(k):
            prob_i *= profile[dic[text[i+j]]][j]
        if prob_i > prob:
           prob = prob_i
           ans = text[i:i+k]
    return ans

with open('rosalind_ba2c.txt', 'r') as fbj:
    lines = fbj.readlines()
    text = lines[0].strip()
    k = int(lines[1].strip())
    profile = [[0 for i in range(k)] for j in range(4)]
    for i in range(2, len(lines)):
        count = 0
        for j in lines[i].strip().split(' '):
            profile[i-2][count] = float(j)
            count += 1
    print(profile_kmer(text, k, profile))