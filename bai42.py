# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:14:20 2024

@author: Huỳnh Như Ngọc
"""

# Tính S(n) 1/1*2 + 1/2*3 +...+ 1/n*(n+)

n = int(input("nhap gia tri n:"))
s = 1 - 1/(n+1)
print("tong s =",s)