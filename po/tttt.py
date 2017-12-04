# -*- coding:utf-8 -*-

class A(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def test(self):
        print self.age
        print self.name


class B(A):

    def __init__(self,name,age,grade):
        super(B, self).__init__(name,age)
        self.grade =grade

