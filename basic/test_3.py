# 12.02.24 Сheck Yourself week 3
'---------------------------------------------'

# 1) У вас есть список чисел от 1 до 10,Напишите код, чтобы создать новый
# список. содержащий квадраты только четных чисел из исходного списка,
# использовать comprehension .   #done
 
# list_ = [i**2 if i % 2 == 0 else i for i in range(1,10)]
# print(list_)

'---------------------------------------------'
# 2)У вас есть словарь содержащий названия предметов в качестве ключей и
# их оценки в виде чисел Напишите код чтобы создать новый словарь где
# ключами будут те же оценки а значениями будут значения True или False,
# True будет если оценка будет равна или больше 4
# пример) ratings = {item: 1, item2: 5, item: 4}
# вывод >>> {item: False, item2: True, Item: True}     #done

# ratings = {'item1': 1, 'item2': 2, 'item3': 3, 'item4': 4}
# new_dict = {}
# for k, v in ratings.items():
#     if v % 2 == 0:
#         v = True
#         new_dict[k]=v
#     else:
#         v = False
#     new_dict[k] = v
# print(new_dict)

'---------------------------------------------'
# 3) У вас есть список чисел. Напишите код, который попытается получить
# элемент по индексу, введенному пользователем, из этого списка. Если
# индекс выходит за пределы списка, программа должна вывести сообщение
# о выходе за пределы списка.   #done

numbers_list = [1, 3, 5, 7, 8, 12]
neww = numbers_list[int(input())]
print(neww)  # Если индекс выходит за пределы списка, автоматически выходит уже IndexError: list index out of range 

# neww = (numbers_list[5])
# print(neww) 

'---------------------------------------------'
# 4) Напишите функцию check_numbers(), которая принимает число в
# качестве аргумента и возвращает булево значение True, если число четное,
# и False, если число нечетное.   #done

# def check_numbers(a):
#     if a % 2 == 0:
#         print(True)
#     else:
#         print(False)

# check_numbers(12)  #True

# '---------------------------------------------'
# # 5) Напишите функцию length_text() которая принимает текстовую строку
# и возвращает список длин слов в этой строке  #done

# text = str(input())
# def length_text(text):
#     print(len(text))
# length_text(text)
 
'---------------------------------------------'
# 6) напишите как создать виртуальное окружение и назовите его makers

# python3 venv makers  / ?poetry  

'---------------------------------------------'
# 7) Напишите функцию length(), чтобы она определяла количество цифр в
# числе, не используя преобразование числа в строку. Для этого используйте
# логику и математические операции.

# def length():
    
    

# >>> print(length(999999)) # 6

'---------------------------------------------'
# 8) напишите как мне установить библиотеку и как его удалить , библиотека называется flake8

# pip/bin/flake8?     pip flake8?

'---------------------------------------------'
# 9) У вас есть список чисел. Напишите код, чтобы создать новое
# множество, содержащее квадраты уникальных чисел из этого списка.

# list1 = [1,2,3,4,5,6,7,8,9]
# set1 = {}
# for i in list1():
#     set1.append(i**2)
# print(set1)

'---------------------------------------------'
# 10) напишите функцию palindrome которая принимает в себе число и
# возвращает True если палиндром а если нет то False  #done

# def palindrome(num):
#     num = str(num)
#     if num == num[::-1]:
#         print(True)
#     else:
#         print(False)
        
# palindrome(122) #False
