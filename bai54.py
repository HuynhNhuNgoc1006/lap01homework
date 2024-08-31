def fibonacci(n):
    fib_list = [0, 1]
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_list
    
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    
    return fib_list

n = 10  
result = fibonacci(n)
print(result)
