# -*- coding: UTF -8 -*-
# 最大公约数算法
def hcf(x,y):
    '''该函数返回两个数的最大公约数'''
    #获取最小值
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf =i
    return hcf

number_1 = int(input('输入一个数字:'))
number_2 = int(input('输入二个数字:'))

print(number_1,'和',number_2,'的最大公约数为',hcf(number_1,number_2))

