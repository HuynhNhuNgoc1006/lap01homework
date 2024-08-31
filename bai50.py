def kiem_tra_so(n):
  """Kiểm tra số nhập vào và trả về giá trị tương ứng

  Args:
    n: Số cần kiểm tra

  Returns:
    -1: Nếu n là số âm lẻ
    1:  Nếu n là số dương chẵn
    0:  Trong các trường hợp khác
  """

  if n < 0 and n % 2 != 0:
    return -1
  elif n > 0 and n % 2 == 0:
    return 1
  else:
    return 0


so = int(input("Nhập một số nguyên: "))
ket_qua = kiem_tra_so(so)

if ket_qua == -1:
  print("Số đã nhập là số âm lẻ.")
elif ket_qua == 1:
  print("Số đã nhập là số dương chẵn.")
else:
  print("Số đã nhập không phải là số âm lẻ hoặc số dương chẵn.")