# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:58:04 2024

@author: Huỳnh Như Ngọc
"""

# Tính S(n) = 1 + 1/2 + 1/3 +...+ 1/n

n = int(input("nhap gia tri n:"))
s = 0
for i in range(1,n+1):
    s += 1/i
print("tong s =",s)

