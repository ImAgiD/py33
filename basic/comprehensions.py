"05.02.24===============================Comprehensions==============================="
# Comprehensions - генераторы, с помощью которых можем создавать последовательности, используя цикл for в одну строку
# элемент for элемент in последовательность
# элемент for элемент in последовательность if фильтр (условие)
# элемент if условие1 else элемент2 for элемент in последовательность
# #1 Methode
# compr_ = [i if i % 2 == 0 else 'elem' for i in range(10)] # i for i in range(10) if i % 2 == 0 / если хотим без else писать
# print(compr_)
# #2 Methode
# compr_1 = []
# for i in range(10):
#     if i % 2 == 0:
#         compr_1.append(i)
#     else:
#         compr_1.append('elem')
# print(compr_1)

# 'создайте новый лист используя старого. В новом лисет должны быть только True'
# list1 = [12, None, 'hi', 123, 1, 6, 2, True, 0, False]
# new_list = [i for i in list1 if bool(i)]
# print(new_list)

# #1
# new_list2 = [i if bool(i) else 0 for i in list1 ] # with Comprehensions
# print(new_list2)
# #2
# new_list3 = []
# for i in list1:
#     if bool(i):
#         new_list3.append(i)
#     else:
#         new_list3.append(0)
# print(new_list3)

'[12, 3, 0, 34, 9, 7] -> ["четное", "нечетное","четное", "четное","нечетное","нечетное", ]'
list111 = [11, 12, 3, 0, 34, 9, 7]
newlist111 = ["четное" if i % 2 == 0 else "нечетное" for i in list111]
print(newlist111)

# list5 = [1, 'hi', 123, 'hello world', True, 'makers', False]

# new_list2 = []
# for i in list5:
#     if type(i) == str:
#         new_list2.append(i)
# print(new_list2)

# new_list2 = [i ** 2 for i in list5 if type(i) == int]
# print(new_list2)

"05.02.24===============================Виды comprehensions==============================="
# изменяемый ТД
# list comprehensions -> []
# dictcomprehensions -> {:}
# set comprehensions -> {} уникальные значения

# comprehensions генератор -> ()
'dict comprehensions'
# {1:1, 2:4, 3:9, 4:16, 5:25}

# dict1 = {i:'values' for i in range(1,5)}
# print(dict1) # {1: 'values', 2: 'values', 3: 'values', 4: 'values'}

# dict2 = {'a': 1, 'b': 2,'c': 3}
# new_dict2 = {v:k for k, v in dict2.items()} # {1: 'a', 2: 'b', 3:'c'}
# print(new_dict2)

# new_dict3 = {v**2:v for v in dict2.values()}
# print(new_dict3)

'set comprehensions'   #принимает только измен ТД
# set_ = {i for i in range(11) if i % 2 == 0}
# print(set_)

# set1 = {12, 34, 1, 1, 1, 1, 'hi', 'Hello' , 'hello', 123, None}
# set2 = {i.swapcase() for i in set1 if type(i) == str} #{'hELLO', 'HELLO', 'HI'}
# print(set2) 

'05.02.24===============================Вложеные Comprehensions==============================='

# создайте словарь, где ключи будут числаот 1 до 5, а значениями - списки с числами от 1 до этого числа
# {1:[1], 2:[1,2], 3:[1,2,3],4:[1,2,3,4], 5:[1,2,3,4,5]}
dict_ = {}
for i in range(1, 6):
    key = i
    values = [j for j in range(1, 2)] 
    dict_[key] = values
print(dict_) 

dict2 = {i: [j for j in range(1, i+1)] for i in range(1, 6) }
print(dict2)

''' создать список, состоящий из 10 списков, в которых строка "hello world" повторяется по 5 раз '''



