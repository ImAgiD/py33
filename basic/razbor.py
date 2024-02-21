# #• Работнику начисляли зарплату в d_salary = 2400 долларов period = 15 месяцев,
# #  • распечатайте сколько заработал за этот период работник, в сомах, курс доллара к сому использовать 84 сома к 1 доллару,
# # результат распечатайте в терминале

# # d_salary = 2400
# # period = 15
# # kurs = 84
# # print(d_salary * period * kurs)

'--------------------------------------'

# # Задание 11
# # Создайте переменную string со значением в виде любой строки.
# # Обменяйте местами первый и последний символы и выведите результат в консоль.(ваш код должен работать со строками любой длины)
# # К примеру, если в string хранится строка:

# # Hello
# # результат в терминале будет:

# # oellH 
# # используйте срезы(индексацию строк) и конкатенацию(склеивание строк)

# # string = 'world'
# # print(string[-1]+string[1:-1]+string[0])


'--------------------------------------'


# # Nurmuhammed., [26/1/24 14:34]
# # Задание 13

# #     В переменные leg_a, leg_b запишите два числа, которые будут обозначать два катета прямоугольного треугольника .
# #     Рассчитайте длину гипотенузы треугольника hypotenuse, воспользовавшись теоремой Пифагора.

# #     Note: Теорема Пифагора: a  **2 + b  2 = c  2.

# #     Распечатайте результат

# leg_a = 10
# leg_b = 5
# # c^2 = b^2 + a^2
# from math import sqrt 
# hypotenuse = sqrt((leg_a ** 2) + (leg_b ** 2))
# print(hypotenuse)

'----------------------------------------'

# Task 22
# Объявите переменную string значением которой будет input().
# Выведите ее значение используя интерполяцию строк ("Hello" и значение переменной string)
# К примеру, если в переменной string хранится строка: "Makers"

# string = input()
# print(f'Hello {string}')

'------------------------------------'

# Объявите переменную string со значением в виде любой строки.

# Необходимо проверить начинается ли ваша строка с подстроки "Python" (Регистр должен учитываться). Вывод: True/False

# Например:

# string = 'python is the best'
# # False
# string = 'Python is the best'
# # True
# string = 'I love Python'
# # False

# string = 'i love Python'
# print(string.startswith('Python')) # False

'-----------------------------------'

# Объявите переменную string со значением в виде любой строки.
# Размножьте строку три раза, при этом каждое повторение должно быть на новой строке, необходимо использовать экранирование.
# Необходимо использовать функцию print() один раз.
# К примеру, если в string хранится строка: 'hello world'

# string = 'hello world'
# print((string + '\n') * 3) 

'-----------------------------------------'

# Task 26
# Дана переменная string, с текстом "cow loves good milk".

# Замените в ней только первые две буквы o на e

# Вывод:

# "cew leves good milk"

# string = "cow loves good milk"
# print(string.replace('o', 'e', 2))

'----------------------------------------'

# Задание 13
# Создайте переменные name(имя), last_name(фамилия), age (возраст) и city(город), значения которых вы будете получать от пользователей из функции input().

# Во вкладке INPUT введите значения для переменных name(имя), last_name(фамилия), age (возраст) и city(город).

# С помощью f-строк выведите краткую информацию о человеке.

# Например, если в перемнную name ввели значение 'Иван', в last_name - 'Пупкин', в age - 35, а в city - 'Москва',
# то в терминале получим строку: Вас зовут Иван Пупкин, Ваш возраст: 35, Вы проживаете в городе Москва

# name = input()
# last_name = input()
# age = input() 
# city = input()

# print(f'Вас зовут {name} {last_name}, Ваш возраст: {age}, Вы проживаете в городе {city}')

'--------------------------------------'

# Task 24
# Даны две переменные string1 = "America" и string2 = "Japan".
# Выведите новую строку в который будут записаны первый, средний и последний элемент двух переменных.
# Необходимо использовать срезы.
# Вывод:
# "AJrpan".

# string1 = 'Kyrgyzstan'
# string2 = 'Kazahstan'
# middle_l_A =  len(string1) // 2
# middle_l_J = len(string2) // 2
# res = string1[0] + string2[0] + string1[middle_l_A] + string2[middle_l_J] + string1[-1] + string2[-1]
# print(res)

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите первое число: "))
# oper = input("Введите оператор: ")
# if oper == '+':
#     print(num1+num2)
# elif oper == '-':
#     print(num1-num2)
# elif oper == '*':
#     print(num1*num2)
# elif oper == '/':
#     if (num2 == 0):
#         print("Ошибка")
#     else:
#         print(num1/num2)
# elif oper == '**':
#     print(num1**num2)

# # 12
# n=int(input())
# print('На лугу пасется ',end='' )
# if (n > 100):
#     print("Incorrect number")
# elif ((n > 10 and n < 20) or (n % 10 >= 5) or (n % 10 == 0)):
#     print(n, "коров")
# elif (n % 10 == 1):
#     print(n, "корова")
# elif (n % 10 in [2,3,4]):
#     print(n, "коровы")
    
# #13 count = 0
# number = input("Введите строку с числом: ")
# if number.isdigit():
#     count = int(number)
# print(count)
    
# # 24
# step_1 = input("Номер столбца 1-й клетки: ")
# step_2 = input("Номер строки 1-й клетки: ")
# step_3 = input("Номер столбца 2-й клетки: ")
# step_4 = input("Номер строки 2-й клетки: ")

# if (step_1 == step_3) or (step_2 == step_4):
#   print ("YES")
# else:
#   print ("NO")
  
# #25 x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if abs(x1 - x2) == abs(y1 - y2):
#     print('YES')
# else:
#     print('NO')

# #21
# Даны три стороны треугольника a, b, c (inputs). Определите тип треугольника с заданными сторонами.
# Выведите одно из четырех слов: rectangular для прямоугольного треугольника, acute для остроугольного треугольника,
# obtuse для тупоугольного треугольника или impossible, если треугольника с такими сторонами не существует

# a,b,c=int(input()), int(input()), int(input())   #it works!
# a1=min(a,b,c)
# b1=max(a,b,c)
# c1=sum([a,b,c])-a1-b1
# if b1>=a1+c1:
#     print('impossible')
# elif b1**2==a1**2+c1**2:
#     print('rectangular')
# elif b1**2<a1**2+c1**2:
#     print('acute')
# elif b1**2>a1**2+c1**2:
#     print('obtuse')    #bis hier
    
# a = int(input())
# b = int(input())
# c = int(input())
# if (a + b > c) and (c + b > a) and (a + c > b):
#     if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (c*c + b*b == a*a):
#         print("rectangular")
#     elif (a*a + b*b > c*c) or (a*a + c*c > b*b) or (c*c + b*b > a*a):
#         print("acute")
#     elif (a*a + b*b < c*c) or (a*a + c*c < b*b) or (c*c + b*b < a*a):
#         print("obtuse")
# else:
#     print("impossible")

# a = int(input())
# b = int(input())
# c = int(input())
# a1 = min(a, b, c)
# b1 = max(a, b, c)
# c1 = sum([a, b, c]) - a1 - b1
# print(c1)

# list_ = [123, 43, 34, 43, 1, 2]
# list_.sort()   # сортирует и меняет list_
# print(list_)    

# a = sorted(list_)
# print(a) #сортирует, но не меняет list_
# number = input('Введите число через запятую: ')
# list_ = number.split(",")
# tuple_ = tuple(list_.split(','))
# print(list_)
# print(tuple_)

# list1 = 
'''Типы данных. Списки. Цикл for. Таск 35
Задание 35
Вам дан список из букв, пользователь вводит 2 буквы, от какой и до какой буквы нужно соединить в одну строку, ваш код должен соединить эти буквы
Например:

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
merge_from = 'a'
merge_to = 'd'
Результат:

['abcd', 'e', 'f', 'g']'''
# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# merge_from = input()
# merge_to = input()
# from_to = "".join(chars[chars.index(merge_from):chars.index(merge_to)+1])
# result = []

# for char in chars[:chars.index(merge_from)]:
#     result.append(char)

# result.append(from_to)

# for char in chars[chars.index(merge_to)+1:]:
#     result.append(char)

# print(result)
# 14

# a = {'a': 3, 'b': 9}
# res = a.get('a') + a.get('b')
# print(res)

# a1 = {'a': 1, 'b': 2}
# a2 = dict([('a', 1), ('b', 2)])
# a3 = dict(['a1', 'b2'])
# print(a1)
# print(a2)
# print(a3)

# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# for k, v in dict_.items():
#     print(max(k)) 


# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# print(max(dict_.values()))

# dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 
# dict2 = {}
# for k, v in dict1.items():
#     if v % 2 != 0:
#         dict2[k] = 1
#     else:
#         dict2[k] = v
# print(dict2)


dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
dict2 = {}
for k, v in dict_.items:
    if v == None:
        print(dict2)

        