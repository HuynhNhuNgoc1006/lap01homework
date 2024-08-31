def tinh_chu_vi(a, b):
    chu_vi = 2 * (a + b)
    return chu_vi


def tinh_dien_tich(a, b):
    dien_tich = a * b
    return dien_tich


chieu_dai = 4
chieu_rong = 6

chu_vi = tinh_chu_vi(chieu_dai, chieu_rong)
dien_tich = tinh_dien_tich(chieu_dai, chieu_rong)

print("Chu vi hình chữ nhật là:", chu_vi)
print("Diện tích hình chữ nhật là:", dien_tich)



def ve_hinh_chu_nhat(a, b):
    for i in range(a):
        for j in range(b):
            print("*", end="")
        print()


chieu_dai = 4
chieu_rong = 6

ve_hinh_chu_nhat(chieu_dai, chieu_rong)