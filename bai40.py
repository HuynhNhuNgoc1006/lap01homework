# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:04:52 2024

@author: Huỳnh Như Ngọc
"""

# Tính S(n) = 1/2 + 1/4 +...+ 1/2n

s = 0
n = int(input("nhap gia tri n:"))
for i in range(1,n+1):
    s += 1/(2*i)
    print("tong s =",s)