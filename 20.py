'''
 Создайте класс City, у которого есть:

конструктор __init__, принимающий единственный аргумент - название города.
 Вам необходимо сохранить его в качестве атрибута экземпляра name, причем вам
  нужно преобразовать переданное имя города таким образом, чтобы первая буква
  каждого слова была заглавной, а остальные оказались строчными (пример "new york" - > "New York")

переопределить метод __str__ таким образом, чтобы он возвращал имя города

переопределить метод __bool__ так, чтобы он возвращал False ,если название города заканчивается
 на любую гласную букву латинского алфавита (a, e, i, o, u), в противном случае True
'''

# class City:
#     def __init__(self, name):
#         self.name = name.title()
#
#     def __str__(self):
#         return self.name
#
#     def __bool__(self):
#         x=['a', 'e', 'i', 'o', 'u']
#         result=True
#         for i in x:
#             if i == self.name[-1]:
#                 result = False
#                 break
#             else:
#                 result = True
#
#         return result
#
#             #     return True
#             # else:
#             #     return False
#
# p1 = City('new york')
# print(p1)  # печатает "New York"
# print(bool(p1))  # печатает "True"
# p2 = City('SaN frANCISco')
# print(p2)  # печатает "San Francisco"
# print(p2 == True)  # печатает "False"


'''
Сейчас вам нужно создать класс Quadrilateral (четырехугольник), в котором есть:

конструктор __init__. Он должен сохранять в экземпляр класса два атрибута: width и height. 
При этом в сам метод __init__ может передаваться один аргумент(тогда в width и height присваивать 
это одно одинаковое значение, тем самым делать квадрат), либо два аргумента( первый идет в атрибут width, второй - в height)
переопределить метод __str__ следующим образом: 
если width и height одинаковые, возвращать строку "Куб размером <width>х<height>
в противном случае, возвращать строку "Прямоугольник размером <width>х<height>
переопределить метод __bool__ так, чтобы он возвращал True, если объект является кубом, и False в противном случае
'''
class Quadrilateral:
    def __init__(self, *args):
        if len(args)==1:
            self.width = self.height = args[0]
            # print(self.width, self.height)
        elif len(args)==2:
            self.width = args[0]
            self.height = args[1]
            # print(self.width, self.height)
    def __str__(self):
        if self.width == self.height:
            return f"Куб размером {self.width}х{self.height}"
        elif self.width != self.height and self.height != 0 and self.width != 0:
            return f"Прямоугольник размером {self.width}х{self.height}"

    def __bool__(self):
        if self.width == self.height:
            return True
        else:
            return False

q1 = Quadrilateral(10)
print(q1)  # печатает "Куб размером 10х10"
print(bool(q1))  # печатает "True"
q2 = Quadrilateral(3, 5)
print(q2)  # печатает "Прямоугольник размером 3х5"
print(q2 == True)  # печатает "False"
