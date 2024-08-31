def kiem_tra_gia_tri(min_value, max_value):
  """Kiểm tra giá trị nhập vào có nằm trong khoảng [min_value, max_value] không

  Args:
    min_value: Giá trị nhỏ nhất của khoảng
    max_value: Giá trị lớn nhất của khoảng

  Returns:
    Giá trị hợp lệ nằm trong khoảng
  """

  while True:
    try:
      gia_tri = int(input(f"Nhập giá trị trong khoảng [{min_value}, {max_value}]: "))
      if min_value <= gia_tri <= max_value:
        return gia_tri
      else:
        print("Giá trị không hợp lệ. Vui lòng nhập lại.")
    except ValueError:
      print("Giá trị nhập vào không phải là số nguyên. Vui lòng nhập lại.")


gia_tri_hop_le = kiem_tra_gia_tri(-89, 90)
print("Giá trị hợp lệ:", gia_tri_hop_le)