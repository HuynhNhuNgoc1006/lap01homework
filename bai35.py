#. Tính S = 1 + 2 + 3 + ... + n 
#(n nguyên và lớn hơn 0)

n=int(input("Nhập số nguyên dương n:"))
S = 0
for i in range(n, n+1):
    S += i
print("Tổng S = ",S)