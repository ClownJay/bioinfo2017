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

def approximate_pattern_match(pattern, text, d):
    ans = []
    for i in range(len(text)-len(pattern)+1):
        if hamming_distance(text[i:i+len(pattern)], pattern) <= d:
            ans.append(str(i))
    return ' '.join(ans)

with open('rosalind_ba1h.txt', 'r') as fbj:
    lines = fbj.readlines()
    pattern = lines[0].strip()
    text = lines[1].strip()
    d = int(lines[2].strip())
    print(approximate_pattern_match(pattern, text, d))