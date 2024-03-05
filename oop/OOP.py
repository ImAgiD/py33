'04.03.24================OOP================='
# OOP - Objekt-orientated programing
# ООП - Объектно-ориентированное программирование (парадигма / способ)

# class Person:
#     #переменнная внутри класса = аттрибуты
#     head = 1
#     body = 1
    
#     def __init__(self, name, age): #функция внутри класса = методы
#         self.name = name
#         self.age = age
        
#     def walk(self):
#         print(f'{self.name} ходит')
        
# obj1 = Person('Tima', 21)
# obj2 = Person('Katana', 21)
# print(obj1.name, obj1.age, obj1.head, obj1.body)
# print(obj2.name, obj2.age, obj2.head, obj2.body)

# obj1.walk()
# obj2.walk() 

'Объекты, экземпляры, instance - конечный продукт, созданный по шаблону класса (он перенимает все аттрибуты и методы класса)0'

# class A:
#     var1= 'аттрибут самого класса'
    
#     def __init__(self):
#         self.var2 = 'аттрибут объекта'
        
# print(dir(A)) # кдасс не видит аттрибуты объекта

# obj1 = A()
# print(dir(obj1))# объект видит аттрибуты класса

'self = это ссылка на объект'
# Что отрабатывает при создании объекта
# obj1 = Person('makers', 5)
'__new__ - создает пустой объект'
'__init__ - инициализирует этот объект, создает аттрибуты со значениями внутри пустого объекта / благодаря self он ссылается на пустой объекь'

# class Calc:
#     def add(self, a, b):
#         return a+b 
    
#     def sqrt(self, a):
#         return a ** 0.5
    
#     def percent(self, total, _percent):
#         return (total * _percent) / 100
    
# calc = Calc()
# print(calc.add(10, 20))
# print(calc.sqrt(81))
# print(calc.percent(34250, 13)) 

# class  Sniper:
#     health = 100
    
#     def __init__(self, name):
#         self.name = name
        
#     def shoot(self, sniper):
#         sniper.health -= 20
#         print(f'атаковал {self}')
#         print(f'У {sniper} осталось {sniper.health}')
        
#     def __str__(self):
#         return self.name
        
# sniper1 = Sniper('Anonym')
# sniper2 = Sniper('Tima') 

# sniper1.shoot(sniper2)   
# sniper2.shoot(sniper1)
# sniper1.shoot(sniper2)   
# sniper2.shoot(sniper1)   
# sniper1.shoot(sniper2)   
 
# import random
# while sniper1.health > 0 and sniper2.health > 0:
#     choice = random.randint(1,2)
#     if choice == 1:
#         sniper1.shoot(sniper2)
#     elif choice == 2:
#         sniper2.shoot(sniper1)
        
# if sniper1.health:
#     print(f'Выиграл снайпер {sniper1}')
# else:
#     print(f'Выиграл снайпер {sniper2}')
    
    
# class Taxi:
    
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km

#     def get_total_cost(self, km):
#         self.km = km
#         print(f'стоимость поездки: {self.km * self.cost_km} сом')

# taxi1 = Taxi("Namba, 50, 30")
# taxi2 = Taxi("Yandex, 45, 40")
# taxi3 = Taxi('Jorgo, 50, 45')

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14)) 

