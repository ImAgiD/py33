'14.02.24============================Built in Function==========================='
# map, filter, reduce - функции высшего порядка, zip, enumerate
'------------------------------------'
'ZIP'
# zip - функция, которая соединяет несколько последовательностей(получаем генеартор, в котором элементы - tuple) (zip objekt)
# list1 = [1,2,3,4]
# list2 = ['a', 'b', 'c']
# list3 = [10.5, 20.0, 1.3, 0.5]

# zipped = zip(list1, list2, list3)
# print(zipped) #<zip objekt at 0x7fedh2ty[h2r>] -> list()
# print(list(zipped)) #[(1,'a', 10.5), (2, 'b', 20.0), (3, 'c', 1.3)] рулит максимальный лист :)
# print(tuple(zipped)) #((1,'a', 10.5), (2, 'b', 20.0), (3, 'c', 1.3))   #если оставить и лист и тюпл то тюпл выходит пустым. Потому что мы уже получили ответ в листе
# print(dict(zipped)) #только 2 листа можно засовывать здесь

'-------------------------------------'
'ENUMERATE'
# enumerate - функция, которая нумерует последовательность )по дефольу с 0, (тоже возвращает генератор)
# <enumerate objekt at 0x7dfjpq3r08h>

# enumerated = enumerate('hello world', -10)  # по умолчанию стоит 0, можно любое число написать
# print(enumerated) # -> <enumerate objekt at 0x7dfjpq3r08h>
# print(list(enumerated)) #[(0, 'h'), (1, 'e'), (2, 'l'), ...]
# # print(tuple(enumerated)) 
# for elem in list(enumerated):
#     print(elem)

# enumerated = enumerate([True , False, None, 1,2,3,4, -10], 100)  # по умолчанию стоит 0, можно любое число написать
# print(enumerated) # -> <enumerate objekt at 0x7dfjpq3r08h>
# print(list(enumerated)) #[(0, 'h'), (1, 'e'), (2, 'l'), ...]
# # print(tuple(enumerated)) 
# for elem in list(enumerated):
#     print(elem)

'-------------------------------------'
'MAP'
# функция высшего порядка только 1 аргумент , принимает 1ым аргументом функцию и 2ым аргументом последовательность 
# записывает в новую последовательность результат функции применив на каждый элемент последовательности
# <map objekt at 0x7dfjpq3r08h>

# list1 = ['1', '2', '3', '4']
# mapped = map(int, list1)
# print(mapped)   # <map object at 0x7dfjpq3r08h>
# print(list(mapped)) 

# mapped2 = map(str.isdigit, list1)
# print(list(mapped2))
#1 использовали def
# list_ = [12,234,3,45,56]
# def pow_(x):
#     return x**2

# print(list(map(pow_, list_))) 
# #2 использовали лямбду здесь: анонимная, одноразовая функция 
# print(list(map(lambda x: x**2, list_)))  
#1
# str_ = 'hello world'
# mapped = map(str.upper, str_)
# print(''.join(list(mapped)))  #-> HELLO WORLD
# #2
# print(''.join(list(map(str.upper, 'hello world')))) #-> HELLO WORLD

'-------------------------------------'
'FILTER'
# возвращает генератор с элементами, прошедшим фильтрацию (какое-то условие), принимает функцию и последовательность
# убирает лишнее, нужных оставляет, возвращает генератор
# <filter objekt at 0x7dfjpq3r08h>
# list_ = [12, 23, -234, 3, 123,-13]
# filtered = filter(lambda x:x >= 0, list_)
# print(filtered)
# print(list(filtered)) 

# users = [
#     {'name': 'makers', 'age': 20},
#     {'name': 'anonym', 'age': 15},
#     {'name': 'sem', 'age': 25}
# ]
# #оставить только 18+

# filtered = filter(lambda x:x['name'].startswith('a'), users)  #[{'name': 'anonym', 'age': 15}]
# print(list(filtered))  #x:x >= 18 #[{'name': 'makers', 'age': 20}, {'name': 'sem', 'age': 25}]

'-------------------------------------'
'REDUCE'
# принимает функцию и последовательность, но возвращает 1 элемент (передаваемая функция должна принимать 2 аргумента)
# импортируется из functools

from functools import reduce

list1 = [1,2,3,4,5,6]
res = reduce(lambda x, y: x*y, list1) 
print(res) 

# users = [
#     {'name': 'makers', 'age': 20},
#     {'name': 'anonym', 'age': 15},
#     {'name': 'sem', 'age': 25}
# ]
# #оставить только 18+ +reduce
# # filtered = filter(lambda x:x['name'].startswith('a'), users)  #[{'name': 'anonym', 'age': 15}]
# # print(list(filtered))
# def func(k, v):
#     if k['age'] < v['age']:
#         return k
#     else:
#         return v

# print(reduce(func, users))
# Task 3
# list1 = [1,-23, -213, 2,4,5,6,324,324,5]
# reduced = reduce(lambda x, y : x if x < y else y, list1)
# print(reduced) 
