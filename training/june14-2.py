# -*- coding: UTF -8 -*-
number = float(input('请输入一个数字：'))
if number > 0:
    print('正数')
elif number == 0:
    print('零')
else:
    print('负数')

# 写法2 内嵌if语句
number = float(input('请输入一个数字：'))
if number >= 0:
    if number == 0:
        print('零')
    else:
        print('正数')
else:
    print('负数')

# 写法3 优化增加异常输出
while True:
    try:
        number = float(input('请输入一个数字: '))
        if number == 0:
            print('零')
        elif number > 0:
            print('正数')
        else:
            print('负数')
        break
    except ValueError:
        print('输入无效，需要输入一个数字')
# 写法3 最好，多学习学习