# -*- coding: UTF -8 -*-
def is_number(s):
    try: #如果能运行float(s)语句，返回True（字符串是浮点数）
        float(s)
        return True
    except ValueError:# ValueError为Python的一种标准异常，表示“传入无效的参数”
        pass # 如果引发了ValueError这种异常，不做任何事情

    try:
        import unicodedata #处理ASSCii码的包
        for i in s:
            unicodedata.numeric(i) #把一个表示数字的字符串转换为浮点数返回的函数
        return True
    except (TypeError,ValueError):
        pass
    return False

# 测试字符串和数字
print(is_number('foo')) #False
print(is_number('1')) #True
print(is_number('1.3')) #True
print(is_number('-1.37')) #True
print(is_number('le3')) #True

# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥')) #True
#泰语 2
print(is_number('๒')) #True
# 中文数字
print(is_number('四')) #True
# 版权号
print(is_number('©')) #False

