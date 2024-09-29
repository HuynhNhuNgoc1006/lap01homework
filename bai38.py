# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:44:43 2024

@author: Huỳnh Như Ngọc
"""

# Tính S = 1*2*3*...*n (với n lẻ >0)

n = int(input("nhap so le n:"))
s = 1
for i in range(1,n+1,2):
    s *= i
print("tich s = ",s)