#Tính tổng các chữ số N nguyên dương. 
#(Nhập N = 6789 thì 6+7+8+9 = 30)

N = int(input("Nhập số nguyên dương N: "))
tong = 0

for ch in str(N):
    tong += int(ch)
print("Tổng các chữ số của", N, "là:", tong)