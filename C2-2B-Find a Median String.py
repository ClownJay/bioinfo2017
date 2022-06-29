#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.18

import itertools

def form_all_kmer(k):
    all_kmer = []
    for i in itertools.product('ACGT', repeat=k):
        all_kmer.append(''.join(i))
    return all_kmer

def hamming_distance(p, q):
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist += 1
    return dist

def median_string(k, dna):
    dist = float('inf')
    median = []
    for kmer in form_all_kmer(k):
        # 记录每个kmer的d总和
        dist_kmer = 0
        for i in range(len(dna)):
            # 计算每个kmer对应到每个dna的最小d
            dist_dna = float('inf')
            for j in range(len(dna[i])-k+1):
                if hamming_distance(kmer, dna[i][j:j+k]) < dist_dna:
                    dist_dna = hamming_distance(kmer, dna[i][j:j+k])
            dist_kmer += dist_dna
        if dist_kmer < dist:
            dist = dist_kmer
            median = [kmer]
        elif dist_kmer == dist:
            median.append(kmer)
    return median

with open('rosalind_ba2b.txt', 'r') as fbj:
    lines = fbj.readlines()
    k = int(lines[0].strip())
    dna = []
    for i in range(1, len(lines)):
        dna.append(lines[i].strip())
    print(median_string(k, dna)[0])