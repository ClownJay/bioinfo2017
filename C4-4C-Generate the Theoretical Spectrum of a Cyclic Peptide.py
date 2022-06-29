#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.31

def circle_ppet_to_spectrum(pet):
    mass_table = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
                  'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
                  'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                  'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
    sub_pet = ['', pet]
    for i in range(len(pet)):
        for j in range(i+1, len(pet)):
            sub_pet.append(pet[i:j])
        for j in range(0, i):
            sub_pet.append(pet[i:]+pet[:j])
    # 不能简单使用set：因为存在相同的子序列，如相同的单个氨基酸
    # sub_pet = sorted(list(set(sub_pet)))
    mass = []
    for sub in sub_pet:
        if sub == '':
            mass.append('0')
        else:
            aas = list(sub)
            aas_mass = 0
            for aa in aas:
                aas_mass += mass_table[aa]
            mass.append(str(aas_mass))
    return ' '.join(sorted(mass, key=int))

with open('rosalind_ba4c.txt', 'r') as fbj:
    lines = fbj.readlines()
    pet = lines[0].strip()
    print(circle_ppet_to_spectrum(pet))