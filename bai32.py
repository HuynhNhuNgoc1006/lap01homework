#Viết chương trình tính tiền cước TAXI. Biết rằng: 1 km đầu tiên là 15000đ, 
#từ km thứ 2 đến thứ 5 giá là 13500đ, từ km thứ 6 giá là 11000đ, nếu đi 
#hơn 120km thì sẽ được giảm 10% trên tổng tiền.


#Nhập số km di chuyển
so_km = float(input("Nhập số km di chuyển:"))

#Khởi tạo biến lưu trữ tổng tiền
tong_tien = 0

#Tính tiền cho các khoản km khác nhau
if so_km <=1:
    tong_tien = 15000
elif so_km <=5:
    tong_tien = 15000 + (so_km-1)*135000
else:
    tong_tien = 15000 + 4 *13500 + (so_km-1)*11000
#Áp dụng giảm giá nếu đủ điều kiện
if so_km >120 :
    tong_tien *= 0.9
print("Tổng số tiền phải trả là:",tong_tien,"đồng")