'''

с другим вектором такой же длины. В результате должен получиться новый Vector, состоящий из суммы элементов, расположенных на одинаковых местах. Если длины векторов различаются, выведите сообщение "Сложение векторов разной длины недопустимо";
В случае, если вектор складывается с другим типом(не числом и не вектором), нужны вывести сообщение "Вектор нельзя сложить с <значением>"
'''
class Vector:
    def __init__(self, *args):
        x=args
        self.values=[]
        for value in x:
            if isinstance(value, int):
                self.values.append(value)
        self.values.sort()


        # self.values = sorted(args)

    def __str__(self):
        if len(self.values)>0:
            return(f"Вектор{tuple(self.values)}")
        return "Пустой вектор"

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*[i + other for i in self.values])

        elif isinstance(other, Vector):
            if len(self.values)==len(other.values):
                return Vector(*[sum(i) for i in zip(self.values, other.values)])
            else:
                return "Сложение векторов разной длины недопустимо"

        else:
            print (f"Вектор нельзя сложить с {other}")

    def __mul__ (self, other):
        if isinstance(other, int):
            return Vector(*[i*other for i in self.values])
        elif isinstance(other, Vector):
            if len(self.values)==len(other.values):
                return Vector(*[i[0]*i[1] for i in zip(self.values, other.values)])
            else:
                return "Умножение векторов разной длины недопустимо"
        else:
            print ( f"Вектор нельзя умножать с {other}")


v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"

v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"
