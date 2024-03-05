'''1) Создайте функцию, которая будет принимать 2 числа, складывать их и возвращать
результат сложения.''' #done
# def sum(a, b):
#     return a+b
# print(sum(1,2))


'''2) Создайте функцию, которая принимает два обязательных параметра. Задача этой
функции выводить тип принятых аргументов.''' #done

# def func(a, b):
#     res1 = type(a)
#     res2 = type(b)
#     print(res1)
#     print(res2)
# func(12, '12')

'''3) Напишите функцию, которая принимает список чисел и возвращает их
произведение.''' #not done
#my
# list_ = [1,2,3,4,5,6]
# neww = list(map(lambda x: x*y  list_))
# print(neww) 

# #richtig
# from functools import reduce
# list_ = [1, 2, 3, 4, 5, 6]
# product = reduce(lambda x, y: x * y, list_)
# print(product)


'''4) Напишите функцию, которая принимает строку и выводит количество гласных,
согласных букв и остальных символов. Используйте только кириллические символы
'''
# def func(*args. **kwargs):
    
# def count_chars(input_str):
#     vowels = "аеёиоуыэюя"
#     consonants = "бвгджзйклмнпрстфхцчшщъь"

#     input_str = input_str.lower()  # Приводим строку к нижнему регистру

#     vowel_count = sum(1 for char in input_str if char in vowels)
#     consonant_count = sum(1 for char in input_str if char in consonants)
#     other_count = len(input_str) - vowel_count - consonant_count

#     print(f"Гласных: {vowel_count}, Согласных: {consonant_count}, Других символов: {other_count}")

# # Пример использования
# input_string = "Пример строки для подсчета символов"
# count_chars(input_string)


'''5) Дан список из имён. Найдите самое длинное имя из списка функцией reduce.''' #done

# from functools import reduce

# list_1 = ['Agi', 'Kama', 'Ayuer', 'Zhan']
# new_list = reduce(lambda x, y: x if len(x) > len(y) else y, list_1)  
# print(new_list)

  
'''6) Дана глобальная переменная num со значением 3. Напишите функцию mul которая
будет возвращать квадрат этой переменной и записывать результат в глобальную
переменную num. Вызовите функцию три раза, и распечатайте переменную num.''' #done
# num = 3
# def mul():
#     res = num**2
#     print(res)
# mul()
# mul()
# mul()
# print(num)

'''7) Есть глобальная переменная, которая обозначает размер самой главной первой
матрешки. Напишите функцию, в которой к размеру главной матрешки прибавляется
размер второй матрешки, который определен в этой функции. То же самое сделайте и
с третьей функцией внутри второй. Верните результат сложения.'''



'''8) Cоздайте переменную list_ и сохраните в ней список из чисел. Создайте новый
список, используя встроенные функции, состоящий из квадратов этих чисел, результат
сохраните в новой переменной result и выведите в консоль.
Обязатьльно нужно использовать builtin functions''' #done

# list_ = [1,2,3,4,5,6]
# result = list(map(lambda x:x**2, list_))
# print(result)



# balance = 0

# def get_salary(amount):
#     print(f'У вас на счету', {get_salary}, 'сом')

# def get_balance():
#     print(f'Вы заплатили', {pay_bills}, 'сом за кабельное тв')

# def pay_bills(*args, **kwargs):
#     print(f'У вас на счету', {pay_bills}, 'сом')


# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()

# result = 0
# def pow_first(x, y):
#     global result
#     result = x**y
#     print(result)
# def pow_second(z):
#     global result
        
#     result= result % z
#     print(result)

# pow_first(2, 3)
# pow_second(3)
# print(result)


# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# for k, v in a.items():
#     if v > 17:
#         print(f'{k}, Вы можете войти в клуб')
#     else:
#         print(f'{k}, извините, Вы не проходите по age-control')

# a = ['father', 'mother', 'brother', 'sister']
# b = []
# for i in a:
#     b.append(i.capitalize())
# print(b)
