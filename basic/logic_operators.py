"================Логические и условные операторы================"
# Логические операторы, выражения, которые возвращают True если выражение верное, False = если наоборот. 
# 'Равентство'
# 5 == 6 # False
# 5 == 5 # True

# 'Не равентство'
# 4 != 5 #True
# 5 != 5 #False

# 'Больше'
# - 5 > 2  #False
# 10 < 11 #True

# 'Меньше'
# 5 < 6 #True
# 7 < 2  #False

# 'Больше или равно'
# 5 >= 10 #False
# 10 >= 5 #True
# 5 >= 5 #True

# 'Меньше или равно'
# 10 <= 5 #False
# 5 <= 10 #True
# # 5 <= 5 #True

# # a = 10
# # b = '10'
# # print(a == b) #True or False

# # a = 'Hello'  #ascii-code - A < B
# # b = 'Hello 12345'
# # print(a < b) # True считает кол-во символов во строке < / > 



# "================ And, Or, Not ================"
# # И
# # Или
# # Не - 

# a = 5
# b = 6 

# #True и True --> True     
# a == 5 and b == 6 #True
# #True  и False  --> False
# a == 5 and b == 3
# #False  и False  --> False
# a > 10 and b < 2 

# #Возвартится True, если с права True И слева True
# #если хотябы с одной стороны будет False,или сразу c 2 сторонах, то возвартится False

# 'OR'
# a = 20
# b = 5
# #True или True  ---> True
# a == 20 or b > 1
# #True или False  ---> True
# a == 20 or b < 1
# #False  и True  --> True
# a > 100 or b == 5
# #False и False  --> False
# a < 10 or b < 1

# #если хотябы с одной стороны будет True, то возвартится True

# 'NOT'
# #not False = True
# #not True = False

# a = 5
# not a < 6 #False
# print(not a != 5) #True
# print(not  not not not not a != 10) #True

# "================ Boolean Type ================"
# #Булевой ТД имеет всего 2 значения 
# # Булевой ТД используется в условных операторах для выполнения ситуативных задач

# bool(1) #True
# bool(0) #False
# bool(-123) #True

# bool('hello') #True
# bool(' ') #True
# bool('') #False

# bool(True) #True
# bool(False) #False

# "================ None Type ================"
# # None - неизменяемый ТД с одним значением - None, который использвуется для обозначения отсутсвия значения.

# a = None
# print(a) 
# bool(None) #True
# bool("None") #False

# "================Условные операторы================"
# # if/elif/else - условные операторы - конструкция, которая используется для того, чтобы при разных входных данных код работал по разному

# # if: #на улице идёт дождь:
# # pogoda == 'dojd'
# # if pogoda == 'dojd'

# # if условие 1:
# #     тело1
# # if условие1:
# #     Тело1 #тело1 будет выполняться если условия1 = True
# # else:
# #     тело2 #тело2 будет работать во всех других условиях
    
# # '________'
# # if условие1:
# #     тело1
# # elif условие2:
# #     тело2
    
    
# # if условие1:
# #     тело1
# # elif условие2:
# #     тело2
# # else:
# #     тело3
    
# num = input('Введите число: ')

# if num > 0:  #Должен быть 1
#     print(f'Число {num} - положительное')
# elif num < 0: #Может быть 1+
#     print(f'Число {num} - отрицательное')
# else: #Должен быть 1
#     print('Это ноль/If не сработал, elif не сработал')   

# num1 = int(input('Введите первое число:'))
# num2 = int(input('Введите второе число:'))
# oper = int(input('Введите оператор:'))

# if oper == '+':
#     print(num1+num2)
# elif oper == '-':
#     print(num1-num2)

# "================Тернарный операторы================"
# #only 'IF' and 'ELSE'
# # telo1 if uslovlie else telo2

# a = -20
# res = a ** 2 if a > 0 else a - 2
# print(res) 



x=int(input())
y=int(input())
if x%y==0:
    print('x делится на y')
    print('частное: ',x//y)
else:
    print('x не делится на y')
    print('частное: ',x//y)
    print('остаток: ',x%y)

    

    




