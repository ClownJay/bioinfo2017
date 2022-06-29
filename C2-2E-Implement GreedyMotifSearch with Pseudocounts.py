#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.20

# 只需要修改上一道题profile的算法即可
def hamming_distance(p, q):
    """计算汉明距离"""
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist += 1
    return dist

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

def greedy_motif_search(dna, k, t):
    best_motif = []
    best_score = float('inf')
    # 对于dna1中的每个kmer都构建对应的贪婪motif矩阵
    # 遍历过程中的每次选择都是当前条件下的最优解:most probable
    # 在选择之后不断刷新profile以便更新最优解的指标集合
    for i in range(len(dna[0])-k+1):
        # 初始化motif & profile
        motif = [dna[0][i:i+k]]
        profile = get_profile(motif, k)
        # 遍历剩下的每个dna序列，并且每次选择最优的kmer
        # 同时更新motif & profile
        for j in range(1, len(dna)):
            kmer = most_profile_kmer(dna[j], k, profile)
            # 更新motif 与profile
            # 加入新的kmer
            motif.append(kmer)
            # 更新profile
            profile = get_profile(motif, k)
        score = get_score(profile, motif, k)
        # 更新最优score & 最优motif
        if score < best_score:
            best_score = score
            best_motif = motif
    return best_motif

with open('rosalind_ba2e.txt', 'r') as fbj:
    lines = fbj.readlines()
    dna = []
    k, t = map(int, lines[0].strip().split(' '))
    for i in range(1, len(lines)):
        dna.append(lines[i].strip())
    for ans in greedy_motif_search(dna, k, t):
        print(ans)