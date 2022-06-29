#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.06.13

import re
from collections import defaultdict

def pam_250():
    score_matrix = defaultdict(int)
    with open('pam_250.txt', 'r') as fbj:
        lines = fbj.readlines()
        pro = lines[0].strip().split('  ')
        for i in range(1, len(lines)):
            # 切割模式分先后
            score = list(map(int, re.split('  | ', lines[i])[1:]))
            for j in range(len(score)):
                score_matrix[pro[i-1], pro[j]] = score[j]
                score_matrix[pro[j], pro[i-1]] = score[j]
    return score_matrix

def local_alignment(seq1, seq2, score_matrix, sigma=-5):
    score = [[0 for j in range(len(seq2)+1)] for i in range(len(seq1)+1)]
    # 注意局部比对初始化的问题
    for i in range(1, len(seq1)+1):
        score[i][0] = 0
    for j in range(1, len(seq2)+1):
        score[0][j] = 0
    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):
            score[i][j] = max(score[i-1][j-1] + score_matrix[seq1[i-1], seq2[j-1]],
                              score[i-1][j]+sigma, score[i][j-1]+sigma, 0)
    # 回溯
    # 先找到最大的那个点然后回溯即可
    max_score = float('-inf')
    index_i, index_j = 0, 0
    for i in range(0, len(seq1)+1):
        for j in range(0, len(seq2)+1):
            if score[i][j] > max_score:
                index_i, index_j = i, j
                max_score = score[i][j]
    i, j = index_i, index_j
    seq1_align, seq2_align = [], []
    while i > 0 or j > 0:
        if score[i][j] == score[i-1][j-1] + score_matrix[seq1[i-1], seq2[j-1]]:
            seq1_align.append(seq1[i-1])
            seq2_align.append(seq2[j-1])
            i -= 1
            j -= 1
        elif score[i][j] == score[i-1][j]+sigma:
            seq1_align.append(seq1[i-1])
            seq2_align.append('-')
            i -= 1
        elif score[i][j] == score[i][j-1]+sigma:
            seq1_align.append('-')
            seq2_align.append(seq2[j-1])
            j -= 1
        elif score[i][j] == 0:
            break
    seq1_align = (''.join(reversed(seq1_align)))
    seq2_align = (''.join(reversed(seq2_align)))
    return max_score, seq1_align, seq2_align,

with open('rosalind_ba5f.txt', 'r') as fbj:
    lines = fbj.readlines()
    seq1, seq2 = map(list, [lines[0].strip(), lines[1].strip()])
    score_matrix = pam_250()
    score, seq1_align, seq2_align = local_alignment(seq1, seq2, score_matrix)
    print(score)
    print(seq1_align)
    print(seq2_align)