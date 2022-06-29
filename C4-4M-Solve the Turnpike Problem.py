#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.06.08

def find_a(ans, dif_a, position, count):
    # position 表示取哪个位置
    tmp = dif_a[position]
    if position == -1:
        dif_a = dif_a[:position]
    else:
        dif_a = dif_a[:position] + dif_a[position+1:]
    tag = True
    # 不计入0
    tmp_dif_a = dif_a[:]
    for i in range(1, len(ans)):
        if abs(ans[i] - tmp) not in tmp_dif_a:
            tag = False
        else:
            tmp_dif_a.remove(abs(ans[i]-tmp))
    # 正确递归
    if tag:
        for i in range(1, len(ans)):
            dif_a.remove(abs(ans[i] - tmp))
        ans.append(tmp)
        ans = sorted(ans)
        position = -1
    # 错误递归
    else:
        if position == -1:
            dif_a = dif_a + [tmp]
        else:
            dif_a = dif_a.insert(len(dif_a)+1+position, tmp)
        if position == -len(dif_a):
            position = -1
        else:
            position -= 1
    if not len(ans) == count or dif_a:
        find_a(ans, dif_a, position, count)
    return ans

with open('test.txt', 'r') as fbj:
    lines = fbj.readlines()
    dif_a = list(map(int, lines[0].strip().split(' ')))
    count, index = 0, 0
    for i in range(len(dif_a)):
        if dif_a[i] > 0:
            index += 1
        elif dif_a[i] == 0:
            count += 1
    dif_a = dif_a[len(dif_a)-index:]
    ans = [0, dif_a[-1]]
    for i in range(len(ans)):
        for j in range(i + 1, len(ans)):
            dif_a.remove(ans[j] - ans[i])
    find_a(ans, dif_a, -1, count)
    print(ans)