def la_so_chan_am(n):
  """Kiểm tra xem một số có phải là số chẵn âm hay không

  Args:
    n: Số cần kiểm tra

  Returns:
    True: Nếu n là số chẵn âm
    False: Nếu n không phải là số chẵn âm
  """

  return n < 0 and n % 2 == 0

# Ví dụ sử dụng:
so = int(input("Nhập một số nguyên: "))
if la_so_chan_am(so):
  print("Số đã nhập là số chẵn âm.")
else:
  print("Số đã nhập không phải là số chẵn âm.")