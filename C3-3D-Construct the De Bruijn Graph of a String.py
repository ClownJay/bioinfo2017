#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.23

def debruijn_graph(text, k):
    connect = {}
    graph = []
    for i in range(len(text)-k+1):
        string = text[i:i+k]
        if string[:-1] not in connect.keys():
            connect[string[:-1]] = [string[1:]]
        else:
            connect[string[:-1]].append(string[1:])
    for key in sorted(connect.keys()):
        val = ','.join(list(set(connect[key])))
        graph.append(key+' -> '+val)
    return graph

with open('test.txt', 'r') as fbj:
    lines = fbj.readlines()
    k = int(lines[0].strip())
    text = lines[1].strip()
    for i in debruijn_graph(text, k):
        print(i)