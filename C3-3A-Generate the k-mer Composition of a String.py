#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.23

def kmer_composition(text, k):
    kmer_list = []
    for i in range(len(text)-k+1):
        kmer_list.append(text[i:i+k])
    return sorted(kmer_list)

with open('rosalind_ba3a.txt', 'r') as fbj:
    lines = fbj.readlines()
    k = int(lines[0].strip())
    text = lines[1].strip()
    for kmer in (kmer_composition(text, k)):
        print(kmer)