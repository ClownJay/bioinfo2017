#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.06.01

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

def peptide_spectrum_score(peptide, ideal_spectrum, is_circle=False):
    spectrum = peptide_to_spectrum(peptide, is_circle)
    score, i = 0, 0
    local_spectrum = ideal_spectrum[:]
    while i < len(spectrum):
        if spectrum[i] in local_spectrum:
            score += 1
            local_spectrum.remove(spectrum[i])
            i += 1
        else:
            i += 1
    return score

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

def leaderboard_cycle_peptide_sequencing(n, ideal_spectrum):
    mass_list = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115,
                 128, 129, 131, 137, 147, 156, 163, 186]
    max_mass = max(ideal_spectrum)
    leaderboard, candidate = [], [[i] for i in mass_list]
    # 初始化leaderboard
    candidate = sorted(candidate,
                       key=lambda x: peptide_spectrum_score(x, ideal_spectrum),
                       reverse=True)
    index = n-1
    for i in range(n, len(candidate)):
        if peptide_spectrum_score(candidate[i], ideal_spectrum) == \
                peptide_spectrum_score(candidate[n-1], ideal_spectrum):
            index = i
        else:
            break
    leaderboard = candidate[:index+1]
    # 判断这一轮的延伸是否能够产生新的序列，作为是否继续延伸-剪枝的策略
    while True:
        # 分支: 不需要删除原有的分支
        candidate = leaderboard[:]
        j, expand = 0, 0
        while j < len(candidate):
            c = candidate[j]
            for m in mass_list:
                tmp = c + [m]
                # 这里如果超过理想谱最大质量则不能加入
                if sum(tmp) <= max_mass:
                    j += 1
                    expand += 1
                    candidate.insert(j, tmp)
            j += 1
        # 更新leaderboard
        deletions = []
        for c in candidate:
            if not is_sublist(c, ideal_spectrum):
                expand -= 1
                deletions.append(c)
        for d in deletions:
            candidate.remove(d)
        candidate = sorted(candidate,
                           key=lambda x: peptide_spectrum_score(x, ideal_spectrum),
                           reverse=True)
        index = n-1
        for i in range(n, len(candidate)):
            if peptide_spectrum_score(candidate[i], ideal_spectrum) == \
                    peptide_spectrum_score(candidate[n-1], ideal_spectrum):
                index = i
            else:
                break
        leaderboard = candidate[:index+1]
        leaderboard = sorted(leaderboard,
                            key=lambda x: peptide_spectrum_score(x, ideal_spectrum, is_circle=True),
                            reverse=True)
        if expand == 0:
            return leaderboard[0]

with open('test.txt', 'r') as fbj:
    lines = fbj.readlines()
    n = int(lines[0])
    ideal_spectrum = list(map(int, lines[1].strip().split(' ')))
    print('-'.join(map(str, leaderboard_cycle_peptide_sequencing(n, ideal_spectrum))))