n = int(input('Введите, сколько будет элементов в массиве: '))
a = []
count = 0
for i in range(n):
    a.append(int(input(f'{i + 1} эллемент: ')))
print(a)
x = int(input('Введите для проверки число: '))
for i in range(n):
    if x == a[i]:
        count += 1
print(f'Число {x} встречается {count} раз.')

'''
Задача 16:
Требуется вычислить,
сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. 
Последняя строка содержит число X

n = 5
1 2 3 4 5
x = 3

-> 1
'''