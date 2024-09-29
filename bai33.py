#. Viết chương trình nhập vào số nguyên dương n. Kiểm tra xem n có phải là 
#số chính phương hay không? (Số chính phương là số khi lấy căn bậc 2 có 
#kết quả là nguyên).


import math
n=int(input("Nhập số nguyên dương n:"))

#Tính căn bậc hai của n
can_bac_hai = math.sqrt(n)

#Kiểm tra xem phần thập phân của căn bậc hai có bằng 0 không
if can_bac_hai - int(can_bac_hai) == 0:
    print(n,"là số chính phương")
else:
    print(n,"không phải là số chính phương")