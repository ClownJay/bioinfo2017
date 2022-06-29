#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.06.08

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

with open('rosalind_ba4j.txt', 'r') as fbj:
    lines = fbj.readlines()
    peptide = peptide_to_mass(lines[0].strip())
    spectrum = peptide_to_spectrum(peptide)
    print(' '.join(list(map(str, spectrum))))

