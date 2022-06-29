#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.12

def reverse_comp(text):
    rc_string = []
    dic = {"A": "T", "T": "A", "G": "C", "C": "G"}
    for i in range(len(text)-1, -1, -1):
        rc_string.append(dic[text[i]])
    return ''.join(rc_string)

with open("rosalind_ba1c.txt", 'r') as fbj:
    lines = fbj.readlines()
    text = lines[0].strip()
print(reverse_comp(text))