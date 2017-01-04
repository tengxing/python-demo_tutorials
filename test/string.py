#!/usr/bin/python3
counter=100
name = "tengxin"
mailes= 1990.1
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')
#! 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号(())里#! 元素之间用逗号隔开。
print (tuple)             #! 输出完整元组
print (tuple[0])          #! 输出元组的第一个元素
print (tuple[1:3])        #! 输出从第二个元素开始到第三个元素
print (tuple[2:])         #! 输出从第三个元素开始的所有元素
print (tinytuple * 2)     #! 输出两次元组
print (tuple + tinytuple) #! 连接元组
tup1 = ()    #! 空元组
tup2 = (20,) #! 一个元素，需要在元素后添加逗号

#! 集合（set）是一个无序不重复元素的序列。
#! 基本功能是进行成员关系测试和删除重复元素。
#! 可以使用大括号({})或者 set()函数创建集合，注意：创建一个空集合必须用 set() 而#! 不是 { }，因为 { } 是用来创建一个空字典
student = ({'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'},{'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'})

print(student)   #! 输出集合，重复的元素被自动去掉
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)     #! a和b的差集

print(a | b)     #! a和b的并集

print(a & b)     #! a和b的交集

print(a ^ b)     #! a和b中不同时存在的元素
#! 字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


print (dict['one'])       #! 输出键为 'one' 的值
print (dict[2])           #! 输出键为 2 的值
print (tinydict)          #! 输出完整的字典
print (tinydict.keys())   #! 输出所有键
print (tinydict.values()) #! 输出所有值

print (counter)
print ( name[0:1])
print ( mailes)
