'''











'''

#    Создайте класс Robot, у которого есть:
class Robot:

# атрибут класса population. В этом атрибуте будет хранится общее количество роботов,
#  изначально принимает значение 0;
    population = 0


# конструктор __init__, принимающий 1 аргумент name.
#  Данный метод должен сохранять атрибут name и печатать сообщение
#  вида "Робот <name> был создан". Помимо инициализации робота
#  данный метод должен увеличивать популяцию роботов на единицу;
    def __init__(self, name):
        self.name=name
        Robot.population+=1
        print(f"Робот {self.name} был создан")


# метод destroy, должен уменьшать популяцию роботов на единицу и печатать сообщение вида
# "Робот <name> был уничтожен"
    def destroy(self):
        Robot.population-=1
        print(f"Робот {self.name} был уничтожен")

    # метод say_hello, которой печатает сообщение вида "Робот <name> приветствует тебя,
#  особь человеческого рода"
    def say_hello(self):
        print(f"Робот {self.name} приветствует тебя, особь человеческого рода")

    # метод класса  how_many, который печатает сообщение вида "<population>, вот сколько нас еще осталось"
    @classmethod
    def how_many(self):
        print(f"{Robot.population}, вот сколько нас еще осталось")




r2 = Robot("R2-D2") # печатает "Робот R2-D2 был создан"
r2.say_hello() # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
Robot.how_many() # печатает "1, вот сколько нас еще осталось"
r2.destroy() # печатает "Робот R2-D2 был уничтожен"
p3 = Robot("P3-PiO") # печатает "Робот R2-D2 был создан"
Robot.how_many()