#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.24
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

def eulerian_graph(connect):
    # 初始化
    unused_node, used_node, with_unused_edge, path = \
        [connect.keys()], [], [], []

    # 初始随机选取一个节点开始遍历
    node = random.choice(list(connect.keys()))
    path.append(node)
    connect, unused_node, used_node, with_unused_edge = \
        undate_node(node, connect, unused_node, used_node,
                    with_unused_edge)

    # 随机游走过程：终止条件是所有的连接都用到
    while connect:
        # 随机挑选下一个节点
        while node in connect.keys():
            # 随机选取下一个节点：记录环, 删除节点信息
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
            next = random.choice(connect[node])
            connect[node].remove(next)
            path.append(next)
            node = next
            connect, unused_node, used_node, with_unused_edge = \
                undate_node(node, connect, unused_node, used_node,
                            with_unused_edge)
    return path

with open('test.txt', 'r') as fbj:
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
    print('->'.join(eulerian_graph(connect)))