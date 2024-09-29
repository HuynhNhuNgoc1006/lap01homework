#*Viết chương trình liệt kê tất cả bọ nghiệm nguyên của phương trình sau:
    # 2x+7y+9z=979 với (x,y,z > 0)
    
# 2*x + 7*1 + 9*1 = 979 => X = (979 - (7/9))/2 = 488.5 (490)
# 2*1 + 7*y + 9*1 = 979 > y = (979 - (2+9))/7 = 138.5 (140)
# 2*1 + 7*1 + 9*z = 979 > z (979 - (2+7))/9 = 108 (109-110)

bo_nghiem = []
for i in range(1,490):
    for y in range(1,140):
        for z in range(1,109):
            x = (979 - 7*y - 9*z)//2
            if x > 0:
                bo_nghiem += [(x,y,z)]
if bo_nghiem:
    print(f' {bo_nghiem}')               
