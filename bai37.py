# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:41:20 2024

@author: Huỳnh Như Ngọc
"""

# Tính S = 2+4+6+...+n (với n chẵn 0)
  

n = int(input("nhap so chan n:"))
s = 0
for i in range(2,n+1,2):
    s += i
print("tong s = ",s)