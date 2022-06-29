#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.06.28
from collections import defaultdict
import re

def blosum_62():
    score_matrix = defaultdict(int)
    with open('blosum_62.txt', 'r') as fbj:
        lines = fbj.readlines()
        pro = lines[0].strip().split('  ')
        for i in range(1, len(lines)):
            # 切割模式分先后
            score = list(map(int, re.split('  | ', lines[i])[1:]))
            for j in range(len(score)):
                score_matrix[pro[i-1], pro[j]] = score[j]
                score_matrix[pro[j], pro[i-1]] = score[j]
    return score_matrix

def affine_gap_penalties_alignment(seq1, seq2, score_matrix,
                                   sigma=-11, epsilon=-1):
    # lower代表i prefix of seq1 与 j prefix of seq2之间全局比对并且以seq2 indels结尾的最高分值
    lower = [[0 for _ in range(len(seq2)+1)] for i in range(len(seq1)+1)]
    # middle代表i prefix of seq1 与 j prefix of seq2之间全局比对并且以mis/match结尾的最高分值
    middle = [[0 for _ in range(len(seq2)+1)] for i in range(len(seq1)+1)]
    # upper代表i prefix of seq1 与 j prefix of seq2之间全局比对并且以seq1 indels结尾的最高分值
    upper = [[0 for _ in range(len(seq2)+1)] for i in range(len(seq1)+1)]
    # 初始化
    for i in range(1, len(seq1)+1):
        if i == 1:
            lower[i][0] = sigma
        else:
            lower[i][0] = lower[i-1][0] + epsilon
        middle[i][0] = lower[i][0]
        upper[i][0] = lower[i][0]
    for j in range(1, len(seq2)+1):
        if j == 1:
            upper[0][j] = sigma
        else:
            upper[0][j] = upper[0][j-1] + epsilon
        middle[0][j] = upper[0][j]
        lower[0][j] = upper[0][j]
    # 动态规划遍历
    # 注意遍历顺序：需要先更新lower和upper的值才能更新middle
    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):
            lower[i][j] = max(lower[i-1][j] + epsilon, middle[i-1][j] + sigma)
            upper[i][j] = max(upper[i][j-1] + epsilon, middle[i][j-1] + sigma)
            middle[i][j] = max(lower[i][j],
                               middle[i-1][j-1]+score_matrix[seq1[i-1], seq2[j-1]],
                               upper[i][j])
    score = max(lower[len(seq1)][len(seq2)], middle[len(seq1)][len(seq2)], upper[len(seq1)][len(seq2)])
    # 回溯
    fig = ''
    if score == lower[len(seq1)][len(seq2)]:
        fig = 'lower'
    elif score == middle[len(seq1)][len(seq2)]:
        fig = 'middle'
    else:
        fig = 'upper'
    i, j = len(seq1), len(seq2)
    seq1_align, seq2_align = [], []
    while i > 0 and j > 0:
        if fig == 'lower':
            if lower[i][j] == lower[i-1][j] + epsilon:
                seq1_align.append(seq1[i-1])
                seq2_align.append('-')
                i -= 1
                fig = 'lower'
            elif lower[i][j] == middle[i-1][j] + sigma:
                seq1_align.append(seq1[i-1])
                seq2_align.append('-')
                i -= 1
                fig = 'middle'
        elif fig == 'middle':
            if middle[i][j] == middle[i-1][j-1]+score_matrix[seq1[i-1], seq2[j-1]]:
                seq1_align.append(seq1[i-1])
                seq2_align.append(seq2[j-1])
                i -= 1
                j -= 1
                fig = 'middle'
            elif middle[i][j] == lower[i][j]:
                fig = 'lower'
            elif middle[i][j] == upper[i][j]:
                fig = 'upper'
        elif fig == 'upper':
            if upper[i][j] == upper[i][j-1] + epsilon:
                seq1_align.append('-')
                seq2_align.append(seq2[j-1])
                j -= 1
                fig = 'upper'
            elif upper[i][j] == middle[i][j-1] + sigma:
                seq1_align.append('-')
                seq2_align.append(seq2[j-1])
                j -= 1
                fig = 'middle'
    seq1_align = (''.join(reversed(seq1_align)))
    seq2_align = (''.join(reversed(seq2_align)))
    return score, seq1_align, seq2_align
with open('rosalind_ba5j.txt', 'r') as fbj:
    lines = fbj.readlines()
    seq1, seq2 = lines[0].strip(), lines[1].strip()
    score_matrix = blosum_62()
    score, seq1_align, seq2_align = \
        affine_gap_penalties_alignment(seq1, seq2, score_matrix)
    print(score)
    print(seq1_align)
    print(seq2_align)