# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:10:19 2024

@author: Huỳnh Như Ngọc
"""

# Tính S(n) = 1+ 1/3 + 1/5 +...+ 1/2n+1

s = 0
n = int(input("nhap gia tri n:"))
for i in range(n+1):
    s += 1 / (2*i+1)
print("tong s =",s)
