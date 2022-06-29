#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.16

# 使用数列代替我之前使用的字典计算对应的pattern出现的次数
# 输出次数矩阵
# 可以修改为更简洁的递归算法
def pattern_to_number(text):
    number = 0
    for i in range(len(text)-1, -1, -1):
        if text[i] == 'A':
            number += 0
        elif text[i] == 'C':
            number += 4 ** (len(text) - i - 1)
        elif text[i] == 'G':
            number += 2 * 4 ** (len(text) - i - 1)
        elif text[i] == 'T':
            number += 3 * 4 ** (len(text) - i - 1)
    return number

# 需要再写一个number_to_pattern就可以很快找到出现频率最高的几个
# 如果使用排序算法而不是max，又可以缩小最后输出most-freq时候的操作数


def compute_frequencise(text, k):
    freq = [0 for i in range(4 ** k)]
    # 滑窗
    for i in range(len(text) - k + 1):
        freq[pattern_to_number(text[i:i+k])] += 1
    return freq

with open('rosalind_ba1k.txt', 'r') as fbj, open('out.txt', 'w') as fbj_w:
    lines = fbj.readlines()
    text = lines[0].strip()
    k = int(lines[1].strip())
    freq = compute_frequencise(text, k)
    for i in freq:
        fbj_w.write(str(i) + ' ')