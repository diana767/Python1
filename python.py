#1
a = [1, 1, 2, 3, 5, 8, 10, 12, 34, 38, 40, 41, 46, 50, 55, 89]
for element in a:
    if element < 15:
        print(element)

2
number = float(input("������� �����: "))
if number > 0:
    print("������������� �����")
elif number < 0:
    print("������������� �����")
else:
    print("����� ����� ����")

3
def calculator():
    print("������� ��� �����:")
    a = float(input("������ �����: "))
    b = float(input("������ �����: "))
    
    print("�������� ��������: +, -, *, /")
    operation = input("��������: ")
    
    if operation == '+':
        print(f"���������: {a + b}")
    elif operation == '-':
        print(f"���������: {a - b}")
    elif operation == '*':
        print(f"���������: {a * b}")
    elif operation == '/':
        if b != 0:
            print(f"���������: {a / b}")
        else:
            print("������: ������� �� ����")
    else:
        print("����������� ��������")

calculator()

#4
for i in range(10, 0, -1):
    print(i)

#5
import cmath

def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c  # ������������
    sol1 = (-b + cmath.sqrt(d)) / (2 * a)
    sol2 = (-b - cmath.sqrt(d)) / (2 * a)
    return sol1, sol2

# ���� �������������
a = float(input("������� ����������� a: "))
b = float(input("������� ����������� b: "))
c = float(input("������� ����������� c: "))

solutions = solve_quadratic(a, b, c)
print(f"����� ���������: {solutions[0]} � {solutions[1]}")

