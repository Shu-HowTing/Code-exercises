# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
题目描述:
    在股市的交易日中，假设最多可进行两次买卖(即买和卖的次数均小于等于2)，规则是必须一笔成交后进行另一笔(即买-卖-买-卖的顺序进行)。
    给出一天中的股票变化序列，请写一个程序计算一天可以获得的最大收益。请采用实践复杂度低的方法实现。
    给定价格序列prices及它的长度n，请返回最大收益。保证长度小于等于500。
测试样例：
    [10，22，5，75，65，80],  6
返回：
    87
'''

import itertools
def max_profit(l, n):
    L = []
    for i in range(2,n-1):
        l1 = [ x for x in l[0:i]]
        l2 = [ x for x in l[i:]]
        max1 = max(max(diff(l1)),0)
        max2 = max(max(diff(l2)),0)
        L.append(max1 + max2)
    return max(L)

def diff(l):
    diff_l= []
    for i in itertools.combinations(l, 2):
        diff_l.append(i[1] - i[0])
    return diff_l

L = eval(input())   #[22, 10, 5, 75, 65]
max_profit = max_profit(L, len(L))
print(max_profit)