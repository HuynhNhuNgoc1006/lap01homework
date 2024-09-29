#. Tính S = 1**2 + 2**2 + 3**2 + ... + n**2
#(n nguyên và lớn hơn 0)

n=int(input("Nhập số nguyên dương n:"))
S = 0
for i in range(1, n+1):
    S += i**2
print("Tổng S = ",S)