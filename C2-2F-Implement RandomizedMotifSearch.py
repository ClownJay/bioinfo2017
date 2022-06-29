#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.20
import random

def hamming_distance(p, q):
    """计算汉明距离"""
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist += 1
    return dist

def random_initiate(dna, k):
    """随机产生一个初始的Motif矩阵"""
    motif = []
    for i in range(len(dna)):
        j = random.randrange(0, len(dna[i])-k+1)
        motif.append(dna[i][j:j+k])
    return motif

def get_profile(motif, k):
    """获得对应motif的profile"""
    # 其实这里的更新可以优化，减少操作的数目
    dic = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    profile = [[1 for i in range(k)] for j in range(4)]
    for i in range(len(motif)):
        # 先算总和，之后除一下，注意保留小数位数
        for j in range(k):
            profile[dic[motif[i][j]]][j] += 1
    for i in range(len(profile)):
        for j in range(len(profile[0])):
            profile[i][j] = float(format(profile[i][j]/float(len(motif)+4),
                                         '.3f'))
    return profile

def get_score(profile, motif, k):
    """根据profile确定consensus然后计算score"""
    dic = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    consensus = ''
    for i in range(k):
        j = 0
        most_index, most = 0, 0
        while j < 4:
            if most < profile[j][i]:
                most, most_index = profile[j][i], j
            j += 1
        consensus += dic[most_index]
    score = 0
    for i in range(len(motif)):
        score += hamming_distance(consensus, motif[i])
    return score

def most_profile_kmer(text, k, profile):
    """寻找最可能的kmer"""
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

def get_motif(profile, dna, k):
    """根据profile确定最优的motif"""
    motif = []
    for i in range(len(dna)):
        motif.append(most_profile_kmer(dna[i], k, profile))
    return motif

def random_motif_search(dna, k, t):
    """随机搜索motif"""
    # 随机产生初始的motif
    motif = random_initiate(dna, k)
    best_motif = random_initiate(dna, k)
    profile = get_profile(best_motif, k)
    # 初始化score
    best_score = get_score(profile, best_motif, k)
    # 每次random算法终止条件为score不再降低
    while True:
        # 根据给定的motif获得对应的profile
        profile = get_profile(motif, k)
        # 根据profile获得对应的motif
        motif = get_motif(profile, dna, k)
        # 根据profile & motif 计算score
        score = get_score(profile, motif, k)
        if score < best_score:
            best_score = score
            best_motif = motif
        else:
            break
    return best_motif, best_score

def random_search_1000(dna, k, t, times=1000):
    """主程序要运行1000次，并取score最低的那个"""
    best_score = float('inf')
    best_motif = []
    for i in range(times):
        motif, score = random_motif_search(dna, k, t)
        if score < best_score:
            best_score = score
            best_motif = motif
    return best_motif

with open('rosalind_ba2f.txt', 'r') as fbj:
    lines = fbj.readlines()
    k, t = map(int, lines[0].strip().split(' '))
    dna = []
    for i in range(1, len(lines)):
        dna.append(lines[i].strip())
for kmer in random_search_1000(dna, k, t):
    print(kmer)