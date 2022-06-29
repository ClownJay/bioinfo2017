#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.06.01

def is_sublist(lsa, lsb):
    # 在使用方法操作的时候要注意是否能够更改原变量
    local_lsa = lsa[:]
    local_lsb = lsb[:]
    while local_lsa:
        value = local_lsa.pop()
        try:
            # 这里这么写会导致输入的spectrum被修改lsb.remove(value)
            local_lsb.remove(value)
        except ValueError:
            return False
    return True

def peptide_to_spectrum(peptide, is_circle=False):
    spectrum = [0, sum(peptide)]
    if is_circle:
        for i in range(len(peptide)):
            for j in range(i+1, len(peptide)):
                spectrum.append(sum(peptide[i:j]))
            for j in range(0, i):
                spectrum.append(sum(peptide[i:]+peptide[:j]))
    else:
        for i in range(len(peptide)):
            for j in range(i+1, len(peptide)):
                spectrum.append(sum(peptide[i:j]))
    return sorted(spectrum)

def circle_spectrum_to_peptide(ideal_spectrum):
    mass_list = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115,
                 128, 129, 131, 137, 147, 156, 163, 186]
    sol_peptide, candidate = [], [[i] for i in mass_list]
    # 定界：判断是否一致
    while candidate:
        i = 0
        while i < len(candidate):
            if is_sublist(peptide_to_spectrum(candidate[i]), ideal_spectrum):
                i += 1
            else:
                candidate.remove(candidate[i])
        # 判断是否得到solution
        i = 0
        while i < len(candidate):
            if peptide_to_spectrum(candidate[i], True) == ideal_spectrum:
                sol_peptide.append('-'.join(map(str, candidate[i])))
                candidate.remove(candidate[i])
            else:
                i += 1
        # 分支：延伸
        i = 0
        while i < len(candidate):
            c = candidate[i]
            for m in mass_list:
                tmp = c + [m]
                i += 1
                candidate.insert(i, tmp)
            candidate.remove(c)
    return sol_peptide

with open('test.txt', 'r') as fbj:
    lines = fbj.readlines()
    ideal_spectrum = list(map(int, lines[0].strip().split(' ')))
    # print(ideal_spectrum)
    solution = circle_spectrum_to_peptide(ideal_spectrum)
    print(' '.join(sorted(solution)))