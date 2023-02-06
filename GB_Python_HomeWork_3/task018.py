list_1 = [0, 1, 2, 7, 9, 4, 4, 6, 3, 2] 
print(list_1)
x = int(input("Задайте число: "))

list_1.append(x)
ints_list = list(set(sorted(list_1)))
i = (ints_list.index(x))
ir,il = i + 1, i - 1
if i == 0:
    print(f'Ближайшее по величине число: {ints_list[ir]}')
elif i+1 == len(ints_list):
    print(f'Ближайшее по величине число: {ints_list[il]}')    
else:
    a = ints_list[i] - ints_list[il]
    b = ints_list[ir] - ints_list[i]
    if a < b:
        print(f'Ближайшее по величине число: {ints_list[il]}')
    elif b < a:
        print(f'Ближайшее по величине число: {ints_list[ir]}')
    else:
        print(f'Ближайшие по величине числа: {ints_list[il]} и {ints_list[ir]}')    

'''
Задача 18:
Требуется найти в массиве A[1..N] 
самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное
число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. 
Последняя строка содержит число X

n = 5
1 2 3 4 5
x = 6
-> 5
'''