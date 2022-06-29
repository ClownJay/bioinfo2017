#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.17


def hamming_distance(p, q):
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist += 1
    return dist

def neighbor(text, d):
    # 递归计算
    # 递归终止条件
    if d == 0:
        return [text]
    if len(text) == 1:
        return ['A', 'C', 'G', 'T']
    neighborhood = []
    suffix_neighborhood = neighbor(text[1:], d)
    # 递归主体逻辑
    # 视情况将第一个字符加到对应的已有pattern上
    for pattern in suffix_neighborhood:
        if hamming_distance(pattern, text[1:]) == d:
            neighborhood.append(text[0]+pattern)
        else:
            for symbol in ['A', 'C', 'G', 'T']:
                neighborhood.append(symbol+pattern)
    return neighborhood

with open('rosalind_ba1n.txt', 'r') as fbj:
    lines = fbj.readlines()
    text = lines[0].strip()
    d = int(lines[1].strip())
    for i in neighbor(text, d):
        print(i)