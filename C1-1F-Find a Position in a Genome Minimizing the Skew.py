#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.13

def minimun_skew(text):
    ans = []
    skew, skew_i = 0, 0
    for i in range(len(text)):
        if text[i] == 'G':
            skew_i += 1
        elif text[i] == 'C':
            skew_i -= 1
        if skew_i < skew:
            skew = skew_i
            ans = [str(i+1)]
        elif skew_i == skew:
            ans.append(str(i+1))
    return ' '.join(ans)

with open('rosalind_ba1f.txt', 'r') as fbj:
    lines = fbj.readlines()
    text = lines[0].strip()
    print(minimun_skew(text))



