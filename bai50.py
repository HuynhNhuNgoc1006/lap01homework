# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:03:57 2024

@author: Huỳnh Như Ngọc
"""

# Viết phương thức kiểm tra một số nhập vào: nếu là số âm có giá trị lẻ thì 
#trả về -1, nếu là số dương có giá trị chẵn thì trả về 1, trường hợp khác trả
#về 0

number = int(input("Nhập một số nguyên: "))

if number < 0 and number % 2 != 0:
            print(-1)
elif number > 0 and number % 2 == 0:
            print(1)
else:
            print(0)