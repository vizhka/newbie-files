import math
a = int(input("Введите значение a="))
b = int(input("Введите значение b="))
c = int(input("Ввежите значение c="))
d = b ** 2 - 4 * a *c
print(d)
if d < 0:
    print("Корней нет")
elif d == 0:
    x = -b / (2 * a)
    print(x)
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(x1)
    print(x2)
