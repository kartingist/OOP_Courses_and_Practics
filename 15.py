'''

Создайте класс Person, у которого есть:

конструктор __init__, принимающий 3 аргумента: name, surname, gender.
Атрибут gender может принимать только 2 значения:
"male" и "female", по умолчанию "male".
Если в атрибут gender передается любое другое значение,
печатать сообщение: "Не знаю, что вы имели ввиду?
Пусть это будет мальчик!" и проставить атрибут gender значением "male"

переопределить метод __str__ следующим образом:
если объект - мужчина (атрибут gender = "male"), возвращать строку "Гражданин <Фамилия> <Имя>
если объект - женщина (атрибут gender = "female"), возвращать строку "Гражданка <Фамилия> <Имя>

'''

# class Person:
#     def __init__(self, name, surname, gender='male'):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         x= ['male', 'female']
#         if gender not in x:
#             print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
#             self.gender='male'
#
#
#     def __str__(self):
#         if self.gender=="male":
#             return f"Гражданин {self.surname} {self.name}"
#
#         else:
#             return f"Гражданка {self.surname} {self.name}"
#
# p1 = Person('Chuck', 'Norris')
# print(p1) # печатает "Гражданин Norris Chuck"
# p2 = Person('Mila', 'Kunis', 'female')
# print(p2) # печатает "Гражданка Kunis Mila"
# p3 = Person('Оби-Ван', 'Кеноби', True)# печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
# print(p3) # печатает "Гражданин Кеноби Оби-Ван"

'''
Создайте класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:

конструктор __init__, принимающий произвольное количество аргументов.
 Среди всех переданных аргументов необходимо оставить только целые числа
  и сохранить их в атрибут values в виде списка;
  
переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом: 
"Вектор(<value1>, <value2>, <value3>, ...)",
 если вектор не пустой. При этом значения должны быть упорядочены
  по возрастанию (будьте аккуратнее с пробелами,
   они стоят только после запятых, см. пример ниже);
   
"Пустой вектор", если наш вектор не хранит в себе значения
'''
class Vector:
    def __init__(self, *args):
        x=args
        self.values=[]
        for value in x:
            if str(value).isnumeric():
                self.values.append(value)
        self.values.sort()


    def __str__(self):
        if len(self.values)==0:
            return('Пустой вектор')
        else:
            return(f"Вектор{tuple(self.values)}")
#
#
v1 = Vector(1,2,3, 4, '4')
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"

