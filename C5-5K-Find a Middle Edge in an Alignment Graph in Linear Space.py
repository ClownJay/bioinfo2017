#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.06.29

from collections import defaultdict
from math import floor
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

def middle_edge(seq1, seq2, score_matrix, sigma=-5):
    middle = floor(len(seq2)/2)
    score = [[0 for _ in range(2)] for i in range(len(seq1)+1)]
    score[0][1] = sigma
    for i in range(1, len(seq1)+1):
        score[i][0] = score[i-1][0] + sigma
    for j in range(1, middle+1):
        for i in range(1, len(seq1) + 1):
            score[i][1] = max(score[i-1][1]+sigma,
                              score[i-1][0]+score_matrix[seq1[i-1], seq2[j-1]],
                              score[i][0]+sigma)
        for i in range(len(seq1)+1):
            score[i][0] = score[i][1]
            if i == 0:
                score[i][1] = score[i][0] + sigma
            else:
                score[i][1] = 0
    rev_seq1, rev_seq2 = seq1[::-1], seq2[::-1]
    rev_score = [[0 for _ in range(2)] for i in range(len(rev_seq1)+1)]
    rev_score[0][1] = sigma
    for i in range(1, len(rev_seq1)+1):
        rev_score[i][0] = rev_score[i-1][0] + sigma
    for j in range(1, len(rev_seq2)-middle+2):
        for i in range(1, len(rev_seq1)+1):
            rev_score[i][1] = max(rev_score[i-1][1]+sigma,
                                  rev_score[i-1][0]+score_matrix[rev_seq1[i-1], rev_seq2[j-1]],
                                  rev_score[i][0]+sigma)
        # 保留最后的信息以确定middle node后面节点的节点
        if not j == len(rev_seq2)-middle+1:
            for i in range(len(rev_seq1)+1):
                rev_score[i][0] = rev_score[i][1]
                if i == 0:
                    rev_score[i][1] = rev_score[i][0] + sigma
                else:
                    rev_score[i][1] = 0
    # 需要把rev_score列倒过来: 注意第一行不能翻，从而拼接两个矩形的比对结果
    oppo_score = [[0 for _ in range(2)] for i in range(len(rev_seq1) + 1)]
    for i in range(len(rev_seq1)+1):
        if i == 0:
            oppo_score[i][0] = rev_score[i][0]
            oppo_score[i][1] = rev_score[i][1]
        else:
            oppo_score[len(rev_seq1)-i+1][0] = rev_score[i][0]
            oppo_score[len(rev_seq1)-i+1][1] = rev_score[i][1]
    # 找到middle node 与 middle edge
    middle_score = []
    for i in range(len(seq1)+1):
        middle_score.append(score[i][0]+oppo_score[i][1])
    middle_node_i = middle_score.index(max(middle_score))
    middle_node_j = middle
    # 判断下一个连接
    index_i = len(rev_seq1) - middle_node_i + 1
    if rev_score[index_i][1] == rev_score[index_i-1][1] + sigma:
        next_node_i = middle_node_i + 1
        next_node_j = middle_node_j
    elif rev_score[index_i][1] == rev_score[index_i][0] + sigma:
        next_node_i = middle_node_i
        next_node_j = middle_node_j + 1
    else:
        # 这里索引转换不过来了，将就这样写吧
        next_node_i = middle_node_i + 1
        next_node_j = middle_node_j + 1

    return middle_node_i, middle_node_j, next_node_i, next_node_j

with open('rosalind_ba5k.txt', 'r') as fbj:
    lines = fbj.readlines()
    seq1, seq2 = lines[0].strip(), lines[1].strip()
    score_matrix = blosum_62()
    middle_node_i, middle_node_j, next_node_i, next_node_j = \
        middle_edge(seq1, seq2, score_matrix)
    print("({}, {}) ({}, {})".format(middle_node_i, middle_node_j,
                                     next_node_i, next_node_j))