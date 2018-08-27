#-*- coding: utf-8 -*-
"""
 @Time    : 2018/8/27 19:32
 @Author  : franck
 @Email   : franck_gxu@outlook.com
"""
# 类方法和静态方法


# 类方法 我们在调用类的方法的时候 可以不通过实例来调用
# @classmethod 可以实现这种功能

class A(object):
    bar = 1
    @classmethod
    def calss_foo(cls):
        print('hello',cls)
        print(cls.bar)

A.calss_foo() #可以用过类来直接调用类方法,而不用去创建实例变量


# 静态方法
# 静态方法没有 self 和 cls 参数，可以把它看成是一个普通的函数，
# 我们当然可以把它写到类外面，但这是不推荐的
# 因为这不利于代码的组织和命名空间的整洁。
class B(object):
    bar = 1
    @staticmethod
    def static_foo():
        print("hello",A.bar)

b = B()
b.static_foo()

