import itertools

def solve_equation(x, y, z):
    return 2*x + 7*y + 9*z - 979

def find_max_sum(x, y, z):
    return x + y + z

def find_all_solutions():
    max_sum = 0
    solutions = []
    for x in range(1, 100):  # assuming x, y, z <= 100
        for y in range(1, 100):
            for z in range(1, 100):
                if x + y + z > max_sum:
                    max_sum = x + y + z
                    solutions = [(x, y, z)]
                elif x + y + z == max_sum:
                    solutions.append((x, y, z))
                if solve_equation(x, y, z) == 979:
                    solutions.append((x, y, z))
    return solutions

solutions = find_all_solutions()
print("Solutions:")
for solution in solutions:
    print(solution)