# def prob():
#     string = 'hello world\n'
#     print(string* 3)

#     string = 'awehfr 80'
#     print(string.split(' '))

#     string = 'Agiii'
#     input('Hello')
#     print(f"Hello, {string}!")

#     string = 'Agii'
#     string = input()
#     print(f'Hello {string}!')

#     string1 = 'eoiyjiy'
#     string2 = 'wpkjnt'
#     print(f'{string1}+{string2}')



#     string1 = "America"
#     string2 = "Japan"
#     print(string1[:1] + string2[:1] + string1[int(len(string1)/2)] + string2[int(len(string2)/2)] + string1[-1] + string2[-1])

#     string1 = "America"
#     string2 = "Japan"
#     new_string = string1[0] + string2[0] + string1[len(string1) // 2] + string2[len(string2) // 2] + string1[-1] + string2[-1]
#     print(new_string)

#     # Даны две переменные string1 = "America" и string2 = "Japan".
#     # Выведите новую строку в который будут записаны первый, 
#     # средний и последний элемент двух переменных.
#     # Необходимо использовать срезы.


#     string = "      jker lntn  29 "
#     str1 = string.strip()
#     len1 = len(str1)
#     print (f'{str1}\n{len1}')
#     # Заданная строка с пробелами в начале и в конце
#     string = "    example string with spaces    "
#     # Удаление пробелов в начале и в конце строки
#     cleaned_string = string.strip()
#     # Вывод строки без пробелов
#     print(f"Очищенная строка: {cleaned_string}")
#     # Вывод длины строки без пробелов
#     length_without_spaces = len(cleaned_string)
#     print(f"Длина строки без пробелов: {length_without_spaces}")

#     string = "cow loves good milk"
#     string1 = string.replace("o", "e", 2)
#     print(string1)  

#     string = 'cow loves good milk'
#     print(string.replace('o','e', 2 ))

#     title = 'IPhone14'
#     price = 150
#     format_1 = 'Мой телефон', title, 'стоит', price, 'долларов'
#     print(format_1)
#     title = 'IPhone14'
#     # price = 150

#     string1 = 'Название: {} Цена: {}'
#     print(string1.format('IPhone', 150))

#     string = 'Название: %s Цена: %s' 
#     print(string% ('iphone', 150))

#     string = 'oho'
#     print(string.islower())

#     string = 'Danger'
#     letter = string[len(string)//2]
#     # print(letter) 
#     name = 'Python'
#     version = '3'
#     result = '{}-{}, {}.'.format(name[0], name, version)
#     print(result)



#     # • Работнику начисляли зарплату в d_salary = 2400 долларов period = 15 месяцев,
#     #  • распечатайте сколько заработал за этот период работник, в сомах, курс доллара к сому использовать 84 сома к 1 доллару,
#     # результат распечатайте в терминале

#     name=input()
#     last_name=input()
#     age=input()
#     city=input()
#     print(f'Вас зовут {name} {last_name}, Ваш возрост: {age}, Вы проживаете в городе {city}')


#     name = 'Nbvf'
#     last_name = "lzdfg"
#     age = 34
#     city = 'ow'

#     name = input()
#     last_name = input()
#     age = input()
#     city = input()
#     print(f'Вас зовут {name} {last_name}, Ваш возраст: {age}, Вы проживаете в городе {city}')

    # Task 24
    # Даны две переменные string1 = "America" и string2 = "Japan".
    # Выведите новую строку в который будут записаны первый, средний и последний элемент двух переменных.
    # Необходимо использовать срезы.
    # Вывод:
    # "AJrpan".

#     string1 = "America"
#     string2  = 'Japan'
#     middle_letter1 = len(string1) // 2
#     middle_letter2 = len(string2) // 2
#     res = string1[0] + string2[0] + string2[middle_letter1]
#     print(middle_letter1)


#     res = string1[0]+string2[0]
#     print(string)
# prob()

# def zadachi():
    # 1. Типы данных и форматирование:
    # Задача 1:
    # Создайте переменную name, в которой хранится ваше имя, и переменную age, в которой хранится ваш возраст.
    # Выведите сообщение в форме "Меня зовут Имя и мне Возраст лет" с использованием форматирования строк.

    # name = 'Agi'
    # age = 21
    # format = f'Меня зовут {name} и мне {age}'
    # print(format)

    # 2. Экранизация символов:
    # Задача 2:
    # Создайте переменную quote, в которой хранится следующая цитата:
    # arduino
    # Copy code
    # "Programming is like playing the piano. The more you practice, the better you become."
    # Выведите эту цитату, используя экранизацию символов для вставки кавычек внутри строки.
    # #1 метод
    # quote1 = """\"Programming is like playing the piano.
    # The more you practice, the better you become.\""""
    # print(quote1)
    # #2 метод
    # quote = "Programming is like playing the piano. The more you practice, the better you become."
    # # Вывод цитаты с использованием экранизации символов
    # print("\"{}\"".format(quote))

    # 3. Строки и Индексы:
    # Задача 3:
    # Создайте строку sentence:
    # "Python is a powerful programming language."
    # Выведите первые 5 символов, последние 5 символа и символ посередине строки sentence. Используйте индексы.
    # #1 метод
    # sentence = 'Python is a powerful programming language)'
    # print(sentence[:6]) 
    # print(sentence[-5:]) 
    # middle_index = len(sentence) // 2
    # middle_character = sentence[middle_index]
    # print(middle_character) 

    # #2 метод
    # sentence = 'Python is a powerful programming language)'
    # print("{}\n{}\n{}".format(sentence[-5:], sentence[:6], sentence[len(sentence) // 2]))


    # Задача 4:
    # Создайте строку word:
    # "PYTHON"
    # Выведите это слово в обратном порядке, используя индексы.

    # word = 'PYTHON'
    # print(word[::-1])

    # Подсказки:
    # Для форматирования строк используйте метод .format().
    # Экранизация символов осуществляется с использованием \.
    # Индексы в Python начинаются с 0.

    # В Python, для создания многострочных строк, в том числе и цитат, можно использовать тройные кавычки (''' или """). Например:

    # python
    # Copy code
    # quote = '''Programming is like playing the piano.
    # The more you practice, the better you become.''

# zadachi()

#def Logic():
#29.01.24 Lektion 4. Logic_operators / Tasks
# Задание 1 Дано число введенное пользователем в переменной number.
# Если число в переменной number больше 0 вывести True, иначе False.
# Для проверки кода введите число в поле во вкладке INPUT.
# Например, если в number ввели число:

# nuber1 = 2435
# if nuber1 > 0:
#     print("True")
# else:
#     print("False")

# #Задание 2 Проверить переменную string, куда попадает строка введенная пользователем.
# Если длина строки больше 5 символов вывести True, иначе False.
# Для проверки кода введите строку в поле во вкладке INPUT.

# str1 = "input()"
# if len(str1)>5:
#     print("True")
# else:
#     print("False")

#  #11 Задача   
# num = chr(int(input()))
# if num.isalpha():
#     print(f'Это буква "{num}"')
# else:
#     print(f'Это не буква, а символ "{num}"'\
    

# x=int(input())
# y=int(input())
# if x%y==0:
#     print('x делится на y')
#     print('частное: ',x//y)
# else:
#     print('x не делится на y')
#     print('частное: ',x//y)
#     print('остаток: ',x%y)


# numbers1 = list(range(0, 100, 25))
# print(numbers1) 
# # [10, 8, 6, 4] 

# my_list = ['ьечноств'] 
# # new_str = my_list[0] 
# new_str = my_list[0][-1] + my_list[0][1:-1] + my_list[0][0]  
# print(new_str) 

# name_of_list = ['Helloworld!']
# input_string = name_of_list[0]
# length = len(input_string)
# if length % 2 == 0:
#     first_half = input_string[:length // 2]
#     second_half = input_string[length // 2:]
# else:
#     first_half = input_string[:length // 2 + 1]
#     second_half = input_string[length // 2 + 1:]
# new_list = [char for char in second_half + first_half]
# print(input_string)

# list_ = ['world', 'hello']
# new_list = [list_[1], list_[0]]
# print(new_list)

# Methode dict.setdefault()
'''Определение:
Метод setdefault() словаря используется для получения значения по указанному ключу.
Если ключ отсутствует в словаре, то этот метод добавляет ключ с указанным значением в словарь.
Если ключ уже присутствует, метод возвращает текущее значение ключа.
'''
# Пример:
# my_dict = {'a': 1, 'b': 2}
# value = my_dict.setdefault('c', 3)
# print(my_dict)  # {'a': 1, 'b': 2, 'c': 3}
# print(value)    # 3
# existing_value = my_dict.setdefault('b', 5)
# print(my_dict)  # {'a': 1, 'b': 2, 'c': 3} (не изменено, так как ключ 'b' уже существует)
# print(existing_value)  # 2 (текущее значение ключа 'b')

# list.copy()
'''Определение: Метод copy() для списков используется для создания поверхностной копии списка.
Таким образом, изменения в оригинальном или копированном списке не затрагивают друг друга.'''
# # Пример:
# original_list = [1, 2, 3, 4]
# copied_list = original_list.copy()
# copied_list.append(5)
# print(original_list)  # [1, 2, 3, 4] (оригинальный список не изменился)
# print(copied_list)    # [1, 2, 3, 4, 5] (новый элемент добавлен в скопированный список)


# copy.deepcopy()
''''Определение:
deepcopy() из модуля copy используется для создания глубокой копии объекта, включая все вложенные объекты.
Это особенно полезно при работе с вложенными структурами данных, такими как списки внутри словарей.'''
# # Пример:
# import copy
# original_dict = {'a': [1, 2, 3], 'b': {'x': 10, 'y': 20}}
# deep_copied_dict = copy.deepcopy(original_dict)
# deep_copied_dict['a'][0] = 100
# print(original_dict)        # {'a': [1, 2, 3], 'b': {'x': 10, 'y': 20}} (оригинальный словарь не изменился)
# print(deep_copied_dict)     # {'a': [100, 2, 3], 'b': {'x': 10, 'y': 20}} (глубокая копия не влияет на оригинал)


# suitcase = []
# suitcase.append('футболка')
# suitcase.append('шорты')
# suitcase.append('сланцы')
# suitcase.append('очки')
# suitcase.append('кепка')
# suitcase.pop(0)
# suitcase.insert((1), 'панама')
# print(suitcase)


# list_ = input()
# new = list(list_)
# new.sort()
# # print(new)

# numbers = input("Введите числа через запятую: ")
# list_ = numbers.split(",")
# list_.sort(key=int)
# print(list_)


# list_ = sorted(input().split())
# print(list_)


# list1 = input().split('-')     #9,8,7,6,5,4,3,2,1
# list_ =[]
# for x in list1:
#     a = str(x)
#     list_.append(a)
#     list_.sort()
#     print(list_)


# a = 'djl fkvs ldf smk'
# print(a.split(' '))                  #['djl], 'fkvs, 'ldf', 'smk']

# list_ = [1,2,3,4,5]
# new_list = str(list_)
# print(new_list)

# list_ = [1,2,3,4,5]
# new_list = str(list_)
# print(new_list) 

# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for num in list_:
#     new_list.append(str(num))
# print(new_list) 

# list_ = [1,2,3,2,3,4,5]
# # str1 = 'четное'
# # str2 = 'нечетное'
# if list_ % 2 == 0:
#     print('четное')
# else:
#     print('нечетное')

# list_ = [1,2,3,2,3,4,5]
# # str1 = 'четное'
# # str2 = 'нечетное'
# new_list = []
# for a in list_:
#     if list_ % 2 == 0:
#     print(new_list('четное')
# else:
#     print('нечетное')


# list1 = [11, 23, 45, 7, 9] 
# list2 = [21, 4, 16, 8, 10] 
# list3 = list1 + list2 #[11, 23, 45, 7, 9, 21, 4, 16, 8, 10] 
# # summ = 0
# # for i in list3:
#     summ += i
#     print(summ)

# summ = sum(list3)
# print(summ)


# list_ = [20, 10, 20, 1, 100]
# list_.sort()
# print(list_)

# list_ = [20, 10, 20, 1, 100]
# list_.sort()
# print(list_[0])

# list_ = [20, 10, 20, 1, 100]
# f = 1
# for x in list_:
#     if x < f:
#         f = x
#     print(f)

# list_ = [20, 10, 20, 1, 100]
# min_number = list_[0]
# for i in range(1, len(list_)):
#     if list_[i] < min_number:
#         min_number = list_[i]
#         print(min_number)

# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# cleared_tuples = []
# for i in tuples:
#     if i = 0:
#         print(cleared_tuples)

# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# cleared_tuples = []
# for x in tuples:
#     if x != ():
#         cleared_tuples.append(x)
#         print(cleared_tuples)
# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# cleared_tuples = []
# for i in tuples:
#     if len(i)>0:
#         cleared_tuples.append(i)
#         print(cleared_tuples)

# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# cleared_tuples = [a for a in tuples if a]
# print(cleared_tuples) 
# list_ = []
# name1 = input("Введите имя и фамилию: ")
# name2 = input("Введите имя и фамилию: ")
# name3 = input("Введите имя и фамилию: ")
# name4 = input("Введите имя и фамилию: ")
# name5 = input("Введите имя и фамилию: ")
# list_.append(name1)
# list_.append(name2)
# list_.append(name3)
# list_.append(name4)
# list_.append(name5)
# target = " "
# surnames = []
# for x in list_:
#     t = x.find(target)
#     v = x.rfind(target)
#     if x.count(target) > 1:
#         surnames.append(x[v+1:])
#     else: surnames.append(x[t+1:])
#     print(sorted(surnames))
# 18 exercise loop
# # Запрос имен и фамилий у пользователей
# name1 = input("Введите ваше имя и фамилию: ")
# name2 = input("Введите ваше имя и фамилию: ")
# name3 = input("Введите ваше имя и фамилию: ")
# name4 = input("Введите ваше имя и фамилию: ")
# name5 = input("Введите ваше имя и фамилию: ")

# # Создание списка для фамилий
# last_names = []

# # Извлечение фамилий из введенных данных и добавление их в список
# for full_name in [name1, name2, name3, name4, name5]:
#     # Разбиваем полное имя на слова
#     words = full_name.split()
    
#     # Если есть хотя бы одно слово (фамилия считается вторым словом)
#     if len(words) >= 2:
#         last_names.append(words[-1])
#     else:
#         print(f"Предупреждение: Не удалось извлечь фамилию из введенного имени: {full_name}")

# # Сортировка и вывод списка фамилий
# last_names.sort()
# print("Отсортированный список фамилий:", last_names)

# 19
# list_ = [8, 6, 8, 10, 8, 20, 10, 1, 23, 34, 23, 23, 23, 232, 32, 38, 8]
# number = 23
# print(list_.count(number))

# print(type(isinstance))

# value = 42
# print(isinstance(value))
# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
# sum_ = 0
# res = [int(x) for x in list_
# if type(x) == int or x.isdigit()]
# for i in res:
#     sum_ += i
#     print(sum_)

# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
# count = 0
# for i in list_:
#     if type(i) == int or (type(i) == str and i.isdigit()):
#         count += int(i)
# print(count)

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

# # Начальные значения для самого длинного и самого короткого списка
# max_list = lists[0]
# min_list = lists[0]

# for lst in lists:
#     # Если текущий список длиннее, обновляем max_list
#     if len(lst) > len(max_list):
#         max_list = lst

#     # Если текущий список короче, обновляем min_list
#     if len(lst) < len(min_list):
#         min_list = lst

# print("Самый длинный список:", max_list)
# # print("Самый короткий список:", min_list)
# size1 = 3
# matrix2 = [[x for x in range(1, size1+1)]]
# print(matrix2 * size1)

# colors1 = ["red", "orange",  "blue", "green", "white"]
# colors2 = ["black", "yellow", "green", "blue"]
# c1c2 = [x for x in colors1 if not x in colors2]
# c2c1 = [x for x in colors2 if not x in colors1]
# print(c1c2, c2c1)

# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9]
# c1c2 = [x for x in list1 if x in list2]
# c2c1 = [x for x in list2 if x in list1]
# print(True)
# print(False)

# list_ = [4, 6, 4, 3, 3, 3, 3, 8, 4, 3, 4, 6, 3, 3, 8, 8]
# repeats = 6
# res = []
# for i in list_:
#     if list_.count(i) >= repeats and i not in res:
#         res.append(i)
# print(res)

# K = 3
# list_ = [[45 for x in range(K)] for y in range(K)]
# print(list_)

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# step = 2
# element = 'A'

# for i in range(2, 8, 3):
#     list_.insert(i, 'A')

# print(list_) 

# new_list = [i for i in range(1,26) if i % 2 == 0]
# print(new_list)  

# print(range(1,11))

# som = int(input())
# if som > 0:
#     print(som)
# else:
#     print('Сумма не может быть отрицательной!')

# biron = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81, 10:100}
# print(biron)

# dict_ = {12, 34, 43, 21, 0}
# # sorted_dict = {}
# print(dict_.sort()) 

# dict_ = (12, 34, 43, 21, 0)
# sorted_dict = {}
# print(dict_.sort()) 

# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [i for i in list_ if i < 0]
# # print(int_list) 
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {}
# print(dict_.sort)
# elder = {'Мурат': 24, 'Эржан': 21,'Мурат': 24,'Карина': 24, 'Алтынай': 17, 'Айбек': 16}
# for val in elder:
#     if val < 17:
# #         print(val) 
# # print({'a': 32, 'b': 36, 'c': 37, 'd': 21})
# a = {'a': 1, 'b': 2, 'c': 1}
# for v in a.values:
#     print(v) 
    
# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for k, v in list(a.items()):
#     if v == None:
#         a.pop(k)
#     print(a)
    
# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# for k, v in list(a.items()):
#     print(k, v/5) 

# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# # b = {}
# for k, v in list(a.items()):
#     if v % 2 == 0:
#         a.pop(k)
#     else:
#         print(a)

# a = {'apple': 2, 'orange': 5, 'banana': 10}
# a = {k: v for (k,v) in a.items()
#      if v % 2 !=0 }
# print(a)

# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# dict2 = {}
# for key, val in dict_.items():
#     if val == None:
#         dict2.get(key)
#         print(dict2)
        
# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# dict_ = {k:v for k,v in dict_.items() if not v}
# print(dict_) 
# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# dict_2 = {}
# for k,v in dict_.items():
#     if v == None:
#         dict_2.setdefault(k,v)
#         dict_.clear
#         dict_ = dict_2
#         print(dict_) #(Заметка: моё решение принимает платформа, но оно идиотское))
        


# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for k, v in list(dict_.items()):
#     if v != None:
#         dict_.pop(k)
# print(dict_)

# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'} 
# dict2 = {}
# for key, val in dict1:
#         dict2(key**2, val)  
# print(dict2) 

# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'} 
# dict2 = {}
# for key, value in dict1.items():
#     dict2[key**2] = value 
# print(dict2)


# print(dir(dict))

# srt1v= 'aksdbh        wegn      '
# print(srt1v.strip())

# s = 0
# for i  in range(10, 100):
#     s = s*i
# print(s)

# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# dict_ = {}
# for i in list_:
#     key = i
#     dict_[key] = len(key)
# print(dict_)

# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}
# max_ = max(dict_.values())
# for k in dict_.keys():
#     if dict_[k] == max_:
#         print(k)

# dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# dict2 = {}
# for key, value in dict1.items():
#     dict2[key] = key **3
# print(dict2)



# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# for k,v in list(dict_.items()):
#     for v2 in v.values():
#         dict_[k] = v2
#     print(dict_)

# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}
# for key, val1 in dict1.items():
#     for key in dict1.items():
#         for val2 in dict1.values():
#             dict2[key] = val1 * val2
#     print(dict2)
    

# 28 
# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}
# for key, val in dict1.items():
#     res = 1
#     for j in val.values():
#         res = res * j
#         dict2[key] = res
#         print(dict2)

# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# dict_ = {} 
# for i in list_():
#     for key, val in list_():
#         if i.isalpha():
#             dict_.append(key)
#         if i.isdigit():
#             dict_.append(val)
#     # key = str(list_)
#     # val = int(list_)
#     dict_[key] = val
#     print(dict_) 
    
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_values = sorted(dict_.values())
# sorted_dict = {}
# for i in sorted_values:
#     for k in dict_.keys():
#         if dict_[k] == i:
#             sorted_dict[k] = dict_[k]
#             break
#         print(sorted_dict)
        
        
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = sorted(dict_)
# newd = sorted_dict.reverse()
# print(newd)

# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key1 = input()
# for key, value in dict_.items():
#     if key1 == key:
#         print("Key is present in the dictionary")
#     else:
#         print("Key is not present in the dictionary")
        

# dict1 = {1:10, 2:20}
# dict2 = {3:30, 4:40}
# dict3 = {5:50, 6:60}
# dict4_1 = dict1 + dict2
# dict4 = dict4_1 + dict3
# print(dict4)

# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# dict_ = {}
# for key in list1:
#     dict_[key]
#     for val in list2:
#         dict_ = val
#         dict_[key] = val
#     print(dict_)
 
# dict_ = {
#     'math': {
#         'sum': sum
#     },
#     'vars': {
#         'a': 5,
#         'b': 20,
#         'c': 50
#     }
# }

# # Получаем значения переменных из словаря 'vars'
# values1 = dict_['vars'].values()

# # Вычисляем сумму значений
# result = sum(values1)

# Выводим результат
# print(result)

# dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 
# dict2 = {}
# for key, val in dict1.items():
#     if val % 2 != 0:
#         val = 1
#         dict2[key] = val
#     else:
#         dict2[key] = val
#     # print(dict2)
# print(dict2)

# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {}
# for key, val in list(dict_.items()):
#     sd_val = sorted(val)
#     sorted_dict[key] = sd_val
#     sorted_dict.reverse(sd_val)

# print(sorted_dict)



# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {}

# sorted_keys = sorted(dict_, key=dict_.get, reverse=True)
# print(sorted_keys)

# for key in sorted_keys:
#     sorted_dict[key] = dict_[key]
    
# print(sorted_dict)



# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}
# for key, val in dict1.items():
#     # print(key, 'this is key')
#     # print(val, 'this is value')
#     res = 1
#     for j in val.values():
#         print(j, '11111')
#         res = res * j
#         print(res, 'this is res')
#         dict2[key] = res
#         print(dict2)
        
# a = {'a': 10, 'b': 9, 'c': 3}
# res = 1
# for i in a.values():
#     a = res*i
# print(res)

#16 set
# a = [set(), set(), set()]
# inp1 = input()
# inp2 = int(input())
# d = 'default value'

# for i in a:
#     if a.index(i) == inp2 - 1:
#         i.add(inp1)
#     else:
#         i.add(d)
# print(a)

# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [i for i in list_ if i % 2 == 0 and i > 0]
# print(int_list) 

# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# str_ = [x for x in list_ if isinstance(x, str)]
# int_ = [x for x in list_ if isinstance(x, int)]
# dict_ = dict(zip(str_, int_))
# print(dict_)

#7 comprehension
# list_= [x == True if x % 2 == 0 else  x == False for x in range(1, 11)]
# print(list_) 

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = [i == 'shorter' if len(i) <= 4 else i == 'longer' for i in list_name] 
# print(new_list) 

# dict_ = {i:i**2 for i in range(1,10)}
# print(dict_)

# n = int(input())
# dict_ = {i:n**2 for i in range(1,501) if i % n == 0}
# print(dict_)

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {}

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [i for i in string_.split() if i.isdigit()]
# print(list_) 

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# newd = {k: v1 == (max(v2) for v2 in dict_.values) for k, v1 in dict_()} 
# print(newd) 

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {k:i for k, v in my_dict.items() for i in v.values()} 
# print(dict_)

# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [i == 1 if i < 0 else i for i in list_]
# print(int_list)

# list1 = [1, 2, 'hello', 3, 'world', 4, 5, 'book', 'code', 6, 'Makers', 7, 8, 9, 10]
# list2 = [i for i in list1 if i.isalpha]
# print(list2)

# list_ = [0, 3, 9, 7, 5, 2, 18, 4]
# list1 = [i for i in list_ if i > 5]
# print(list1)

# list_ = [False, True, False, True, False, True, False, True, False, True] 
# list2 = [1 if i == True  else 0  for i in list_]
# print(list2) 

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = [len(i) for i in list_name]
# print(new_list)

# string = "happy birthday!"
# list_ = [i for i in string if i != ' ' and i != '!']
# print(list_)

# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# neww = [i for v in dict_.values() for i in v.values()]
# print(neww) 



# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# # neww = [key: val for key,val in dict_.items() if 200< val <5000]
# list1 = [k.upper() for k,v in dict_.items() if 200 < v < 5000]
# print(list1)

# print(neww) 

# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

# dict2 = {key.replace('i', ''): key.count('i') for key in dict1}

# print(dict2)

# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]
# readers = [i for i in SPL_Patrons if i > 100]
# print(readers)

# prairie_pirates = [
# ['Tractor Jack', 1000, True],
# ['Plowshare Pete', 950, False],
# ['Prairie Lily', 245, True],
# ['Red River Rosie', 350, True],
# ['Mad Athabasca McArthur', 842, False],
# ['Assiniboine Sally', 620, True],
# ['Thresher Tom', 150, True],
# ['Cranky Canola Carl', 499, False]
# ]

# neww = [i[0] and i[1]*42 for i in prairie_pirates]
# print(neww) 

# list_ = list(range(0,11))
# resultet = [i/2 for i in list_ if i % 2 == 0]
# print(resultet)

# set1 = {x for x in range(20)}
# print(set1)
# set2 = {a for a in range(8,18)}
# print(set2)
# full_set = set1.union(set2)
# if len(full_set) < 20:
#     print(f'В этом сете было {20-len(full_set)} повторения, его длина составляет {len(full_set)}')
# elif len(full_set) == 20:
#     print("Ваш объединенный сет полностью уникальный!")
    
    
# def my_decorator(func):
#     def wrapper():
#         print("Дополнительная логика перед выполнением функции")
#         func()
#         print("Дополнительная логика после выполнения функции")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Привет!")

# # Теперь вызов say_hello() будет включать в себя дополнительную логику из декоратора
# say_hello()

# import time

# Декоратор
# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"Время выполнения функции {func.__name__}: {execution_time} секунд")
#         return result
#     return wrapper

# # Использование декоратора
# @timing_decorator
# def example_function():
#     print("Функция выполняется...")
#     time.sleep(2)
#     print("Функция завершена.")

# # Вызываем функцию
# example_function()

# dict_ = {'key1': 'value1', 'key2': 'value2'} 
# try:
#     print(v for v in dict_.values())
# except Exception:
#     print('Нет такого ключа!')
# from datetime import datetime
# def func_start_time(func):
#     def wrapper():
#         print('start: ', datetime.now())
#         func()
#         print('Функция запущена ', func, )
#     return wrapper

# @func_start_time
# def func():
#     print('Hello world')
# func()  


# def make_bold(func):
    
#     def wrapper(*args, **kwargs):
#         return f'<b>{func()}</b>'
#     return wrapper

# def make_italic(func):
    
#     def wrapper2(*args, **kwargs):
#         return f'<i>{func()}</i>'
#     return wrapper2

# def make_underline(func):
    
#     def wrapper3(*args, **kwargs):
#         return f'<u>{func()}</u>'
#     return wrapper3

# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'
 
# hello() 

# users = {'Tim':'1234', 'Alex':'qwert', 'Sadyr':'654' }

# def validate_password(func):
#     def wrapper(username, password):
#         if username in users:
#             if users[username] == password:
#                 func(username, password)
#             else:
#                 print('Password is invalid')
#         else:
#             print('Username is not defined')
#     return wrapper

# @validate_password
# def login(username, password):
#     print(f'Welcome, {username}')

# # Пример использования
# login('user1', 'password1')  # Выведет: Welcome, user1
# login('user2', 'wrongpass')  # Выведет: Password is invalid
# login('nonexistentuser', 'password')  # Выведет: Username is not defined

# try:
#     age = int(input())
#     if age < 18:
#         raise ValueError('Доступ запрещён')
# except:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')

# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ]
# def func15(users):
#     result = ''
#     for user in users:
#         if user['work'].startswith('IT'):
#             result += f"{user['name']}, скидки в магазине компьютерной техники!\n"
#     return result

# print(func15(users))

# inp1 = input('Введите слова и числа через пробел')
# a = inp1.split()
# list_ = []
# for i in a:
#     try:
#         i.isdigit()
#         list_.append(int(i))
#     except ValueError:
#         raise Exception('Данный элемент не является числом! ')
        
# dict_ = {1:'asd', 12:'12'}
# dict_ = {k:len(v) if k % 2 == 0 else len(v) ** 3 for k, v in dict_.items()}
# print(dict_)

# var = 'переменная в foo'
# def foo():
#     global var
#     var = 'переменная foo'
#     print('переменная в foo: ', var)
# def bar():
#     global var
#     var = 'переменная bar'
# bar()
# foo()
# print('переменная в foo: ', var)

# def get_string_length(x):
#     return len(x)

# print(get_string_length('hello')) 

# def func(list_):
#     xxx = []
#     for x in list_:
#         xxx.append(int(x[2][:-2]))
#     print(xxx)
    
# students = [('Tinur', '181 cm', '71kg'),
#             ('Ai', '180 cm', '70kg')]

# func(students)
        
import functools
list_ = [1, 2, 3, 4]  
result = functools.reduce(sum(list_))
print(result)