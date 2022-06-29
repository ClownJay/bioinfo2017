#!/public1/user/wangjiex/software/Python3.9/bin/python3.9
# encoding: utf-8
# Author: Wang Jiexin
# Contact: wangjx68@mail2.sysu.edu.cn
# 2022.06.09

def dp_change(money, coins):
    number = [0] * (money+1)
    for i in range(1, money+1):
        min_number = float('inf')
        for j in range(len(coins)):
            if i >= coins[j]:
                tmp = number[i-coins[j]] + 1
                if tmp < min_number:
                    min_number = tmp
        number[i] = min_number
    return number[money]

with open('rosalind_ba5a.txt', 'r') as fbj:
    lines = fbj.readlines()
    money = int(lines[0].strip())
    coins = list(map(int, lines[1].strip().split(',')))
    print(dp_change(money, coins))