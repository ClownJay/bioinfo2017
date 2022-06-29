#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.24

def kmer_debruijn(kmer_list):
    """从kmer组成列表获得对应的de Bruijn图"""
    connect = {}
    graph = []
    for kmer in kmer_list:
        if kmer[:-1] not in connect.keys():
            connect[kmer[:-1]] = [kmer[1:]]
        else:
            connect[kmer[:-1]].append(kmer[1:])
    for key in sorted(connect.keys()):
        graph.append(key+' -> '+','.join(sorted(connect[key])))
    return graph

with open('rosalind_ba3e.txt', 'r') as fbj:
    lines = fbj.readlines()
    kmer_list = []
    for i in range(len(lines)):
        kmer_list.append(lines[i].strip())
    for link in kmer_debruijn(kmer_list):
        print(link)