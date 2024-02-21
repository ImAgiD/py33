"================ Dictionary ================"
# Dictionary {} - изменяемый, неиндексируемый, неупорядоченный, итерируемый ТД, предназначенный для хранения "любых" данных в парах(ключ:значение)

# user = {'name':'Sultan', 'age':20, 'nick':'katana'}
# print(user['age']) #20
# print(user['nick']) #katana
# print(user['name']) #Sultan

# {ключ:значениеб, ключ:значениеб ...}
# ключ - неизменяемый ТД, уникальный (Если ключ повторяется, сохраняется тот, который явдяется последним )
# значение - любые: и изменяемый, и неизменяемый ТД. Могут повторяться

"================ Создание ================"
# 
# dict1 = {'a':1, 'b':2}
# dict2 = dict([('a',1),('b', 2)])
# dict3 = dict(['a1', 'b2'])
# print(dict3)

# dict4 = {}
# dict4['name'] = 'Tima'
# dict4['age'] = 100
# dict4['nick'] = 'collection'
# print(dict4)

"================ Методы словарей ================"
# get - метод для получения, который возвращает значение по ключу, если такого ключа нет, то возвращает дефолтное значение, чаще всего None
# user = {
#     'name': "Nick",
#     'age': 100,
#     'telephon_number': '+123456789'
# }
# # print(user['asfas']) #KeyError
# print(user['name']) #Nick
# print(user.get('name', True)) #Nick
# print(user.get('age', 'нет такого ключа')) #100
# print(user.get('id')) #None

# pop - удаляет пару по ключу и возвращает значение
# dict5 = {'a':1, 'b':2, "c":3}
# popped_values = dict5.pop('a')
# print(popped_values) #1
# print(dict5) # {b':2, "c":3}}

# popitem - ничего не принимает, удаляет последнюю пару и возвращает значение

# dict6 = {'a':1, 'b':2, "c":3}
# popped_values = dict6.popitem()
# print(popped_values) # ("c", 3)

# print(dir(dict()))

# update - расширяет словарь парами из второго словаря

# dict7 = {1 :'a', 2 :'b'}
# dict8 = {2:"c", 4:'d'}
# dict7.update(dict8)
# print(dict7) # {1 :'a', 2 :'b', 4:'d'}

# clear - очищает словарь
# dict9 = {1:1, 2:2, 3:3}
# dict9.clear()
# print(dict9) # {}

# fromkeys - метод для создание нового словаря, используя список ключей

# dict10 = dict.fromkeys([1,2], 'asas')  # {1: 'lufjgvjhb', 2: 'lufjgvjhb' }
# print(dict10)

# dict11 = dict.fromkeys('abcd', 0)
# print(dict11) #{'a' : 0,  'b' : 0,  'c' : 0,  'd' : 0}

# dict.setdefault()
# list.copy
# list.deepcopy()

# items - метод, который достает [(ключ, значение), (ключ, значение)]
# keys - метод, который возвращет ключи 
# values - метод, который возвращет значение

# user = {'name': 'Nick', 'age': 100, 'telephone_number': '+123456789'}
# keys_list = user.keys()
# print(keys_list)
# # Вывод: dict_keys(['name', 'age', 'telephone_number'])

# user = {'name': 'Nick', 'age': 100, 'telephone_number': '+123456789'}
# values_list = user.values()
# print(values_list)
# # Вывод: dict_values(['Nick', 100, '+123456789'])


# dict12 = {'a':1, 'b':2, "c":3 }
# print(dict12.values())
# print(dict12.keys())
# print(dict12.items())

"================ Циклы с dictionary ================"
# dict13 = {'a':1, 'b':2, "c":3, 'a':1, 'b':2, "c":3 , 'a':1, 'b':2, "c":3 }
# print(dict13['a'])
# print(dict13['b'])
# print(dict13['c']) #... OR

# for i in dict13: # + ".keys"
#     print(i)  

# for i in dict13.values:
#     print(i)

# for i in dict13.items:
#     print(i)

# dict13 = {'a': 1, 'b': 2, "c": 3, 'a': 1, 'b': 2, "c": 3, 'a': 1, 'b': 2, "c": 3}
# # Вывод через индексацию
# print(dict13['a'])  # Выведет: 1
# print(dict13['b'])  # Выведет: 2
# print(dict13['c'])  # Выведет: 3
# # Вывод через цикл по ключам
# for key in dict13:  # Итерация по ключам
#     print(key)  # Выведет все уникальные ключи 'a', 'b', 'c'
# # Вывод через цикл по значениям
# for value in dict13.values():  # Итерация по значениям
#     print(value)  # Выведет все значения, включая повторяющиеся 1, 2, 3
# # Вывод через цикл по парам ключ-значение
# for key, value in dict13.items():  # Итерация по парам ключ-значение
#     print(key, value)  # Выведет все уникальные ключи и соответствующие значения


# dict4 = {}
# dict4['name'] = 'Tima'
# dict4['age'] = 100
# dict4['nick'] = 'collection'
# print(dict4)
# items / for /

# dict13 = {'a':1, 'b':2, "c":3}
# dict0 = {}
# for k, v in dict13.items():
#     dict0 = [v] = k 
# print(dict13) 


# list_ = []
# list_.append(True)
# list_.append('text')
# list_.append(123)
# list_.append([123]) 
# print(list_)




# dict13 = {'a':1, 'b':2, "c":3, 'a':1, 'b':2, "c":3 , 'a':1, 'b':2, "c":3 }
# print(dict13['a'])
# print(dict13['b'])
# print(dict13['c']) #... OR

# for i in dict13: # + ".keys"
#     print(i)  

string = "pythonist"
dict_ = {x:string.count(x) for x in string} 
print(dict_)



