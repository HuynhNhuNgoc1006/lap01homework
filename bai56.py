import math

def tinh(*args, **kwargs):
    hinh = kwargs.get('hinh', None)
    tinh = kwargs.get('tinh', None)
    
    if hinh == 'vuong':
        if tinh == 'cv':
            return 4 * args[0]
        elif tinh == 'dt':
            return args[0] ** 2
    elif hinh == 'chu_nhat':
        if tinh == 'cv':
            return 2 * (args[0] + args[1])
        elif tinh == 'dt':
            return args[0] * args[1]
    elif hinh == 'tron':
        if tinh == 'cv':
            return 2 * math.pi * args[0]
        elif tinh == 'dt':
            return math.pi * (args[0] ** 2)


print(tinh(10, hinh='vuong', tinh='cv'))
print(tinh(50, hinh='vuong', tinh='dt'))
print(tinh(18, hinh='tron', tinh='cv'))
print(tinh(20, 30, hinh='chu_nhat', tinh='cv'))
