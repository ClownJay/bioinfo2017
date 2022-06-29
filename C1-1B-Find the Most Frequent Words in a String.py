#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.12

def frequent_words(text, k):
    dic = {}
    string = []
    count = 0
    for i in range(len(text)-k+1):
        if text[i:i+k] not in dic.keys():
            dic[text[i:i+k]] = 1
        else:
            dic[text[i:i+k]] += 1
        if dic[text[i:i+k]] > count:
            count = dic[text[i:i+k]]
    for key, value in dic.items():
        if value == count:
            string.append(key)
    return string

with open("rosalind_ba1b.txt", "r") as fbj:
    lines = fbj.readlines()
    text = lines[0].strip()
    k = int(lines[1].strip())

for i in frequent_words(text, k):
    print(i)