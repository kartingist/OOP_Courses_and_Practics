'''
# random.seed([X], version=2) - инициализация генератора случайных чисел. Если X не указан, используется системное время.
# random.getstate() - внутреннее состояние генератора.
# random.setstate(state) - восстанавливает внутреннее состояние генератора. Параметр state должен быть получен функцией getstate().
# random.getrandbits(N) - возвращает N случайных бит.
# random.randrange(start, stop, step) - возвращает случайно выбранное число из последовательности.
# random.randint(A, B) - случайное целое число N, A ≤ N ≤ B.
# random.choice(sequence) - случайный элемент непустой последовательности.
# random.shuffle(sequence, [rand]) - перемешивает последовательность (изменяется сама последовательность).
# Поэтому функция не работает для неизменяемых объектов.

# random.sample(population, k) - список длиной k из последовательности population.
# random.random() - случайное число от 0 до 1.
# random.uniform(A, B) - случайное число с плавающей точкой, A ≤ N ≤ B (или B ≤ N ≤ A).
# random.triangular(low, high, mode) - случайное число с плавающей точкой, low ≤ N ≤ high. Mode - распределение.
# random.betavariate(alpha, beta) - бета-распределение. alpha>0, beta>0. Возвращает от 0 до 1.
# random.expovariate(lambd) - экспоненциальное распределение. lambd равен 1/среднее желаемое. Lambd должен быть отличным от нуля.
# Возвращаемые значения от 0 до плюс бесконечности, если lambd положительно, и от минус бесконечности до 0, если lambd отрицательный.

# random.gammavariate(alpha, beta) - гамма-распределение. Условия на параметры alpha>0 и beta>0.
# random.gauss(значение, стандартное отклонение) - распределение Гаусса.
# random.lognormvariate(mu, sigma) - логарифм нормального распределения. Если взять натуральный логарифм этого распределения,
# то вы получите нормальное распределение со средним mu и стандартным отклонением sigma.
# mu может иметь любое значение, и sigma должна быть больше нуля.

# random.normalvariate(mu, sigma) - нормальное распределение. mu - среднее значение, sigma - стандартное отклонение.
# random.vonmisesvariate(mu, kappa) - mu - средний угол, выраженный в радианах от 0 до 2π, и kappa - параметр концентрации,
# который должен быть больше или равен нулю. Если каппа равна нулю, это распределение сводится к случайному углу в диапазоне от 0 до 2π.

# random.paretovariate(alpha) - распределение Парето.
# random.weibullvariate(alpha, beta) - распределение Вейбулла.
'''

import random

x=True

while x==True:

    class bones():
        def __init__(self, name):
            self.x = random.randint(1, 6)
            self.y = random.randint(1, 6)
            self.z=self.x+self.y
            self.name = name

            print(f'У игрока по имени {self.name} выпали числа {self.x} и {self.y}')

        def __eq__(self, other):
            if isinstance(other, int):
                if self.z==other:
                    print(f"Сумма на костях равна {other}")
                else:
                    print(f"Сумма на костях не равна {other}")
            elif isinstance(other, bones):
                if self.z==other.z:
                    print(f"У игроков ничья")

                else:
                    if self.z>other.z:
                            print(f"Победил {self.name}")

                    else:
                        print(f"Победил {other.name}")

            else: print('невозможно сравнить')


    p1=bones('Игрок 1')
    p2=bones('Игрок 2')
    p1==p2
    if input()=='q':
        x=False




