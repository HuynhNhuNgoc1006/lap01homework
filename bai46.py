def tim_nghiem(x, y, z, target):
    """
    Hàm đệ quy tìm kiếm nghiệm
    x, y, z: Giá trị hiện tại của các biến
    target: Giá trị đích (979)
    """
    if 2*x + 7*y + 9*z == target:
        print(f"Nghiệm: x = {x}, y = {y}, z = {z}")
    if 2*x + 7*y + 9*z < target:
        for i in range(x+1, target//2+1):
            tim_nghiem(i, y, z, target)
        for j in range(y+1, (target-2*x)//7+1):
            tim_nghiem(x, j, z, target)
        for k in range(z+1, (target-2*x-7*y)//9+1):
            tim_nghiem(x, y, k, target)

# Giá trị đích
target = 979

# Khởi tạo tìm kiếm từ x = 1, y = 1, z = 1
tim_nghiem(1, 1, 1, target)