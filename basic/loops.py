"================================ Циклы ================================"
# цикл - это блок кода, который отрабатывается несколько раз
'''' Итерируемый объект - это какая-та последовательность, которую мы можем перебрать.
Нап:
[list]
"string"
{dict}
(tuple,)
''' 
'''Итерация - процесс перебора итерируемго объекта повторение действия'''
# 1. for - это цикл, который работает с итерируемым объектом. Цикл заканчивает
# работу когда он доходит до последнего элемента итерируемого объекта'''

#2. while - это цикл, который работает до тех пор, пока условие верное

# 'FOR'  #bis zum Ende #ДАКАНСА 
# list_ = [1, True, 'hello', 0, 123]
# for elem in list_:
#     print(elem)
     
'WHILE' #bis True. Код работает до след действия 
# count_ = 0
# while count_ < 10: #False
#     print(count_) #bis True
#     count_ = count_ + 1 


'======================Ключевые слова в циклах======================='
# break - оператор, который останаливает работу цикла (ломает)
# continue - оператор, который пропускает итерацию (продолжает с другой итерации)
# range (start, end, step) - генератор последовательности от start до end(не включительно)/ создает диапазон
# print(list(range(1, 11))) #[1,2,3,4,5,6,7,8,9,10]

# for i in range(0, 21):
#     if i == 10 or i == 5:
#         continue
#     print(i) 


# for i in ['1', '2', '3', 'helloworld', '12']:
#     if i.isdigit():
#         print(int(i))  #'1' - 1, '2'-2, '3'- 3, Error
#         print('Все прошло хорошо')
#     elif i.isalpha():
#         print('Я не могу перевести буквы в число')
#         break
#     else:
#         print('Я нашёл символы')

# count = 0
# password = input('Введите пароль: ')
# while True:
#     print(count)
#     if str(count) == password:   # 1 == 1
#         print(("Вот ваш пароль: ", password))
#         break
#     count += 1 #count = count + 1

# while True:
#     if count != 0:
#         continue
#     if count == 1:
#         break
#     print(count)
#     count += 1 #count = count + 1
# else:
#     print('hi')

# else - в цикле работает тогда, когда условие цикла становится False, если же сработал break то, else не работает

