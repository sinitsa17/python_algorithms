# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.

print('Введите длины трёх отрезков (целые числа, мм)')
l1 = int(input('1: '))
l2 = int(input('2: '))
l3 = int(input('3: '))
print("Треугольник из заданных отрезков - ")
if l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 <= l1:
    print("не существует")
elif l1 != l2 and l1 != l3 and l2 != l3:
    print("разносторонний")
elif l1 == l2 == l3:
    print("равносторонний")
else:
    print("равнобедренный")