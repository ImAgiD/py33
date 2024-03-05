'21.02.24====================JSON===================='
# JavaScript Objekt Notation - универсальный формат, в котором мы можем хранит данные в типах данных, понятных почти для всех языков программирования

import json
# json_list = '[1,2,3,4,5]'
# python_list = json.loads(json_list)  # пменяет jason str на list python
# print(python_list)  # [1,2,3,4,5]

# json_list = 'true'
# python_data = json.loads(json_list)  # поменяет json str на list python
# print(python_data)  # True

# with open ('test.json', 'r') as file:
#     python_data = json.load(file)
    
# print(python_data) 
    
    
# десериализация - перевод данных с json строки в python объекты
# 1 метод loads - метод для десериализации с json строки
# 2 метод load - метод для десериализации с json файла

# python_data = None
# json_data = json.dumps(python_data)  # поменяет json str на list python
# print(json_data)  # null 

# python_data = [1,2,3,4, True, False, None, 'makers']
# with open ('test.json', 'w') as file:
#     json.dump(python_data, file)   # python data получаем
     
# сериализация - перевод python объектов в json строку
# 1 метод dumps - метод для сериализации в json строку
# 2 метод dump - метод для сериализации в json файл

# в json нет set, а с tuple проблемы
