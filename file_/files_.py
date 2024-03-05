'22.02.24==============РЕЖИМЫ=============='
# r+
# w+
# a+

'''r+ (a)' = Открывает файл в режиме чтения + в  режиме append'''

# with open('test1.txt', 'r+') as file:
#     print(file.read())
#     file.write('py33')
#     file.seek(0)
#     print(file.read())

'''w+ (r)' = Открывает файл в режиме записи + read (чтения)'''

# with open('test1.txt', 'w+') as file:
#     file.write('qwertyoqqq')
#     file.seek(0)
#     text = file.read()

'''a+ (r)' = Открывает файл в режиме дозаписи + read (чтения)'''

with open('test1.txt', 'a+') as file:
    file.write('000')
    print(file.read())
    file.seek(0)
    file.write('hello\n')
    file.seek(0)
    print(file.read())
    
'22.02.24==============CSV=============='

# csv - формат файла
# import csv 

# with open('data.csv') as file:
#     data = csv.reader(file)
#     colm = next(data)
#     print()
#     print('Поле', colm)
#     # for product in data:
#     #     print(product)
    
# def read_last(lines: int, filename: str):
#     with open(filename, 'r') as file:
#         data = file.readlines() #list[str]
#         data.reverse()
#         if lines >= len(data):
#             for line in data:
#                 print(line.replace('\n',''))
#         else:
#             count = 1
#             for line in data:
#                 print(line.replace('\n',''))
#                 if lines == count:
#                     break
#                 count += 1      
# read_last(20, 'test1.txt')

# def longest_words(filename: str):
#     with open(filename) as file:
#         data = file.read()
#     data2 = data.split()
#     list_ = []
#     max_word = max(data2, key = len)
#     for word in data2:
#         if len(max_word) == len(word):
#             list_.append(word)
#     if len(list_) ==1:
#         return list_[0]
#     return list_
# longest_words('')

        


