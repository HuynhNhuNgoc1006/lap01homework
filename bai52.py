import math

def tinh_can_bac_x(n, x):
  """Tính căn bậc x của số n"""
  return n**(1/x)

def dao_so(n):
  """Trả về số đảo của n"""
  dao = 0
  while n > 0:
    dao = dao * 10 + n % 10
    n //= 10
  return dao

def la_so_chinh_phuong(n):
  """Kiểm tra xem n có phải là số chính phương hay không"""
  can_bac_hai = int(math.sqrt(n))
  return can_bac_hai * can_bac_hai == n

def la_so_nguyen_to(n):
  """Kiểm tra xem n có phải là số nguyên tố hay không"""
  if n <= 1:
      return False
  if n <= 3:
      return True
  if n % 2 == 0 or n % 3 == 0:
      return False
  i = 5
  while i * i <= n:
      if n % i == 0 or n % (i + 2) == 0:
          return False
      i += 6
  return True

def tich_chu_so_le(n):
  """Tính tích các chữ số lẻ của n"""
  tich = 1
  while n > 0:
    chu_so = n % 10
    if chu_so % 2 != 0:
      tich *= chu_so
    n //= 10
  return tich

def tong_so_nguyen_to_nho_hon(n):
  """Tính tổng các số nguyên tố nhỏ hơn n"""
  tong = 0
  for num in range(2, n):
    if la_so_nguyen_to(num):
      tong += num
  return tong

def tong_so_chinh_phuong_nho_hon(n):
  """Tính tổng các số chính phương nhỏ hơn n"""
  tong = 0
  for num in range(1, int(math.sqrt(n)) + 1):
    tong += num * num
  return tong

def tong_uoc_so(n):
  """Tính tổng các ước số dương của n"""
  tong = 0
  for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
      tong += i + n // i
 
  if int(n**0.5) * int(n**0.5) == n:
      tong -= int(n**0.5)
  return tong


n = int(input("Nhập số nguyên dương n: "))


print("Căn bậc 2 của", n, "là:", tinh_can_bac_x(n, 2))
print("Số đảo của", n, "là:", dao_so(n))
print(n, "là số chính phương" if la_so_chinh_phuong(n) else "không phải số chính phương")
print(n, "là số nguyên tố" if la_so_nguyen_to(n) else "không phải số nguyên tố")
print("Tích các chữ số lẻ của", n, "là:", tich_chu_so_le(n))
print("Tổng các số nguyên tố nhỏ hơn", n, "là:", tong_so_nguyen_to_nho_hon(n))
print("Tổng các số chính phương nhỏ hơn", n, "là:", tong_so_chinh_phuong_nho_hon(n))
print("Tổng các ước số dương của", n, "là:", tong_uoc_so(n))