'''
Задача 6:
 Вы пользуетесь общественным транспортом?
 Вероятно, вы расплачивались за проезд и получали билет с номером.
 Счастливым билетом называют такой билет с шестизначным номером,
 где сумма первых трех цифр равна сумме последних трех.
 Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
 Вам требуется написать программу, которая проверяет счастливость билета.
385916 -> yes
123456 -> no
решение:
'''
print()
number = int(input('Введите шестизначный номер билета: '))
print()
if 99999 < number < 1000000:
    leftnum = number // 1000
    leftnum1 = leftnum // 100
    leftnum2 = leftnum // 10 % 10
    leftnum3 = leftnum % 10
    sumleftnum = leftnum1 + leftnum2 + leftnum3

    rightnum = number % 1000
    rigthnum1 = rightnum // 100
    rigthnum2 = rightnum // 10 % 10
    rigthnum3 = rightnum % 10
    sumrightnum = rigthnum1 + rigthnum2 + rigthnum3

    if sumleftnum == sumrightnum:
        print('Ваш билет счастливый. Поздравляем!')
    else:
        print("Нет,Вам не повезло.Билет не счастливый.")
else:
    print('Nein. Sie haben keine sechsstellige zahl eingegeben. ;-)')
print()