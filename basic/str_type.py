"=================String=================="
# Строки - неизменяемый ТД, который предназаначен для хранения текстов, заключенного в одинарные или двойные кавычки

# string1 = "Строка с одинарными кавычками"
# string2 = "Строка с двойными кавычками"
# string3 = 'Не правильная строка"
# string4 = "Don't" #внутри двойной кавычки все одинарные - просто символы
# string5 = """
# Многострочный текст в одинарных кавычках, тут можно ставить 'любые' "кавычки
# """

# string6 = 'hello' + ' ' + 'world' #объединение
# print(string6)

# string7 = 'A' * 8 #умножение
# print(string7)

"=================Экранизация строк=================="
'\n'  # - это вспомогательный функционал, переносит текст на новую строку
# print("hello\nworld")
# hello
# world

'\t' # табуляция
# print('hello\tworld')
#hello   world

# str1 = 'don\'t' #отображает кавычку -> don't
# print(str1) 

# str2 = "don\"t" #отображает кавычку " -> don"t
# print(str2) 

# str3 = 'Символ - \\'
# print(str3)

'\v' #лестница / перенос на новую строку со смещением вправо на длину предыдущей строки
# print('hello\vworld\vmakers\vbootcamp') 
# print('hello\vworld\vmakers\n\vbootcamp') #добавили \n

'\r' #перенос каретки на начало строки
# print('Makers bootcamp \rHi')
# выйдет Hikers bootcamp = Hi_ -> _Ma + kers = Hi_kers

"=================Форматирование строк=================="
#1 Чтобы правильно отображать сторк
# title = 'IPhone14'
# price = 150
# format_1 = 'Мой телефон', title, 'стоит', price, 'долларов'
# print(format_1) 

# format_2 = f'Мой телефон {title} стоит {price}$' #f - помогает понять строки и тексты
# print(format_2) 

#2
# string = 'Название: {} Цена: {}'
# print(string.format('IPhone', 150)) #благодаря "{}" и ".format" 

#3
# string = 'Название: %s Цена: %s' # вместо "{}" поставили "%s" и "%s"
# print(string% ('iphone', 150))

"=================Методы строк=================="
# Методы - инструменты/ функции, которые относятся к определённому классу, к ним можно обращаться через точку

# print(dir(str))
 
string = 'HELLO' #makers -> hello world, чтоб лучше понять 

# print(string.upper()) #makers - MAKERS
# print(string.lower()) #makers - makers
# print(string.swapcase()) #MaKErS - mAkeRs = umgekehrt


# print(string.title()) #helLo woRLd -> Hello World
# # print(string.capitalize()) #hello world -> Hello world
# print(string.center(11, '-')) # '---hello---'

# print(string.count('l')) # hello -> 2 считает символы

# print(string.startswith('a')) # -> False   с какой буквы начинается слово
# print(string.startswith('h')) # -> True
# print(string.startswith('H')) # -> False
# print(string.endswith('o')) # -> True - заканчивается слово
# print(string.endswith('llo')) # -> True
# print(string.endswith('H')) # -> False

# print(string.islower()) #True, if string -> 'hello'
# print(string.islower()) #False, if string -> 'Hello'
# print(string.isupper()) #False, if HELLO -> True'

# string = '1235243'
# print(string.isdigit()) #True, если текст число - проверка на цифры в тексте
# print(string.isalpha()) #False, если текст число и наоборот - проверка на буквы в тексте
# string = 'makers65134e'
# print(string.isalnum()) #True, проверка и на буквы, на цифры в тексте или все вместе, но не символы -> False / alpha + nummer

# string = 'hello world makers boootcamp'
# print(string)
# print(string.split('o')) #разделить на части 'по умолчанию' через пробелы. если "о" то разделяет "о"и сам символ исчезает
 
"=================Индексы=================="
# Индекс- порядковый номер элемента в последоватеьности (символа в строке),(индексация начинается с 0)

'h e l l o  w o r l d'
#1 2 3 4 5 6 7 8 9 10
#-10 -9 -8- -7 -6 -5 -4 -3 -2 -1

# string = 'hello world'
# print(string[0])  #'h'
# print(string[7]) #'o'
# print(string[10]) #'d'
# print(string[-1]) #'d'

"=================Срезы=================="
# string[start:end:step]
# # срезы - подстроки 
# string = 'hello world'
# print(string[3:9]) #'lo wor'  l- не вкл
# print(string[6:11]) #'world'
# print(string[6:]) #'world' после ":" выйдет всё
# print(string[:]) #'hello world'
# print(string[0:]) #'hello world'
# print(string[:5]) #'hello'

# string = 'hello world'
# print(string[::-1]) #зеркально dlrow olleh
# print(string[::2]) #шаг hlowrd  2  1+3+5+7+9
# print(string[::3]) #шаг hlwl   3  1+4+7+10
# print(string[::4]) #шаг hor  4  1+5+10

string = 'hello'
string = string.upper()
print(string)     #HELLO
"=================List=================="




























