#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.16

def number_to_pattern(index, k):
    # 递归终止条件
    if k == 0:
        return ''
    symbol_dict = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    remainder = index % 4
    quotient = index // 4
    return number_to_pattern(quotient, k-1) + symbol_dict[remainder]

with open('rosalind_ba1m.txt', 'r') as fbj:
    lines = fbj.readlines()
    index = int(lines[0].strip())
    k = int(lines[1].strip())
print(number_to_pattern(index, k))