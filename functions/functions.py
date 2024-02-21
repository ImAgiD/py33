'07.02.24============================Function==========================='
# function() - это именованный блок кода, который может принимать аргументы и возвращать результат

# def get_sum(x, y):   # x, y - параметры
#     result = x+y
#     return result

# print(get_sum(3, 4))  # 3, 4 - аргументы 


# def sqrt_(num):
#     return pow(num, 0.5)   # num ** 0.5
# print(sqrt_(36))

'Функции собладают принцип DRY (don/t repeat yourself)'

'============================Аргументы и параметры==========================='
# параметры - переменные внутри функции, задаются при создании функции
# аргументы - значения, которые мы передаем при вызове функции

'=======================Виды параметров======================='
# 1. обязательные - всегда должны быть
# 2. необязательные делятся на:
        # 1. с дефолтном значением(со значением по умолчанию)
        # 2. args (все позиционные аргументы)
        # 3. kwargs  (все лишние именованные аргументы)
        
# def func(a=5, b=10):
#     return a + b
    
# print(func(20, 20)) 

# def func(*args, **kwargs):
#     print(*args)     # tuple
#     print(kwargs)     # dictionary

# func(1, 2, 3, 'hi', hello = 'hello world', hi = 'hi')

'=======================Виды аргументов======================='
# 1.Позиционные (по позиции)
# 2.Именованные (по названию (памаметр = значение))

# def fucn(a,b,c):
#     pass
# fucn(b=2,c=2,a=1)
#именнованный

'-------------------------Аннотация name : type---------------------------------'
# num : int  = 10
# num : str = 'dfgj'
# name  = 12
# print(num)

# def sum_(a:int, b:int): #a:int - int - просто подсказка, чтоб было понятнее
#     return a + b
# print(sum_(12,123))

# CALCULATOR 1 Mein
# def calc_():
#     num1 = int(input("Введите первое число: "))
#     num2 = int(input("Введите второе число: "))
#     oper = input("Введите операцию: ")

#     try:
#         if oper == '+':
#             print(num1+num2)
#         elif oper == '-':
#             print(num1-num2)
#         elif oper == '*':
#             print(num1*num2)
#         elif oper == '/':
#             print(num1/num2)
#         elif oper == '**':
#             print(num1**num2)
#         else:
#             raise KeyError
#     except ValueError:
#         print('Введите число, а не символ ')
#     except ZeroDivisionError:
#         print('Нельзя делить на ноль')
#     except KeyError:
#         print('Вы ввели не ту операцию')

# calc_()
# # CALCULATOR von Sultan
# def calc_():
#     try:
#         num1 = float(input('Enter number: ')) 
#         num2 = float(input('Enter number: '))  
#         oper = input('Enter oper: ')  
#         if oper == '+':
#             print(num1+num2)
#         elif oper == '-':
#             print(num1-num2)
#         elif oper == '/':
#             print(num1/num2)
#         elif oper == '*':
#             print(num1*num2)
#         elif oper == '**':
#             print(num1**num2)
#         else:
#             raise KeyError
#     except KeyError:
#         print('вы ввели не ту операцию')
#     except ValueError:
#         print('введите число, а не символы')
#     except ZeroDivisionError:
#         print('нельзя делить на ноль')

# calc_()
# code von mir

# db = [
#     {'name': 'Tima', 'password':hash('123456789')},
#     {'name': 'Nick', 'password':hash('098672323')}
# ]

# def in_database(name):
#     for user in db:
#         if name == user['name']:
#             return True
#     return False

# def register(name, password, password2):
#     if in_database(name):
#         raise Exception('Юзер с таким именем уже существует')
#     if password != password2:
#         raise Exception('Пароли не совпадают')
#     user = {'name': name, 'password':hash(password)}
#     db.append(user) 
#     return "Вы успешно зарегистрировались"

# def login(name, password):
#     if not in_database(name):
#         raise Exception('Пользователь не найден!')
#     for user in db:
#         if user['name'] == name:
#            if user['password'] != hash(password):
#                raise Exception('Пароль не верный')
        
#     return "Вы успешно залогинились"

# print(register('katana', '121212', '121212'))
# print(db)
# print(login('katana', '12975r797h'))

'---------------------------------------------------'
# # code von Sultan
# db = [
#     {'name':'Tima', 'password':hash('123456789')},
#     {'name':'Nick', 'password':hash('205221000')}
# ]

# def in_database(name):
#     for user in db:
#         if name == user['name']:
#             return True
#     return False

# def register(name, password, password2):
#     if in_database(name):
#         raise Exception('Юзер с таким именем уже существует')
#     if password != password2:
#         raise Exception('Пароли не совпадают')
#     user = {'name':name, 'password':hash(password)}
#     db.append(user)
#     return 'Вы успешно зарегестрировались'

# def login(name, password):
#     if not in_database(name):
#         raise Exception('Пользователь не найден!')
#     for user in db:
#         if user['name'] == name:
#             if user['password'] != hash(password):
#                 raise Exception('Пароль не верный!')
            
#     return 'Вы успешно залогинились'

# print(register('katana', '123123123', '123123123'))
# print(db)
# print(login('katana', '12amsdbmnasdb'))

# lamdba - анонимная функция, которая записывается в одну строчку / вызвать не можем

# def sum_1(x, y):
#     return x+y

# sum_1(10, 29)
# sum_1(1, 5)
# sum_1(20, 1)

# sum_2 = lambda x, y: x + y
# # sum_2(10, 5) # nur 1 Mal
# print(sum_2(10, 5))


    
    