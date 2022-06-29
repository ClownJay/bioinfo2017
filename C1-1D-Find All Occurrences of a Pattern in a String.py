#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.12

def pattern_search(pattern, text):
    ans = []
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            ans.append(str(i))
    return ' '.join(ans)

with open('rosalind_ba1d.txt', 'r') as fbj:
    lines = fbj.readlines()
    pattern = lines[0].strip()
    text = lines[1].strip()
print(pattern_search(pattern, text))
