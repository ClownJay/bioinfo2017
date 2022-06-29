#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.06.27

def fitting_alignment(seq1, seq2, sigma=-1):
    score = [[0 for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]
    # 每行的第一个设置为0，这样就可以从seq1的任意位点开始比对
    for j in range(1, len(seq2) + 1):
        score[0][j] = score[0][j - 1] + sigma
    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            if seq1[i-1] == seq2[j-1]:
                score[i][j] = max(score[i-1][j-1]+1, score[i-1][j]+sigma,
                                  score[i][j-1]+sigma)
            else:
                score[i][j] = max(score[i-1][j-1]+sigma, score[i-1][j]+sigma,
                                  score[i][j-1]+sigma)
    # 找到fitting alignment的最高分值
    highest_score, seq1_align, seq2_align = score[len(seq1)][len(seq2)], [], []
    i, j = len(seq1), len(seq2)
    for r in range(len(seq1)+1):
        if score[r][len(seq2)] > highest_score:
            highest_score = score[r][len(seq2)]
            i = r
    # 回溯
    while i > 0 and j > 0:
        # 注意回溯的时候需要优先考虑对角线的问题
        # [-1, 1][seq1[i-1] == seq2[j-1]] 后面为True则为1，为False则为-1
        if score[i][j] == score[i-1][j-1] + [-1, 1][seq1[i-1] == seq2[j-1]]:
            seq1_align.append(seq1[i - 1])
            seq2_align.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif score[i][j] == score[i-1][j] + sigma:
            seq1_align.append(seq1[i - 1])
            seq2_align.append('-')
            i -= 1
        elif score[i][j] == score[i][j-1] + sigma:
            seq1_align.append('-')
            seq2_align.append(seq2[j - 1])
            j -= 1
    seq1_align = (''.join(reversed(seq1_align)))
    seq2_align = (''.join(reversed(seq2_align)))
    return highest_score, seq1_align, seq2_align

with open('rosalind_ba5h.txt', 'r') as fbj:
    lines = fbj.readlines()
    seq1, seq2 = lines[0].strip(), lines[1].strip()
    fitting_alignment(seq1, seq2)
    score, seq1_align, seq2_align = fitting_alignment(seq1, seq2)
    print(score)
    print(seq1_align)
    print(seq2_align)