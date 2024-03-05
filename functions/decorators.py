'13.02.24============================decorators==========================='
# функция высшего порядка, это функция которая принимает в аргументы другую функцию, создает внутри себя другую функцую и возвращает функцию

# def func1():
#     return 'hi'
    
# def func2(func_):
#     print(func_())
    
# func2(func1)
# print(func2) 

'13.02.24============================Decorators==========================='
# это - функции высшего порядка, которые нужны для расширения функционала другой функции не изменяя её (функция оберток)

# def decorator_glushitel(func):
#     def wrapper(*args, **kwargs):
#         text = func(*args, **kwargs)
#         res = 'тихо ' + text
#         print(res)
#     return wrapper

# def gun():
#     print('стрелять')

# wrapper = decorator_glushitel(gun)   
# wrapper()  #способ вызвать декоратор в ручную
'------------------------------------------------'
# def decorator_glushitel(func):
#     def wrapper(*args, **kwargs):
#         text = func(*args, **kwargs)
#         res = 'тихо ' + text
#         print(res)
#     return wrapper
# @decorator_glushitel
# def gun():
#     print('стрелять')

# gun()  #способ использовать декоратор при помощи синтаксического сахара

'------------------------------------------------'
# from datetime import datetime

# def decorator(func):
#     def wrapper():
#         print('start: ', datetime.now())
#         func()
#         print('finish: ', datetime.now())
#     return wrapper
# @decorator
# def hello():
#     print('hello world')
# hello()
# # wrapper = decorator(hello)
# # wrapper()

'------------------------------------------------'

# def func_start_time(func):
    # def wrapper(*args, **kwargs):
    #     print('start: ', datetime.now())
    #     func(*args, **kwargs)
        
    # return wrapper

# @func_start_time
# def sum_(a, b):
#     print(a+b)
    
# sum_(20, 10)
'------вложенные декораторы------------------------------------------'
    
# def decorator(num):
#     def inner_decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(num):
#                 func(*args, **kwargs)
#         return wrapper
#     return inner_decorator
# @decorator(10)
# def hello():
#     print('hello world')
    
# hello()
    
    

# def benchmark(func):
#     import time
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print('[*] Время выполнения: {} секунд.'.format(end-start))
#     return wrapper

# @benchmark
# def fetch_webpage():
#     import requests
#     webpage = requests.get('https://google.com')
# fetch_webpage()

# def makebold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped

# def makeitalic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped

# @makebold
# @makeitalic
# def hello():
#     return "hello world"

# print(hello())

# def my_decorator(arg1, arg2):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print(f"Аргументы декоратора: {arg1}, {arg2}")
#             result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator

# @my_decorator("Привет", 42)
# def example_function():
#     print("Функция выполнена")

# example_function()

# def a_decorator_passing_arguments(function_to_decorate):
#     def a_wrapper_accepting_arguments(arg1, arg2):
#         print(arg1, arg2)
#         function_to_decorate(arg1, arg2)
#     return a_wrapper_accepting_arguments

# @a_decorator_passing_arguments
# def print_full_name(first_name, last_name):
#     print("Меня зовут", first_name, last_name)

# a = ['1', '2', '3', '4']
# a = list(map(int, a))
# print(a) 
# dict10 = dict.fromkeys([1,2], 'asas')  # {1: 'lufjgvjhb', 2: 'lufjgvjhb' }
# print(dict10)

