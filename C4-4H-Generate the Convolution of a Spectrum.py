#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.06.08

def spectrum_convolution(spectrum):
    spectrum = sorted(spectrum)
    convolution = {}
    for i in range(len(spectrum)):
        for j in range(i, len(spectrum)):
            if spectrum[i] < spectrum[j]:
                if spectrum[j]-spectrum[i] in convolution.keys():
                    convolution[spectrum[j]-spectrum[i]] += 1
                else:
                    convolution[spectrum[j]-spectrum[i]] = 1
    mass = sorted(convolution.items(), key=lambda x: (-x[1], x[0]))
    ans = []
    for i in mass:
        for j in range(i[1]):
            ans.append(str(i[0]))
    return ' '.join(ans)


with open('rosalind_ba4h.txt', 'r') as fbj:
    lines = fbj.readlines()
    spectrum = list(map(int, lines[0].strip().split(' ')))
    print(spectrum_convolution(spectrum))