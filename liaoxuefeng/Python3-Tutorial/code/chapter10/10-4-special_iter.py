#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1 # ��ʼ������������a��b

    def __iter__(self):
        return self # ʵ��������ǵ������󣬹ʷ����Լ�

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # ������һ��ֵ
        if self.a > 100000: # �˳�ѭ��������
            raise StopIteration();
        return self.a # ������һ��ֵ

for n in Fib():
    print(n)