#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.21
import random
import numpy

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

def gibbs_sample_motif(text, k, profile):
    """
    根据当前profile计算当前dna对应kmer的概率
    然后根据概率分布随机抽样返回抽到的motif
    """
    dic = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    prob = []
    for i in range(len(text) - k + 1):
        prob_i = 1
        for j in range(k):
            prob_i *= profile[dic[text[i+j]]][j]
        prob.append(prob_i)
    prob_total = sum(prob)
    for i in range(len(prob)):
        prob[i] = float(format(float(prob[i]) / float(prob_total)))
    j = numpy.random.choice(range(len(text)-k+1), p=prob)
    return text[j:j+k]

def gibbs_sample_search(dna, k, t, n):
    """
    gibbs采样搜索motif
    """
    # 随机产生初始的motif
    motif = random_initiate(dna, k)
    best_motif = motif
    profile = get_profile(best_motif, k)
    best_score = get_score(profile, best_motif, k)
    # print(best_motif, best_score)
    # 增加了循环次数以求是否有最优解
    for i in range(n):
        # 抽取删除
        random_number = random.randrange(0, t)
        # print(random_number)
        # 删除随机选的Motif i并获得对应的dnai 序列用于更新motif
        text = dna[random_number]
        # print(text)
        del motif[random_number]
        # print(motif)
        # 获得替换的gibbs_motif并进行替换
        gibbs_profile = get_profile(motif, k)
        gibbs_motif = gibbs_sample_motif(text, k, gibbs_profile)
        # print(gibbs_motif)
        motif.insert(random_number, gibbs_motif)
        # print(motif)
        profile = get_profile(motif, k)
        score = get_score(profile, motif, k)
        # print(score)
        if score < best_score:
            best_score = score
            best_motif = motif
    return best_motif, best_score

with open('rosalind_ba2g.txt', 'r') as fbj:
    lines = fbj.readlines()
    k, t, n = map(int, lines[0].strip().split(' '))
    dna = []
    for i in range(1, len(lines)):
        dna.append(lines[i].strip())
    best_motif = []
    best_score = float('inf')
# 需要随机20个启动以使得程序不会陷入局部最优解中
for i in range(20):
    motif, score = gibbs_sample_search(dna, k, t, n)
    if best_score > score:
        best_score = score
        best_motif = motif

for kmer in best_motif:
    print(kmer)
# print(best_score)