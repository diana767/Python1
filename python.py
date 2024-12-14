#1
a = [1, 1, 2, 3, 5, 8, 10, 12, 34, 38, 40, 41, 46, 50, 55, 89]
for element in a:
    if element < 15:
        print(element)

2
number = float(input("Введите число: "))
if number > 0:
    print("Положительное число")
elif number < 0:
    print("Отрицательное число")
else:
    print("Число равно нулю")

3
def calculator():
    print("Введите два числа:")
    a = float(input("Первое число: "))
    b = float(input("Второе число: "))
    
    print("Выберите операцию: +, -, *, /")
    operation = input("Операция: ")
    
    if operation == '+':
        print(f"Результат: {a + b}")
    elif operation == '-':
        print(f"Результат: {a - b}")
    elif operation == '*':
        print(f"Результат: {a * b}")
    elif operation == '/':
        if b != 0:
            print(f"Результат: {a / b}")
        else:
            print("Ошибка: деление на ноль")
    else:
        print("Неизвестная операция")

calculator()

#4
for i in range(10, 0, -1):
    print(i)

#5
import cmath

def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c  # Дискриминант
    sol1 = (-b + cmath.sqrt(d)) / (2 * a)
    sol2 = (-b - cmath.sqrt(d)) / (2 * a)
    return sol1, sol2

# Ввод коэффициентов
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

solutions = solve_quadratic(a, b, c)
print(f"Корни уравнения: {solutions[0]} и {solutions[1]}")

