import math
a=float(input("Nhập số thưc a:"))
b=float(input("Nhập số thực b:"))
S= ((math.pow(a, 1/2)-math.pow(b, 1/2))/(math.pow(a, 1/4)-math.pow(b, 1/4)))-((math.pow(a, 1/2)+math.pow(a*b, 1/4))/(math.pow(a, 1/4)+math.pow(b,1/4)))
print("Kết quả là: ",S)