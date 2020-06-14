# -*- coding: UTF -8 -*-
# 阿姆斯特朗数
# 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 
# 例如1^3 + 5^3 + 3^3 = 153。
# 10000以内的阿姆斯特朗数： 
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407,1643,8208,9474。

number = int(input('请输入一个数字：'))
# 初始化变量 sum
sum = 0
# 指数
n = len(str(number))
#检测
temp = number
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

# 输出结果
if number == sum:
    print(number,'是阿姆斯特朗数')
else:
    print(number,'不是阿姆斯特朗数')

# 写法2
lower = int(input('最小值：'))
upper = int(input('最大值：'))

for number in range(lower,upper + 1):
    #初始化 sum
    sum = 0
    #指数
    n = len(str(number))

    #检测
    temp = number
    while temp > 0:
        digit = temp % 10 
        sum += digit ** n
        temp //= 10
    if number == sum:
        print(number)
