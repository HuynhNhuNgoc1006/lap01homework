# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 09:20:35 2024

@author: Huỳnh Như Ngọc
"""

# S(n) = 1/2 +3/4 +...+ 2n+1/2n+2
 
s = 0
n = int(input("nhap n:"))
while n <=0:
    n = int(input("nhap n:"))
    
for i in range(1,n+1):
    s += (2*i + 1)/(2*i + 2)
print(round(s,2))