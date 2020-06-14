# -*- coding: UTF -8 -*-
# 整数阶乘（factorial)是所有小于及等于该数的正整数的积，0的阶乘为1.即：n!=1*2*3...*n。

number = int(input('请输入一个数字：'))
factorial = 1
# 判断数字是0、负数、正数
if number < 0:
    print('你输入的是负数，负数没有阶乘！')
elif number == 0:
    print('0 的阶乘是 1')
else:
    for i in range(1,number + 1):#遍历输入的数字，包头不包尾，所以要+1
        print(i)
        factorial = factorial * i
        #print(factorial)
    print('%d 的阶乘为 %d' % (number,factorial))
