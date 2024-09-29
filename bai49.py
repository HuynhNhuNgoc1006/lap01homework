# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:03:03 2024

@author: Huỳnh Như Ngọc
"""

# Viết phương thức kiểm tra một số nhập vào là số chẵn có giá trị âm. Đúng 
#trả về true. Sai trả về false.

number = int(input("Nhập một số nguyên: "))

if number % 2 == 0 and number < 0:
    print("true")
else:
    print("false")