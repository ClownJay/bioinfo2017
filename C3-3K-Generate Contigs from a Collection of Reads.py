#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.30
from collections import defaultdict

def kmer_to_connect(kmer_list):
    connect = defaultdict(list)
    for kmer in kmer_list:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        connect[prefix].append(suffix)
    return connect

def connect_to_degree(connect):
    """
    记录每个节点的出入度, 返回四种类型节点的列表
    :param connect: dict
    :return: bran_node, start_bnode, end_node, path_node: list
    """
    ingree, outgree = defaultdict(int), defaultdict(int)
    not_11_node, is_11_node = [], []
    for key in connect.keys():
        # 注意connect的类型为connect[prefix] = [list of suffix]
        outgree[key] += len(connect[key])
        for value in connect[key]:
            ingree[value] += 1

    for key in connect:
        if ingree[key] == 1 and outgree[key] == 1:
            is_11_node.append(key)
        else:
            not_11_node.append(key)
    return not_11_node, is_11_node, outgree

def max_nonbran_path(connect, not_11_node, is_11_node, outgree):
    all_path = []
    for i in not_11_node:
        # 对于每个非11节点，得到从该节点开始的所有可能路径
        while outgree[i] > 0:
            path = i
            j = connect[i][0]
            connect[i].remove(j)
            outgree[i] -= 1
            path += j[-1]
            # 尽可能延伸最长：全部挑选非分支路径
            while j in is_11_node:
                # 使用之后删除该边
                is_11_node.remove(j)
                j = connect[j][0]
                path += j[-1]
            all_path.append(path)

    # 处理单独成环的11node
    while is_11_node:
        i = is_11_node[0]
        path = i
        j = connect[i][0]
        is_11_node.remove(i)
        connect[i].remove(j)
        path += j[-1]
        while j in is_11_node:
            is_11_node.remove(j)
            j = connect[j][0]
            path += j[-1]
        all_path.append(path)
    return all_path

with open('rosalind_ba3k.txt', 'r') as fbj:
    lines = fbj.readlines()
    kmer = []
    for i in range(len(lines)):
        kmer.append(lines[i].strip())
    connect = kmer_to_connect(kmer)
    not_11_node, is_11_node, outgree = connect_to_degree(connect)
    path = max_nonbran_path(connect, not_11_node, is_11_node, outgree)
    print(' '.join(sorted(path)))