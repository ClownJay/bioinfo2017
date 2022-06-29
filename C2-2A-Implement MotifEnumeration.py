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
    if len(text) == 1:
        return ['A', 'C', 'G', 'T']
    if d == 0:
        return [text]
    neighborhood = []
    suffix_neighborhood = neighbor(text[1:], d)
    for pattern in suffix_neighborhood:
        if hamming_distance(text[1:], pattern) == d:
            neighborhood.append(text[0]+pattern)
        else:
            for symbol in ['A', 'C', 'G', 'T']:
                neighborhood.append(symbol+pattern)
    return neighborhood

def implanted_motif(dna, k, d):
    kmer_list = []
    # 列出所有的可能kmer总和
    # 如果在每个序列中都存在这一kmer的邻域则将其加入ans
    ans = []
    for text in dna:
        for i in range(len(text)-k+1):
            for kmer in neighbor(text[i:i+k], d):
                kmer_list.append(kmer)
    kmer_list = list(set(kmer_list))
    for kmer in kmer_list:
        match = 0
        i = 0
        while i < len(dna):
            j = 0
            # 注意最后的终止节点
            while j < len(dna[i]) - k + 1:
                if hamming_distance(kmer, dna[i][j:j+k]) <= d:
                    match += 1
                    break
                else:
                    j += 1
            i += 1
        if match == len(dna):
            ans.append(kmer)
    return ans

with open('rosalind_ba2a.txt', 'r') as fbj:
    lines = fbj.readlines()
    dna = []
    k, d = map(int, lines[0].strip().split(' '))
    for i in range(1, len(lines)):
        dna.append(lines[i].strip())
    print(' '.join(implanted_motif(dna, k, d)))



