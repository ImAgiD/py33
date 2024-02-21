"===============================Set==============================="
# set - множетсво, это изменяемый, неупорядоченный, итерируемый, неидексируемый ТД, предназначеннный для хранения уникальных значений.
# Множество может хранит в себе только неизменяемый ТД, если же in set использовать tuple, то внутри tuple не должно быть изменяемого ТД.

# set1 = {5, 6, 1 ,2,3,4,5, True, False, 'hello', None}
# print(set1) #{False, 1,2,3,4,5,6 'hello', None}

# set2 = {1,2,3, ('hello'), 1, [1, 2, 3]}
# print(set2)

"===============================FIFO / LIFO==============================="
# FIFO - first in first out
# LIFO - last in first out

# set3 = {1,2,3,4,2}
# print(set3)  # FIFO

"===============================Merhode Set========================="
# pop - удаляет случайный элемент из set
# set2 = {1,2,3}
# popped = set2.pop()
# print(popped)
# print(set2)
'-------------------'
# add - добавляет элемент в set
# set3 = {1,2, 3, 1, 2, 3}
# set3.add(3)
# print(set3) #{1,2,3} 
'--------------------'
# remove - удаляет элемент по значению -> KeyError, если нет такого значения
# set4 = {1,2,3}
# set4.remove(3)
# print(set4)   #{1,2}
'---------------------'
# discard -  удаляет элемент из множества, если он присутствует. Если нет, то программа продолжает выполнение без ошибок:
# set4 = {1, 2, 3}
# set4.discard(4)
# print(set4)
'---------------------'
# # difference(-) - Возвращает множество, содержащее элементы, к-е присутствуют только в 1 множестве, но отсутствуют во 2 множестве.
# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1 - set2) #{1,2}
# print(set2 - set1) #{4,5}
# print(set1.difference(set2)) #{1,2}
# print(set2.difference(set1)) #{4,5}

# set3 = {5,6,7}
# set4 = {6,8,9}
# print(set3 - set4) #{5,7}
# print(set4 - set3) #{8,9}
'--------------------------'
# symmetric_difference - разница, убирает пов-ся чисел/возвращает разность между двумя множествами, исключая общие элементы
# set1 = {0,2,3,4}
# set2 = {1, 2, 3,4,5, 6} 
# print(set1.symmetric_difference(set2))  # {0, 1, 5, 6}
# print(set1)
# print(set2)
'---------------------------'
# intersection (&) - пересечение/операция нахождения пересечения двух множеств.
# set1 = {1,2,3,4} 
# set2 = {3,4,5,6}
# print(set1.intersection(set2)) #3, 4
# print(set1 & set2) #3, 4
'-------------------------------'
# union объединяет set
# set1 = {1,2,3,4, 5}
# set2 = {4,5,6,7}
# print(set1.union(set2))  #{1,2,3,4,5,6,7}
'-----------------------'
# update - 
# set1 = {1,2,3,4}
# set2 = {4,5,6,7}
# set1.update(set2)
# print(set1)  #{1, 2, 3, 4, 5, 6, 7}


# robert = {5, 7, 11, 10, 28} 
# kail = {1, 5, 14, 8, 22} 
# merri = {19, 20, 3, 11, 10}
# if robert.intersection(kail) or robert.intersection(merri):
#     print("kail merri")
# else:
#     print('no one')

# robert = {5, 7, 11, 10, 28}
# kail = {1, 5, 14, 8, 22}
# merri = {19, 20, 3, 11, 10}
# # if robert.intersection(kail) and robert.intersection(merri):
# #     print('kail merri')
# if robert.intersection(kail):
#     print('kail merri')
# elif robert.intersection(merri):
#     print('kail merri')
# else:
#     print('no one')
    
    
# tilek = {'Dodo', 'ImperiaPizza', "FreshBox"}
# timur = {"OchakKebab", "FreshBox"}
# alexander = {"FreshBox", "KFC"}
# elina = {'Dodo', 'ImperiaPizza', "OchakKebab", "FreshBox", "KFC"}
# print(tilek.intersection(timur.intersection(alexander.intersection(elina))))

# ingredients = {"cыр чеддар","грибы", "соус","шпинат"} 
# ingredients.add('помидор')
# print(ingredients)

# ingredients = {"cыр чеддар","грибы", "соус","шпинат"} 
# ingredients.add('помидор')
# ingredients.discard("колбаса")
# ingredients.remove("шпинат" )
# ingredients.add("базилик")
# print(ingredients)

# set1 = {i*2 for i in range(5)}  # it works
# set2 = {i*2+1 for i in range(5)}
# if set1.intersection(set2):
#     print('Множества пересекаются!')
# else:
#     print('Множества не пересекаются!')   

# print([i.lower() for i in "HELLO"]) 

# a = [{}, {}, {}] 
# inp1 = input("Word: ")
# inp2 = int(input())
# d = 'default value'
# for i in inp1:
#     if i == 1:
#         a.append(inp1[0])
#         print(a)
#     elif i == 2:
#         a.append(inp1[1])
#         print(a)
#     elif i == 3:
#         a.append(inp1[3])
#         print(a)
    
