#. Viết chương trình nhập vào số nguyên dương n. Kiểm tra xem n có phải là
#số nguyên tố hay không


n=int(input("Nhập số nguyên dương n:"))

#Khởi tạo cờ kiểm tra, mặc định là số nguyên tố
la_so_nguyen_to = True

#Kiểm tra xem n có chia hết cho số nào từ 2 đến bậc 2 của n ko
if n <= 1:
    la_so_nguyen_to = False
else:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            la_so_nguyen_to = False
            break
if la_so_nguyen_to:
 print(n, "là số nguyên tố")
else:
 print(n, "không phải số nguyên tố ")       