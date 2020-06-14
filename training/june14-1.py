# -*- coding: UTF -8 -*-
# 用户输入
x = input('请输入 x 值：')
y = input('请输入 y 值：')

# 创建临时变量，并交换
temp = x
x = y
y = temp

print('交换后 x 的值为：{}'.format(x))
print('交换后 y 的值为：{}'.format(y))

#写法2
x = input('请输入 x 值：')
y = input('请输入 y 值：')
#不使用临时变量
x,y = y,x
print('交换后 x 的值为：{}'.format(x))
print('交换后 y 的值为：{}'.format(y))

#写法3
x = float(input('请输入 x 值：'))
y = float(input('请输入 y 值：'))
#不使用临时变量
x = x + y
y = x - y
x = x - y
print('交换后 x 的值为：{}'.format(x))
print('交换后 y 的值为：{}'.format(y))

#写法4
x = int(input('请输入 x 值：'))
y = int(input('请输入 y 值：'))
x = x ^ y
y = x ^ y
x = x ^ y
print('交换后 x 的值为：{}'.format(x))
print('交换后 y 的值为：{}'.format(y))
