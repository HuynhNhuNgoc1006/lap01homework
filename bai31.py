#. Nhập vào ba số nguyên dương. Kiểm tra xem 3 số đó có lập thành tam giác 
#không? Nếu có hãy cho biết tam giác đó thuộc loại nào? (Cân, vuông, 
#đều...)


a=int(input("Nhập cạnh a:"))
b=int(input("Nhập cạnh b:"))
c=int(input("Nhậ[ cạnh c:"))

if a>0 and b>0 and c>0:
    if a+b>c and a+c>b and b+c>a:
        print("Là tam giác")
        if a==b==c:
            print("Đều")
        elif a==b or a==c or b==c:
            print("Cân")
        elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
            print("Vuông")
        else:
            print("Thường")
    else:
        print("Không phải tam giác")
else:
    print("Vui lòng nhập các số nguyên ")
            