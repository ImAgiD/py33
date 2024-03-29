'05.04.24================Принципы ООП================'
# Наследование
# Инкапсулация
# Полиморфизм
# Абстракция
# Ассоциация - Композиция, Агрегация

'05.04.24================Наследование================'
# Принципы - правилы которых надо следовать вОП
# Наследование - принцип ООП, в котором мы можем унаследовать, переопределять и использовать в дочернем классе все аттриубты и методы родительского класса

# class A:
#     def method(self):
#         print('Метода класса А')
        
# obja = A()
# obja.method()

# class B(A):
#     '''
#     Наследовали все методы и аттрубиуты родительского класс А
#     '''
    
# objb = B()
# objb.method()

# class C(A):
#     def method(self):
#         print('Метод в классе С')
    
# objc = C()
# objc.method()
'-----------------------------------------------'
# class A:
#     x = 'х в классе А'
#     y = 'y в классе А' 

# class B(A):
#     x = 'х в классе В'

# print(A.x) #х в классе А
# print(A.y) #y в классе А

# print(B.x) #x в классе B
# print(B.y) #y в классе А

'-----------------------------------------------'
# 'mro (method resolution order)' - порядок поиска аттрибута

# class A:
#     ...
    
# class B(A):
#     ...
    
# # B.a
# #[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
# print(B.mro())  

'-----------------------------------------------'
# super() - это функция, благодаря которой мы можем обращаться к родительскому  классу

# class A:
#     def my_range(self, n):
#         return list(range(n+1))

# class B(A):
#     def my_range(self, n):
#         list_ = super().my_range(n) #[0, 1, 2, 3, 4, 5]
#         list_.append(0)
#         return list_
    
# print(B().my_range(10)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]

'05.04.24================Виды наследование================'
# одиночное наследование (когда наследуемся в дочернем классе от 1 класса)
# множественное наследование(когда наследуемся в дочерном классе от нескольких родительских)
# многоуровневое наследование( когда наследуемся от класса у которых есть родитель)
# иерархичесоке наследование (когда от одного родителя много дочерних классов)
# гибридное наследование (когда используются несколько видов наследования)
# rambar
# class A:
#     def __str__(self):
#         return 'A'
    
# class B:
#     def __str__(self):
#         return 'B'
    
# class C(A, B):
#     ...
    
# obj_C = C()
# print(obj_C) 
    
# print(C.mro())
    
# Проблема перекрестного наследовния не решена

# class A:
#     ...
    
# class B:
#     ...
    
# class E(A, B):
#     ...
    
# class D(B, A):
#     ...
    
# class F(E, D):
#     ...

class Password:
    def __init__(self, password):
        self.passw = password

    # def validate(self):
    #     # Проверка длины пароля
    #     if len(self.passw) not in range(8, 15):
    #         raise ValueError('Password should be longer than 8, and less than 15')

    #     # Проверка наличия хотя бы одной цифры в пароле
    #     if not any(c.isdigit() for c in self.passw):
    #         raise ValueError('Password should contain numbers too')

    #     # Проверка наличия хотя бы одной буквы в пароле
    #     if not any(c.isalpha() for c in self.passw):
    #         raise ValueError('Password should contain letters as well')

    #     # Проверка наличия хотя бы одного из специальных символов в пароле
    #     if not any(i in ['@', '#', '&', '$', '%', '!', '~', '*'] for i in self.passw):
    #         raise ValueError('Your password should have some symbols')

    #     return 'Ваш пароль сохранен.'

    def __str__(self):
        # Возвращаем строку из звездочек той же длины, что и пароль
        return '1' * len(self.passw)

# Пример использования
obj = Password('ads112')


