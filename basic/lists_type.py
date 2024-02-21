"===============================List==============================="
# списки'[]' - неизменяемый, индексируемый, упорядоченный, итерируемый ТД, предназначенный для хранения любых данных в определенном порядке
# list1 = [1,2,3,4, 'makers', 'num', [1,2,3 [1,3,4]], True, False, None, 12]
# print(list1[2: -1])
# print(list1[5][2])
# print(list1[6][2][2])
# list1 = [1, 2, 3, 4, 'makers', 'num', [1, 2, 3, [1, 3, 4]], True, False, None, 12]
# print(list1[2:-1])
# print(list1[2][5])


# string = 'hello '
# res = list(string) 
# print(res)  #['h', 'e', 'l', 'l', 'o']

# list_ = []
# list_ = list()
# list_ = [2]*10
# print(list_)

"=============================Методы списков==============================="
#1 - append - добавление элементы в конец списка
# list_ = []
# list_.append(True)
# list_.append('text')
# list_.append(123)
# list_.append([123]) 
# print(list_)

#2 - pop - удаляет элемент из списка по индексу и возвращает удаленный элемент, если не передать индекс в скобки, то удаляет последний элемент

# list1 = [5,135, True, 123, 'q',5,5]
# rm_elem = list1.pop(3)
# print(rm_elem) #123
# print(list1) # rest

# 3 -remove - удаление элемента из списка по значению
# list_ = [12, 'makers', 234, True, 0,1,1,1, False]
# list_.remove("makers") 
# # list_.pop(0) 
# print(list_)

# count - метод, который считает кол-во элементов списка
# list_= [0, 12, 'hi', True, False, True, 0,1,1,0,0,0]
# count_of_elem = list_.count(12) #4
# print(count_of_elem)

# index - возвращает индекс первого вхождения указанного элемента

# list2 = [12, 1, 1, 1, 'hi', None]
# index_ = list2.index('hi') 
# print(index_) #4

'--------------------'

#insert - добавляет элемент в список по указанному индексу
# list_= [87,11,23,'hi', 5, 1 ,True, 'World']
# list_.insert(4, 'makers')
# print(list_)
# '--------------------'

#extend - добавляет элементы списка в  другой список
# list1 = [0,0,0]
# list2 = [1,2,3]
# list1.extend(list2)  #[0,0,0, 1,2,3]
# print(list1)
# '--------------------'

#reverse - переворачивает / расставляет элементы в обратном порядке
# list_ = [1,2,3,3, None,[1,2,3]]
# list_.reverse()
# print(list_) # [[1,2,3], None, 3, 3, 2, 1]

#sort - сортирует список, состоящий из элементов одного типа данных
# list_ = [23, 1, 24, 23, 123, 0]
# list_.sort()
# print(list_)

# list_ = ['a', 'A', 'b', 'B']
# list_.sort() # 'A', 'B', 'a', 'b'
# print(list_)


# list_ = ['makers', 'hi', 'asd', 'qwerty']
# print(list_)
# list_.sort(key=len, reverse=True) # 'makers', 'qwerty', 'asd', 'hi'


# list_ = ['hi', 12, 'hello', 'world']
# list_.sort() #ОШИБКА
# print(list_)

# copy 
# # deecopy

# list_ = ['makers', 'hi', 'asd', 'qwerty']
# list_.copy()
# print(list_)


"============================= Tuple==============================="
#кортеж - неизменяемый, упорядоченный, итерируемый ТД, литералы (,)

# tuple_ = (1,2,3, True, False, None, 'hi')
# print(dir(tuple)) # посмотреть все функции tuple

# есть 2 метода это - index и count

# a = 12, 3, 4
# print(a) #(12, 3, 4)

# my_tuple = (10, 'hello', 3.14, True, 'hello')
# index_of_hello = my_tuple.index('hello')
# print(index_of_hello) # Возвращает 1, индекс первого 'hello' в кортеже


# name_of_friends = ['Maya', 'April', 'Nagi', 'Kama', 'Zhasmin']
# for i in name_of_friends:
#     print(i)


# a = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100) # Кортеж
# b = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # Список


# print(a.__sizeof__()) # Размер кортежа
# print(b.__sizeof__()) # Размер списка

