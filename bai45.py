# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 09:13:07 2024

@author: Huỳnh Như Ngọc
"""

# S(n) = x + x^2/1+2 + x^3/1+2+3 +...+ x^n/1+2+3 +...+ n
 
s = 0
ts = 0
ms = 1
n = int(input("nhap n:"))
while n <=0:
    n = int(input("nhap n:"))
x = float(input("nhap x:"))
for i in range(1,n+1):
    ts = x**i
    ms = ms + i
    s += ts/ms
print(round(s,2))    