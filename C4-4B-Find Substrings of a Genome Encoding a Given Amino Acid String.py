#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.30

def reverse_complemet(rna):
    rc = ''
    for i in range(len(rna)-1, -1, -1):
        if rna[i] == 'A':
            rc += 'U'
        elif rna[i] == 'U':
            rc += 'A'
        elif rna[i] == 'G':
            rc += 'C'
        elif rna[i] == 'C':
            rc += 'G'
    return rc

def rna_to_protein_complete(rna):
    """
    translate rna to protein: 考虑了启动子与终止子完整区域的
    :param rna: string
    :return: protein
    """
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
    # 这里需要修改寻找起始位点的方法：移码框
    start, complete = -1, False
    protein, coding_rna = '', ''
    # 不能写成 for i in range(len(rna), 3): 歧义
    for i in range(0, len(rna), 3):
        if rna[i:i+3] == 'AUG':
            start = i
            break
    if start == -1:
        return '', ''
    for i in range(start, len(rna), 3):
        if len(rna[i:i + 3]) == 3:
            if condon_table[rna[i:i+3]] == '*':
                complete = True
                break
            protein += condon_table[rna[i:i+3]]
            coding_rna += rna[i:i+3]
    if complete:
        return protein, coding_rna
    else:
        return '', ''

def rna_to_protein(rna):
    """
    translate rna to protein: 不考虑启动子与终止子完整区域的
    :param rna: string
    :return: protein
    """
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
    # 这里需要修改寻找起始位点的方法：移码框
    protein, coding_rna = '', ''
    for i in range(0, len(rna), 3):
        if len(rna[i:i + 3]) == 3:
            # if condon_table[rna[i:i+3]] == '*':
                # complete = True
                # break
            protein += condon_table[rna[i:i+3]]
            coding_rna += rna[i*3:(i+3)*3]
    return protein, coding_rna

def find_code(rna, protein, rc=False):
    # 直接在之前翻译的函数中记录对应的rna序列，然后指针寻找即可
    code = []
    for i in range(3):
        coding_pro, coding_rna = rna_to_protein(rna[i:])
        if coding_pro and coding_rna:
            for j in range(len(coding_pro)-len(protein)+1):
                if coding_pro[j:j+len(protein)] == protein:
                    if not rc:
                        code.append(coding_rna[j*3:(j+len(protein))*3])
                    else:
                        code.append(reverse_complemet
                                    (coding_rna[j*3:(j+len(protein))*3]))
    return code

with open('rosalind_ba4b.txt', 'r') as fbj:
    lines = fbj.readlines()
    dna = lines[0].strip()
    protein = lines[1].strip()
    rna = dna.replace('T', 'U')
    rc_rna = reverse_complemet(rna)
    code = find_code(rna, protein)
    rc_code = find_code(rc_rna, protein, rc=True)
    for c in code+rc_code:
        print(c.replace('U', 'T'))