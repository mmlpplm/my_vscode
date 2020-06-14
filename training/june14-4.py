# -*- coding: UTF -8 -*-
# 判断奇偶数
# 如果是偶数除于2余数等于0，如果是奇数除于2余数等于1

number = int(input('请输入一个数字：'))
if (number % 2) == 0:
    print('{} 是偶数'.format(number))
else:
    print('{} 是奇数'.format(number))
    
#写法2 优化加入判断
while True:
    try:
        number = int(input('请输入一个整数：'))#判断输入是否为整数
    except ValueError:#输入的不是纯数字需要重新输入
        print('你输入的不是整数！')
        continue
    if number % 2 == 0:
        print('{} 是偶数'.format(number))
    else:
        print('{} 是奇数'.format(number))
    break

#写法3  简洁
number = eval(input('Number:\n'))
print('{} 是'.format(number) + ('偶数' if number % 2 == 0 else '奇数'))
