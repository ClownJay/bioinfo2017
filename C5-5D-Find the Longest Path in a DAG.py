#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.06.10
import re
from collections import defaultdict

def longest_path(start, end, link):
    # 没有回头路的情况
    path_weight = [0] * (end + 1)
    path = [[str(i)] for i in range(end + 1)]
    for i in range(1, len(path_weight)):
        if link[i]:
            for node in link[i]:
                if path_weight[node] + score[node, i] > path_weight[i]:
                    # 需要保持最大的start开始路径
                    if str(start) in path[node]:
                        path_weight[i] = path_weight[node] + score[node, i]
                        path[i] = path[node] + [str(i)]
    return path_weight[end], path[end]

with open('rosalind_ba5d.txt', 'r') as fbj:
    lines = fbj.readlines()
    start, end = map(int, [lines[0].strip(), lines[1].strip()])
    link = defaultdict(list)
    score = defaultdict(int)
    for i in range(2, len(lines)):
        out_node, in_node, weight = map(int, re.split(':|->', lines[i]))
        if in_node in range(start, end+1) and out_node in range(start, end+1):
            link[in_node].append(out_node)
            score[out_node, in_node] = weight
    weight, path = longest_path(start, end, link)
    print(weight)
    print('->'.join(path))