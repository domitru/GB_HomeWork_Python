base = {}
base = {'0':'', '1':'AEIOULNSTR,АВЕИНОРСТ', '2':'DG,ДКЛМПУ', '3':'BCMP,БГЁЬЯ', '4':'FHVWY,ЙЫ', '5':'K,ЖЗХЦЧ','6':'', '7':'', '8':'JX,ШЭЮ', '9':'', '10':'QZ,ФЩЪ'}

text = input('Введите слово: ')  # ADBFKJQАДБЙЖШФ
text = text.upper()
summa = 0
# print(text)
for i in range(len(text)):
    for j in range(len(base)):
        if text[i] in base[f'{j}']:
            # print(text[i])
            summa += int(j)
print()
print(f'Стоимость слова: {summa} баллов.')

'''
Задача 20:
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:

A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.

А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.

Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

Ввод:
ноутбук
Вывод:
12
'''