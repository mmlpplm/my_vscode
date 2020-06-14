# -*- coding: UTF -8 -*-
# 质数判断

number = int(input('请输入一个数字：'))

if number > 1:
    for i in range(2,number):
        if (number % i) == 0:
            print(number,'不是质数')
            print(i,'乘以',number//i,'是',number)
            break
    else:
        print(number,'是质数')
else:
    print(number,'不是质数')
    
