#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.12

# count the frequency of the k-mer in the string of DNA

def pattern_count(text, pattern):
    count = 0
    # the last k-mer starts at the position of len(text)-len(pattern)
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

with open("rosalind_ba1a.txt", 'r') as fbj:
    lines = fbj.readlines()
    text = lines[0].strip()
    pattern = lines[1].strip()
print(pattern_count(text, pattern))
