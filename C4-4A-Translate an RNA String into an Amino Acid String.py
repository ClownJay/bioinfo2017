#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.30

def rna_to_protein(rna):
    """
    translate rna to protein
    :param rna: string
    :return: protein
    """
    protein = ''
    condon_table = {'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N',
                    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
                    'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGU': 'S',
                    'AUA': 'I', 'AUC': 'I', 'AUG': 'M', 'AUU': 'I',
                    'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H',
                    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
                    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
                    'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
                    'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAU': 'D',
                    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
                    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
                    'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
                    'UAA': '*', 'UAC': 'Y', 'UAG': '*', 'UAU': 'Y',
                    'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
                    'UGA': '*', 'UGC': 'C', 'UGG': 'W', 'UGU': 'C',
                    'UUA': 'L', 'UUC': 'F', 'UUG': 'L', 'UUU': 'F',
                    }
    # 标记翻译起始位点：第一个出现的即可
    start = -1
    for i in range(len(rna)):
        if rna[i:i+3] == 'AUG':
            start = i
            break
    for i in range(start, len(rna), 3):
        if condon_table[rna[i:i+3]] == '*':
            break
        protein += condon_table[rna[i:i+3]]
    return protein

with open('rosalind_ba4a.txt', 'r') as fbj:
    lines = fbj.readlines()
    rna = lines[0].strip()
    print(rna_to_protein(rna))