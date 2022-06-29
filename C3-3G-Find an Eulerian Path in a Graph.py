#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.24

# 感觉3F与 3G区别不大，只需要对输入的图进行搜索找到欧拉路径的开头结尾即可
# 这里先标记会产生问题：当你标记之后会导致随机选择的node中如果存在新增的链条，那么会影响原本欧拉圈的构造

import random

def undate_node(node, connect, unused_node, used_node,
                with_unused_edge):
    # 更新列表与路径记录
    if node in unused_node:
        unused_node.remove(node)
    if node not in used_node:
        used_node.append(node)
    # 注意逻辑判断的先后
    if node in connect.keys() and not connect[node]:
        del(connect[node])
    # 更新是否具有新边
    if node in connect.keys() and node not in with_unused_edge:
        with_unused_edge.append(node)
    elif node not in connect.keys() and node in with_unused_edge:
        with_unused_edge.remove(node)
    return connect, unused_node, used_node, with_unused_edge

def add_link(connect):
    """新增一个connect使其具有欧拉圈"""
    ingree, outgree = {}, {}
    out_node, in_node = '', ''
    for key, values in connect.items():
        outgree[key] = len(values)
        for value in values:
            if value not in ingree.keys():
                ingree[value] = 1
            else:
                ingree[value] += 1
    # 搜索获得对应的欧拉路开头结尾：注意有可能存在出\入度为0的情况
    for key in ingree.keys():
        if (ingree[key] == 1 and key not in outgree.keys()) or \
                ingree[key] > outgree[key]:
            out_node = key
    for key in outgree.keys():
        if (outgree[key] == 1 and key not in ingree.keys()) or \
                outgree[key] > ingree[key]:
            in_node = key
    # 新增连接
    if out_node not in connect.keys():
        connect[out_node] = [in_node]
    else:
        connect[out_node].append(in_node)
    return connect, in_node, out_node

def eulerian_path(connect):
    # 需要添加一对连接使得所有的节点都是平衡的，并且获得对应的搜索开头
    connect, start, end = add_link(connect)
    # 初始化
    unused_node, used_node, with_unused_edge, path = \
        [connect.keys()], [], [], []

    # 选取欧拉路径开始进行遍历
    node = start
    path.append(node)
    connect, unused_node, used_node, with_unused_edge = \
        undate_node(node, connect, unused_node, used_node,
                    with_unused_edge)

    # 随机游走过程：终止条件是所有的连接都用到
    while connect:
        # 随机挑选下一个节点
        while node in connect.keys():
            # 随机选取下一个节点：记录环, 删除节点信息
            # 特殊处理一下我们标记过的首尾节点
            # 如果其中不是只包含innode/ start 则抽取除start之外的节点
            if node == end and len(connect[node]) > 1:
                next = random.choice(connect[node])
                while next == start:
                    next = random.choice(connect[node])
            else:
                next = random.choice(connect[node])
            connect[node].remove(next)
            connect, unused_node, used_node, with_unused_edge = \
                undate_node(node, connect, unused_node, used_node,
                            with_unused_edge)

            node = next
            # 更新三个记录列表
            path.append(node)
            connect, unused_node, used_node, with_unused_edge = \
                undate_node(node, connect, unused_node, used_node,
                            with_unused_edge)
        # 成环但是没有成欧拉环处理
        # 从环里面有边未使用的节点随机选取另一个节点开始新的遍历
        if with_unused_edge:
            # 去掉第一个
            path = path[1:]
            # 如果不是with_unused_edge其中只包含end, 就抽取除end 之外的节点
            if end in with_unused_edge and len(with_unused_edge) > 1:
                node = random.choice(with_unused_edge)
                while node == end:
                    node = random.choice(with_unused_edge)
            else:
                node = random.choice(with_unused_edge)
            # 更改当前的路径调整随机选择的节点在第一位，其他次序不变
            # 并根据选取的节点更新3个列表
            head = path.index(node)
            # 注意处理新的路径要在新挑选的节点处断开并保持原有信息不变
            path = path[head:] + path[:head] + [node]

            # 更新列表
            connect, unused_node, used_node, with_unused_edge = \
                undate_node(node, connect, unused_node, used_node,
                            with_unused_edge)

            # 并且判断节点是否还存在未使用的边
            # 如果其中不是只包含innode/ start 则抽取除start之外的节点
            if node == end and len(connect[node]) > 1:
                next = random.choice(connect[node])
                while next == start:
                    next = random.choice(connect[node])
            else:
                next = random.choice(connect[node])
            connect[node].remove(next)
            path.append(next)

            node = next
            connect, unused_node, used_node, with_unused_edge = \
                undate_node(node, connect, unused_node, used_node,
                            with_unused_edge)

    # 因为我们人工加上了一个新的连接，所以这时候需要对新的连接进行人工断联，使其作为欧拉路的首尾
    index = -1
    for i in range(1, len(path)):
        if path[i] == end and path[i+1] == start:
            index = i+1
            break
    # 注意这时候欧拉环的首尾是同个节点，修改的时候需要去掉其中一个记录
    path = path[:-1]
    path = path[index:] + path[:index]
    return path

with open('rosalind_ba3g.txt', 'r') as fbj:
    lines = fbj.readlines()
    connect = {}
    edge_counts = 0
    for i in range(len(lines)):
        key = lines[i].strip().split(' -> ')[0]
        values = lines[i].strip().split(' -> ')[1].split(',')
        for value in values:
            edge_counts += 1
            if key not in connect.keys():
                connect[key] = [value]
            else:
                connect[key].append(value)
    print('->'.join(eulerian_path(connect)))