# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите три разных целых числа')
num1 = int(input('Первое: '))
num2 = int(input('Второе: '))
num3 = int(input('Третье: '))
if num2 < num1 < num3 or num3 < num1 < num2:
    mid = num1
elif num1 < num2 < num3 or num3 < num2 < num1:
    mid = num2
else:
    mid = num3
print(f'Среднее из введённых чисел: {mid}')