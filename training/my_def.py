# -*- coding: UTF -8 -*-

import os  # 利用import语句进行导入模块，通常以一个tab的距离表示隶属关系
import math,copy,random,time
from collections import Counter  # 利用from...import...进行导入
import numpy as np  # 利用as关键字重命名包名，以后再使用就可以直接用np了

def hello_world():  # 利用def关键字创建函数，函数就是具有独立功能的代码块，需要的时候调用
    # 创建函数格式：def name(参数1，参数2...)
    your_name = input('你好，请输入你的名字：')
    print('欢迎,',your_name)
    print("让我们开始学习Pthon!let's go!")

def hello_twice():
    global your_name,your_height,your_weight
    your_name = input('请输入你的名字：')
    your_height = input('请输入你的身高：')
    your_weight = input('请输入你的体重：')


def deviding_line():
    word_1 = 'i am line'
    word_2 = word_1.upper()  #upper()可以将字符串转换为全大写字母
    word_3 = word_1.lower()  #lower()可以将字符串转换为全小写字母
    word_4 = word_1.title()  #title()可以将字符串标题化

    words = [word_1,word_2,word_3,word_4] # 创建列表
    line = '_'* 40  # 利用*运算符创建串，这里是生成40个_符号

    endReturn = line + words[random.randint(0,3)]+line
    # 字符串可以利用+符号直接相连，rendom.randint()可以创建随机整，0和3是上下限
    return endReturn #返回值，可以在被调用时将之歌值返回

def study_number():
    number_1 = input('请输入一个数字：')
    print('你输入的是数字 %s'%number_1,'它的类型为：',type(number_1)) #  %s,表示格式化一个对象为字符
    number_2 = int(input('再输入一个数字：'))
    print('你输入的是数字%s'% number_2,'它的类型是：',type(number_2))
    number_3 = float(input('再输入一个数字：'))
    print('你输入的是数字%s'% number_3,'它的类型是：',type(number_3))
    print('number_1+number_2={}'.format(int(number_1)+number_2))
    print('number_1-number_2={}'.format(int(number_1)-number_2))
    print('number_1*number_2={}'.format(number_1*number_2))
    print('number_1*number_2={}'.format(int(number_1)*number_2))
    print('number_2//number_3={:.3f}'.format(number_2//number_3)) # ‘//’为整除，‘{:.3f}'为输出小数点后保留三位
    print('number_2/number_3={:.4f}'.format(number_2/number_3))
    print('number_2%number_3={:.4f}'.format(number_2%number_3))  # '%'为求余
    print('number_2%number_3={:.4%}'.format(number_2%number_3))  # '{.4%}'为输出格式为百分比
    print('number_1**number_2={}'.format(int(number_1)**number_2))  # '**'为冥运算
    print('This is the {a},and {b}'.format(a='numbers',b='some operations')) # format多参数，标记位置对应输出
    
def true_false():
    one,two,three = True,True,False
    print(one,two,three)
    print('and运算:',one and two , one and three)
    print('or运算：',one or two ,one or three)
    print('not运算:',not one,not two,not three)

def study_list(length):  # 带参数函数，必须要传入参数
    l1 = [1,2,3,4,5,9.0] # 创建列表 用[]
    l2 = list(range(10,10+length)) # 也可以用list()来创建列表
    # range()函数，可以创建一个整数列表，格式为range(start,end,step)，
    # start为开始位置，end为结束位置，前闭后开，step为步长
    print('l1的类型为: ',type(l1))
    print(l1[1],l2[1]) # 访问列表值，可以直接用list[num]的方式进行访问
    l3 = l2
    print(id(l1),id(l2),id(l3)) # id()函数可以获取对象的内存地址，在这里可以看到l3的的地址和l2是一样的
    l3[0]=99 # 更新列表值
    print('l2==l3么?',l2==l3)
    l4 = l2.copy() # 复制一个l2给l4，copy()创建一个一模一样的列表
    l4[0]=999
    print('l4==l2么?',l4==l2)
    print('删除前',l4)
    del l4[0] # del语句进行删除列表值，在python中del可以删除所有的变量
    print('删除后',l4) 
    l4.append(30) # 给列表添加值
    l4.extend(l1) # 给列表追加一个序列多个值
    print('添加l1后:',l4)
    l4.reverse() # 列表反转
    print('反转后:',l4)
    l4.sort() # sort()函数，将列表进行排序
    print('排序后:',l4)

def study_tuple(length:int)->bool: # 解释参数类型的函数创建，->为返回值类型
    tuple1 = (1,2,3,4) # 创建元组，利用()符号，元组的特性是不可以改变
    tuple2 = tuple(range(10,10+length)) # 利用tuple()创建元组
    print(tuple1.count(1)) # 组函数count(),用于输出某个值的数量
    print(tuple1.index(1)) # 元组函数index(),可以按照值得到下标号位置
    try:  # try:语句内部如果出现错误则会转入到except中
        tuple[0] = 9 # 因为元组的不可改变性，所以该语句会出错
    except TypeError: 
        print('元组插入失败')
    finally: # finally内语句不管是否出现错误都会执行
        print('不管插入成不成功我都会执行')
    try:
        print(id(tuple1),id(tuple2))
    except :
        return False
    else:
        tuple3 = tuple1+tuple2 # 元组虽然不可改变，但是可以通过+号进行合并为另一个元组
        print(tuple3,id(tuple3))
    return True

def study_dict():
    dict1 = {1:'一',2:'二',3:'三',4:'四'}
    dict2 = dict(one=1,two=2,three=3)
    dict3 = dict(zip([6,7,8,9],['Six','Seven','Eight','Nine']))
    dict4 = dict([('One',1),('Two',2),('Three',3)])
    dict5 = dict({1:'一',2:'二',3:'三',4:'四'})
    # 以上为创建字典的5种方法
    print(type(dict1),dict1==dict5)
    print(dict1[1],dict2['one'],dict3[6],dict4['One'],dict5[1])
    print(dict1.get(4)) # 过get函数访问内容

    dict1[1] = '壹' # 修改字典内容
    dict1[5] = '五' # 添加字典
    print(dict1)
    print(1 in dict1, 6 in dict1, 7 not in dict1)
    dict6 = dict1.copy() # 字典的复制
    dict6[1] = 'One'
    print(dict1,'<dict1-----------dict6>',dict6)

    dict1.clear() # 字典的清空
    print(dict1)
    del dict1,dict2,dict3,dict4,dict5,dict6 # 删除字典,也可以用del dict[key]的方式删除某个键

def study_set(): # python中集合的学习，集合中不存在相等的值
    set1 = set(['You','Are','Not','Beautiful']) # 利用set()函数进行创建集合
    set2 = {'You','Are','So','Beautiful'} # 利用{}创建集合，创建空集合的时候不能用{},因为{}表示字典
    set3 = set2.copy() # 集合的复制

    print(type(set1))
    print(set1,set2)
    print(set1|set2) # 或运算符，得到两个集合中所有元素
    print(set1&set2) # 与运算符，得到两个集合共同元素
    print(set1^set2) # 不同时包含于set1和set2的元素
    print(set1-set2) # 集合差运算，得到set1有，set2没有的元素
    print(set1<=set2,set3<=set2,set3<set2)

    set1.add('Me too') # 集合添加元素
    print('is语句用法',set3==set2,set3 is set2,set1 is not set2)
    set3.clear() # 清空集合，集合变为空
    print(set3)
    del set3

def study_Some_functions():
    list1 = [1,2,3,4,5,6]
    tuple1 = (11,12,13,14,15,16)
    set1 = set(list1)
    dict1 = dict(zip([1,2,3,4,5],['one','Two','Three','Four','Five']))

    print(max(list1),max(tuple1),max(set1),max(dict1))
    print(min(list1),min(tuple1),min(set1),min(dict1))
    print(sum(list1),sum(tuple1),sum(set1),sum(dict1))
    print(len(list1),len(tuple1),len(set1),len(dict1))
    print(divmod(list1[0],tuple1[0]))  # divmod()函数，计算两个数的商和余数，结果两个格式为(商，余数)
    # 意思为divmod的（）内第一个数除以第二个数，得到商和余，返回的格式是前面是商后面是余
    print(list(enumerate(tuple1))) # enumerate()，给元组添加一个索引

    list2 = list(tuple1) # 利用list()将元组，字典等等转换为列表
    list3 = list(set1)
    list4 = list(dict1)
    tuple2 = tuple(list1) # 利用tuple()将列表，字典等转换为元组

    print(list2,list3,list4)

    for i in range(len(list1)):
        print(list1[i],end=' ') # print的属性end，可以使输出格式为end的内容，而不是默认换行
    print()
    for i in dict1:
        print(i,dict1[i],end=' ')
    list5 = list(reversed(list1)) # reversed()函数，可以反转序列
    print('\n',list5) # \n,换行符

    testStr = 'The mountains and rivers are different,the wind and the moon are the same'
    words = testStr.split(' ') # split()函数，以split()内参数分割字符串，返回一个列表
    print(words)
    words.sort(key=len) # sort()函数，进行排序，参数key=len时，以字符串长度为标准排序
    print('以长度排序:',words)
    words.sort(key=len,reverse=True) # reverse参数，结果反转
    print('以长度排序且反转:',words)
    words.sort(key=str) # 以字典序进行排序
    print('以字典排序:',words)

    ct = Counter(testStr) # collections模块中的Counter,可以得到字符串中每个数字出现次数
    print(ct)
    ct.update('eeeexxxxxlllll') # 更新
    print(ct)
    print(ct.most_common(5)) # 得到字符数最多的前五位


def study_slice(): # 切片操作，得到序列的部分内容
    str1 = 'I hope one day,I can find you, my sweet dream'
    list1 = list(range(10))
    tuple1 = tuple(list1)

    print(str1[:]) # 切片格式为str[start:end:step]，前闭后开,step可为正负，默认步长为1
    print(str1[::-1]) # 当步长为负数的时候，反转
    print(str1[:15]) # 只有end时，截取最开始到end
    print(str1[15:]) # 只有start时，截取从start到末尾的所有字符
    print(str1[::2]) # 步长为2
    print(str1[1::2])

    print(list1[::]) # 和str一样
    print(list1[2:])
    print(list1[:2])
    print(list1[::-1])

    list1[1:5] = [10] # 切片赋值，右边必须为一个可以遍历的序列
    # #list1[1:5] = 10   这样就会报错
    print(list1)

def study_loop_select(): # 循环和选择
    list1 = [1,2,3,4,5]
    num = int(input('while循环，输入你想要循环的次数：'))
    i = 1
    while i<=num: # while expression:当expression为真的时候进行循环
        if i<5: # if...elif...else选择语句，如果判断结果只有两个,可以使用if...else
            print('我打印了',i,'次')
        elif i < 10:
            print('我打印了',i,'次，真累啊')
        elif i<15:
            print('我打印太多了，再打印我就要停止了...')
        elif i<20:
            print('continue...')
            i+=1
            continue # continue语句，用在循环中，continue后的所有语句都不允许，直接进入下次循环
            print('我想我可能输出不了了')
        else:
            print('累死我了，休息，都',i,'次了~_~')
            break # break语句，运用在循环中，直接退出循环，所以，在本例子中，这个循环最多循环20次
        i+=1
        time.sleep(0.5) # time库为python中的时间库，time.sleep(second)可以使程序暂停运行second秒
    else: # while循环后接一个else语句，当执行完所有循环后执行一次，可以省略(个人感觉用处不大)
        print('while结束了')

    for i in list1:
        print(i,end=' ')
    print()
    for i in range(5):
        print(i)


def study_expression_deduction(): # 表达式推导
    list1 = [i for i in range(10)] # 利用该语句推导出列表
    list2 = [x for x in range(20) if x%2==0] # 语句中增加if，满足if后表达式的才会是列表
    print(list1,'<list1----------------list2>',list2)

    print(deviding_line()) # 函数可以在任何地方被调用，如果是自己调用自己就可以称为递归调用

    list3 = [['_'] * 3 for i in range(3)]
    print(list3)

    fruits = ['Apple','Banana','Pear']
    colors = ['Red','Yellow','Green']
    suitcolor = [(color,fruit) for color,fruit in zip(colors,fruits)]
    # 两个列表合并
    print(suitcolor)
    cartesian = [(color,fruit) for color in colors for fruit in fruits]
    # 两个列表的笛卡尔积
    print(cartesian)

    dict1 = {fruit:color for fruit,color in suitcolor}
    # 字典的推导，只要是带有键值对的任何序列，都可以推导出字典
    print(dict1)


def study_files():
    filepath = input('请输入你的文件路径(输入quit退出):')
    if filepath=='quit':
        return True

    try:
        file = open(filepath,'w') # 打开文件，'w'为写格式打开
        file.write('哈哈，现在开始写文件.\n 今天是6月26日')
        # 向文件写入字符串
        file.close() # 关闭文件
        file = open(filepath,'r') # 以'r'读格式打开
        print('从文件中读出的内容: \n',file.read()) # read()函数可以得到文件内容
    except FileNotFoundError:
        print('文件未找见请重新输入')
        study_files() # 函数可以在任何地方被调用，如果是自己调用自己就可以称为递归调用
    except:
        print('出现错误，请重新输入路径')
        study_files()

class Users(): # 面向对象编程，python中创建类class，类包含有属性与方法，包括有私有变量，共有变量等等
    def __init__(self,name,height,weight): # 类的构造方法，创建实例时自动调用
        self.name = name
        self.height = height
        self.weight =weight
        self.yanzhi = 100

    def display(self): # 类方法
        print('大家好，我是{},身高{}公分,体重{}公斤,颜值超高{}分'.format(self.name,self.height,self.weight,self.yanzhi))

if __name__=='__main__': # 无论之前有什么，程序都会从这里开始运行
    hello_world() # 所以这是运行的第一句，调用该函数
    print(deviding_line()) # 调用deviding_line函数，由于该函数没有打印方法，故直接加print语句打印出来
    try:
        print(your_name) # 调用完hello_world()函数后，因为在hello_world()函数内部有一个your_name变量，所以我们进行输出，看在这里能不能找见这个变量
    except:
        print('  未能找到该变量  ') # 不可能找见这个变量的，因为your_name是局部变量，只存在于hello_world()函数内部
    print(deviding_line()) # # 调用deviding_line函数，由于该函数没有打印方法，故直接加print语句打印出来
    hello_twice() # 因为在该函数中定义了global语句，所以该函数中的变量在以下程序中都可以使用

    user = Users(your_name,your_height,your_weight) # 实例化对象，创建Users类的实例
    user.display() # 对象调用方法


chooseinformation = '''Input the number of the function you want to Run(quit is exit):
1、study_unmber    2、study_list
3、study_tuple     4、study_dict
5、study_set       6、study_Some_functions
7、study_Slice     8、study_loop_select
9、study_expreesion_deduction
10、study_files
'''

print(deviding_line())
while True:
    input('按键继续')
    print(chooseinformation)
    num = input('输入序号')

    if num == 'quit':
        break
    elif num =='1':
        study_number()
    elif num =='2':
        study_list(10)
    elif num == '3':
        study_tuple(10)
    elif num =='4':
        study_dict()
    elif num =='5':
        study_set()
    elif num =='6':
        study_Some_functions()
    elif num =='7':
        study_slice()
    elif num =='8':
        study_loop_select()
    elif num =='9':
        study_expression_deduction()
    elif num =='10':
        study_files()
    print(deviding_line())
print('哈哈，恭喜你，这个程序结束了~')







