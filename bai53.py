def tinh_tong_1_den_n(n):
  """Tính tổng các số từ 1 đến n bằng công thức tổng quát"""
  return n * (n + 1) // 2

def tinh_tong_binh_phuong(n):
  """Tính tổng các bình phương từ 1^2 đến n^2"""
  return n * (n + 1) * (2*n + 1) // 6

def tinh_tong_nghich_dao(n):
  """Tính tổng các số nghịch đảo từ 1/1 đến 1/n"""
  s = 0
  for i in range(1, n+1):
    s += 1/i
  return s

def tinh_giai_thua(n):
  """Tính giai thừa của n"""
  if n == 0:
    return 1
  else:
    return n * tinh_giai_thua(n-1)

def tinh_tich(n):
  """Tính tích các số từ 1 đến n"""
  tich = 1
  for i in range(1, n+1):
    tich *= i
  return tich


n = int(input("Nhập vào một số nguyên dương n: "))


print("Tổng các số từ 1 đến", n, "là:", tinh_tong_1_den_n(n))
print("Tổng các bình phương từ 1^2 đến", n**2, "là:", tinh_tong_binh_phuong(n))
print("Tổng các số nghịch đảo từ 1/1 đến 1/", n, "là:", tinh_tong_nghich_dao(n))
print(n, "! =", tinh_giai_thua(n))
print("Tích các số từ 1 đến", n, "là:", tinh_tich(n))