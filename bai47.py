def tim_bo_nghiem_lon_nhat(a, b, c, d):
 
  ket_qua = []
  max_tong = 0

  for x in range(1, d//a + 1):
    for y in range(1, (d - a*x)//b + 1):
      z = (d - a*x - b*y) // c
      if z > 0:
        tong = x + y + z
        if tong > max_tong:
          ket_qua = [(x, y, z)]
          max_tong = tong
        elif tong == max_tong:
          ket_qua.append((x, y, z))

  return ket_qua

# Nhập các hệ số
a = 2
b = 7
c = 9
d = 979

# Tìm và in kết quả
ket_qua = tim_bo_nghiem_lon_nhat(a, b, c, d)
print("Các bộ nghiệm có tổng lớn nhất:", ket_qua)