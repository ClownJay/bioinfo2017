#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.06.08
from collections import defaultdict

def peptide_to_mass(peptide):
    mass_table = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
                  'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
                  'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                  'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
    mass = []
    for i in range(len(peptide)):
        mass.append(mass_table[peptide[i]])
    return mass

def peptide_to_spectrum(peptide, is_circle=False):
    spectrum = [0]
    if is_circle:
        for i in range(len(peptide)):
            for j in range(i+1, len(peptide)+1):
                spectrum.append(sum(peptide[i:j]))
            for j in range(0, i):
                spectrum.append(sum(peptide[i:]+peptide[:j]))
    else:
        for i in range(len(peptide)):
            for j in range(i+1, len(peptide)+1):
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

def trim_leaderboard(peptides, n):
    for p in peptides:
        mass[p] = peptide_to_mass(p)
    ideal_spectrum = list(map(int, lines[1].strip().split(' ')))
    score = defaultdict(int)
    for p in peptides:
        score[p] = peptide_spectrum_score(mass[p], ideal_spectrum)
    leaderboard = sorted(score.items(), key=lambda x: -x[1])
    index = n
    for i in range(n, len(leaderboard)):
        if leaderboard[i][1] == leaderboard[n - 1][1]:
            index = i + 1
    ans = []
    for i in range(index):
        ans.append(leaderboard[i][0])
    return ' '.join(ans)

with open('rosalind_ba4l.txt', 'r') as fbj:
    lines = fbj.readlines()
    peptides = lines[0].strip().split(' ')
    mass = defaultdict(list)
    n = int(lines[2].strip())
    print(trim_leaderboard(peptides, n))

