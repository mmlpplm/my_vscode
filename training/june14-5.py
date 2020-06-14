# -*- coding: UTF -8 -*-
# 判断闰年
year = int(input('请输入一个年份:'))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print('{} 是闰年'.format(year)) # 整百年能被400整除的是闰年
        else:
            print('{} 不是闰年'.format(year))
    else:
        print('{} 是闰年'.format(year)) # 非整百年能被4整除的是闰年
else:
    print('{} 不是闰年'.format(year))
