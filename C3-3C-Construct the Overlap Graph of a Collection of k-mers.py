#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.23

def true_connect(p, q):
    return True if p[1:] == q[:-1] else False

def overlap_graph(patterns):
    connect = {}
    graph = []
    for pattern in patterns:
        connect[pattern] = []
    for i in range(len(patterns)):
        for j in range(len(patterns)):
            if i != j and true_connect(patterns[i], patterns[j]):
                connect[patterns[i]].append(patterns[j])
    for key in sorted(connect.keys()):
        for pattern in connect[key]:
            graph.append(key+' -> '+pattern)
    return graph

with open('rosalind_ba3c.txt', 'r') as fbj:
    lines = fbj.readlines()
    patterns = []
    for i in range(len(lines)):
        patterns.append(lines[i].strip())
    for connect in overlap_graph(patterns):
        print(connect)