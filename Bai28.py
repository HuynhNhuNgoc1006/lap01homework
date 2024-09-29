#. Nhập vào số N từ bàn phím (điều kiện N nguyên dương) nếu người dùng 
 #nhập không đúng thì bắt nhập lại. Sao đó in ra tất cả ước số của N


while True:
    N = int(input("Nhập vào số nguyên dương N:"))
    if N > 0:
        break
    else:
        print("Vui lòng nhập số nguyên dương.")
        print("Định dạng nhập không hợp lệ. Vui lòng nhập số nguyên.")
print("Các ước số của",N, "là:")
for i in range(1,N+1):
            if N % i==0:
                print(i)