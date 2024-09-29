#Nhập tháng, năm. Hãy cho biết tháng đó có bao nhiêu ngày

thang = int(input("Nhập vào tháng:"))
nam = int(input("Nhập vào năm:"))
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    print("Tháng có 31 ngày")
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    print("Tháng có 30 ngày")
else:
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 !=0):
        print("Tháng có 29 ngày")
    else:
        print("Tháng có 28 ngày")
    