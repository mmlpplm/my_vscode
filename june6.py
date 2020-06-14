# 1-100个数字，打印，但是要求逢3和3的倍数不打印


for i in range(1, 101):  # 遍历1-100，用i接收
    if i % 3 == 0:  # 3的倍数就是除3的余数等于0
        continue  # 跳过
    elif i % 10 == 3:  # 个位数为3就是除10余数等于3
        continue
    elif i // 10 == 3:  # 十位数为3就是取整除10商的整数部分等于3
        continue
    else:
        print(i)

