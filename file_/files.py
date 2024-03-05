'21.02.24======================Модули и пакеты======================'
# любой файл с расширением  ".py" это модуль
# несколько модулей - package / пакеты

'21.02.24======================File======================'
# open() - это функция открывает в опреденном режиме для работы с ней

#1 режим - r -read для читения
#2 w - write (только для записи, каждый раз файл очищается)
#3 a -append - (только для дозаписи, добавляется в конец) 
#4 x - создаеет файл, но если он существует выйдет ошибка

'21.02.24======================Read======================'
# file = open('test1.txt', 'r')
# print(dir(file))
# print(file.readable()) #True
# print(file.writable()) #False
# print(file.read()) # q'fhp   'efhp   ihe (test1.txt) / читает 
# file.seek(0)  #
# print(file.read()) # q'fhp   'efhp   ihe (test1.txt) 
# print(file.read(5)) #first 5 symbol
# print(file.readline())  #читает построчно
# print(file.readline()) 
# print(file.readline(3))  # returned 3 line 
# print(file.readline())
# print(file.tell())
# print(file.readlines()) #возвращает всё как list
# print(file.tell()) #где находится корретка
# 'read -> str, readline -> str, readliines -> list[str]' 
# file.close()

'21.02.24======================Write======================'
# file = open('test1.txt', 'w')   #пишет новый текст свой, очищая старого
# file.write('makers\nHELLO WORLD')
# file.writelines(['hello world\n', 'Makers\n']) 
# # file.close()
'write(str), writlines(list[str, str])'

'21.02.24======================Append======================'
# a - добавляет записи в конец
# file = open('test1.txt', 'a')
# file.write('py33\n')
# file.seek(0) 
# file.write('py32\n') 
# file.close()

'21.02.24======================Контекстный менеджер======================'
# with - Основное преимущество использования with - это гарантия закрытия файла вне зависимости от того, как будет завершён вложенный код.
# with open('test1.txt', 'r') as f:
#     print(f.read()) 

# print(f.closed)  #True  - файл закрыт

# with open('task1.txt', 'r') as f:
#     for line in f.readlines(10):
#         print(line)

# with open('task3.txt', 'w+') as file_:
#     for i in range(10):
#         file_.write(f'{i}*')
#     file_.seek(0)

#     print(file_.read())
    
# with open ('task4.txt', 'r') as file_:
#     print(len(file_.readlines()))

