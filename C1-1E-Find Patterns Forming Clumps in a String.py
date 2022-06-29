#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.12

def clump_find(text, k, l, t):
    # double slide window
    # use the list the get the specific pattern
    ans = []
    for i in range(len(text)-l+1):
        # use the dic to get the number of pattern
        dic = {}
        for j in range(i, min(i+l-k, len(text))):
            if text[j:j+k] not in dic.keys():
                dic[text[j:j+k]] = 1
            else:
                dic[text[j:j+k]] += 1
            # remember the one that appears at least t times
            if dic[text[j:j+k]] >= t and text[j:j+k] not in ans:
                ans.append(text[j:j+k])
    return ' '.join(ans)

with open('rosalind_ba1e.txt', 'r') as fbj:
    lines = fbj.readlines()
    text = lines[0].strip()
    k, l, t = map(int, lines[1].split(' '))
    print(clump_find(text, k, l, t))

