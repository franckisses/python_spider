#-*- coding: utf-8 -*-
"""
 @Time    : 2018/8/27 15:34
 @Author  : franck
 @place : china
 @Email   : franck_gxu@outlook.com
"""

# 闭包:如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，
# 那么内部函数就被认为是闭包(closure)
#如果调用外部函数的话,会返回一个内部函数的对象,

# 内嵌函数
def Fun1():
    print("fun1正在被调用")
    def fun2():  #内嵌函数
        print("fun2正在被调用")
    fun2()
Fun1()

# 闭包 函数是编程的重要的语法结构
#
def Funx(x):
    def fun(y):
        return  x*y
    return fun
a = Funx(1)
print(a)
print(a(10))
print(Funx(5)(8))

# 在内部函数中只能对外部函数得局部变量进行访问,但不能修改,
# def out():
#     a = 1
#     def inside():
#         a += 1
#         return a
#     inside()
#
# out()
# 返回的错误是在引用之前没有被定义

# 如果需要修改内部函数的外部函数的局部变量的时候 需要先将其加上nonlocal声明一下
def out():
    a = 1
    def inside():
        nonlocal a
        a += 1
        return a
    return inside()

print(out())

#
flist = []
for i in range(3):
    def foo(x):
        print(x + i)
    flist.append(foo)
for f in flist:
    f(2)
# print(flist)

# 闭包的用途:
# 1.当闭包执行完后，仍然能够保持住当前的运行环境
#2.闭包可以根据外部作用域的局部变量来得到不同的结果，这有点像一种类似配置功能的作用，
# 我们可以修改外部的变量，闭包根据这个变量展现出不同的功能
