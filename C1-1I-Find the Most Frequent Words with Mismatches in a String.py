#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.13

# 创建一个k-mer列表之后生成对应的k-mer d pattern search counts
import itertools

def form_kmer_dict(k):
    dic = {}
    kmer = itertools.product('ACGT', repeat=k)
    for i in kmer:
        dic[''.join(i)] = 0
    return dic

def hamming_distance(p, q):
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist += 1
    return dist

def most_freq_mismatch(text, k, d):
    dic = form_kmer_dict(k)
    ans = []
    for i in range(len(text)-k+1):
        for pattern in dic.keys():
            if hamming_distance(text[i:i+k], pattern) <= d:
                dic[pattern] += 1
    most_freq = max(dic.values())
    for key, value in dic.items():
        if value == most_freq:
            ans.append(key)
    return ' '.join(ans)

with open('rosalind_ba1i.txt', 'r') as fbj:
    lines = fbj.readlines()
    text = lines[0].strip()
    k, d = map(int, lines[1].split(' '))
    print(most_freq_mismatch(text, k, d))


