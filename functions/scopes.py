'12.02.24=======================Области видимости======================='
#LEGB - local enclosed global built-in

'=======================Built-in======================='
# Встроенное пространство имен таких как (list, print, dict, len, input)

'=======================Global======================='
#Все переменные, которые мы создали внутри файла
#Чтобы посмотреть все глобальные переменные, можно использовать функцию globals
# a = 10 
# b = 'hello'
# print(globals())

'=======================enclosed======================='
# - замкнутое пространство имен - локальное пространство, у которого есть внутреннее локальное пространство/ вложенное пространство
# var = 'global'  #хранитися в глобальном пространстве

# def func():
#     var = 'enclosed'  #замкнутое пространство
    
#     def inner_func():
#         var = 'local' #локальное пространство
#         print(var)  #local
#     print(var) #enclosed
#     inner_func()
# print(var)
# func()   #global -> enclosed -> local

'=======================local======================='
# локальное пространство имён - это пространство, которое находится внутри функции
# мы не можем менять переменную глобального пр в локалбном пр-е  
# операторы - global / nonlocal
# a = 10
# def func(a, b):
#     res = a+b
#     print(res)
#     print(locals())
#     print(globals())
# func(10, 5)  #15

# def count_(num):
#     count = 0
#     def inner_count_():
#         nonlocal count   
#         count += 1
#         print(count)
#     for i in range(num):
#         inner_count_()
# count_(3) 

# def func():
#     print('hello world')
#     return func
# func()()()()



