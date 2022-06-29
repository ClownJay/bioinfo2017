#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.05.31

def count_pet(mass):
    # 记得113 与 128有两个
    mass_list = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115,
                 128, 129, 131, 137, 147, 156, 163, 186]
    # pet_number[i]代表对应i mass的序列数目
    pet_number = [0 for i in range(0, mass+1)]
    # 初始化
    pet_number[0] = 1
    # 递推公式为i mass的数目 等于所有i-AA>=0 mass 数目的总和: 书里的定义为质量数字序列
    # 根据书上定义该的递推公式，我个人认为是i-AA要刚好又能作为任意aa的组合质量
    for i in range(mass+1):
        for j in range(len(mass_list)):
            if i - mass_list[j] >= 0:
                pet_number[i] += pet_number[i-mass_list[j]]
    return pet_number[mass]

with open('rosalind_ba4d.txt', 'r') as fbj:
    lines = fbj.readlines()
    mass = int(lines[0].strip())
    print(count_pet(mass))