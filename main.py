# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# пример
# 5
# 1 2 3 4 5
# 3
# -> 1

# import random
#
# n = int(input('ведите колличество элементов: '))
#
# a = [random.randint(0,10) for i in range(n)]
# print(a)
#
#
# x = int(input('Введите число которое нужно отследить: '))
#
# count = 0
# for i in a:
#     if x == i:
#         count += 1
#
# print(f' -> {count}')




# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# пример
# 5
# 1 2 3 4 5
# 6
# -> 5


# import random
# n = int(input('ведите колличество элементов: '))
# a = [random.randint(0, 10) for i in range(n)]
# print(a)
# b=int(input('введите число: '))
# number=0
# for i in range(n):
#     if (b-a[i])<b-number and b-a[i]>0:
#         number=i
# print(f'Ближайший элемент к числу {b}: {a[number]}')




# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
#
# пример
#
# Ввод:
# ноутбук
# Вывод:
# 12


eng_letters = {1: 'AEIOULNSTR',
                   2: 'DG',
                   3: 'BCMP',
                   4: 'FHVWY',
                   5: 'K',
                   8: 'JX',
                   10: 'QZ'}
rus_letters = {1: 'АВЕИНОРСТ',
               2: 'ДКЛМПУ',
               3: 'БГЁЬЯ',
               4: 'ЙЫ',
               5: 'ЖЗХЦЧ',
               8: 'ШЭЮ',
               10: 'ФЩЪ'}

word = input('Ввод: ')
count = 0
for i in word:
    for k, v in eng_letters.items():
        if i in v:
            count +=k
for i in word:
    for k, v in rus_letters.items():
        if i in v:
            count +=k
print(f' -> {k}')
