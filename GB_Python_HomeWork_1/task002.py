'''Задача 2:
 Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
решение:'''

number = int(input('Введите трёхзначное число: '))
print()
if 99 < number < 1000:
    num1 = number // 100
    num2 = number // 10 % 10
    num3 = number % 10
    sumnum = num1+num2+num3
    print(f'Сумма цифр трехзначного числа =', sumnum)
    print()
else:
    print('Вы ввели не трёхзначное число!')
    print()