# -*- coding: UTF -8 -*-
# 输出指定范围内的素数，素数（prime number)又称质数，有无限个，除了1和它本身以外不再被其它的数整除。

under = int(input('请输入区间最小值：'))
upper = int(input('请输入区间最大值：'))

for number in range(under,upper + 1):
    if number > 1:
        for i in range(2,number):
            if (number % i) == 0:
                break
        else:
            print(number,end='|')# end参数省略等于默认end='\n'等于成列打印每字换行,end='|'表示成行打印以|分隔
