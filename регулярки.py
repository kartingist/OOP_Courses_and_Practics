# ^ - начало строки
# $ - конец строки
# ^начало или конец$

# \b - начало и конец слова
# \bPy bkb on\b

# | - или

# [] - любые из символов, перечисленных в скобках
# [0-9а-яА-Я]

# [^0-9] - отрицание, 1 символ все кроме чисел

# \d - любая цифра
# \D - любая не цифра
# \w - любой алфавитно цифровой символ(оба языка) или  _
# \W - любой не алфавитно цифровой символ(оба языка) или не _
# \s - пробельный символ, табуляция или разрыв строки
# \S - любой не пробельный символ
# . = 1 любой символ

# {min, max} квантификатор, количество элементов
# [0-9]+ - от 1 до бесконечности
# [0-9]* - от 1 до бесконечности
# [0-9]? - 0 или 1 вхождение

# +*?{}()\ - спец. символы которые нужно экранировать символом \ перед символом

# ((http|https)(://)(a-zA-Z0-9.-_)\.(ru|com)) - группы, пример регулярки для сайта
# \b или $n - указание номера группы

# (.*?) - обычно обозначают любой текст



# re.search() # возвращает первую попавшуюся часть строки
# re.match() # поиск происходит в начале строки
# re.sub(что, на_что, где) # поиск и замена данных на новые
# re.split(что, какой разделитель, где) # разделяет строку опираясь на символ разделитель
# re.findall() # возвращает все совпадения с шаблоном в строке(не работает с группами)
# re.finditer() # то же самое но работает с группами
# re.compile()

# FLAGS
# re.match(r'(?i)[a-z]+', string) флаг i убирает чувствительность к регистру
# re.match(r'([a-z]+', string, re.I) флаг I убирает чувствительность к регистру


import re
# пример валидации мыла
def email_input():
    s=input('Input email:')
    reg = r"((^[a-zA-Z0-9]{3,15}@([a-zA-Z]{0,10})\.(ru|com)$))"
    match = re.match(reg, s)
    if match != None:
        print(f'You email: {s}')
    else:
        print("uncorrect value")

email_input()

# регулярка для номера полиса на согазе)
r'^((IB811|MB811)|(^[0-9]{3}))\-[0-9]{7}$/u'