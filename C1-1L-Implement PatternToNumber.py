#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.16

def pattern_to_number(text):
    # text: list
    dic_symbol = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    if not text:
        return 0
    symbol = text.pop()
    return 4 * pattern_to_number(text) + dic_symbol[symbol]

with open('rosalind_ba1l.txt', 'r') as fbj:
    lines = fbj.readlines()
    text = list(lines[0].strip())

print(pattern_to_number(text))