import datetime


def one():
    start=datetime.datetime.now()
    x = [i for i in range(10000000)]
    fin=datetime.datetime.now()
    print(fin-start)

def two():
    start = datetime.datetime.now()
    x = []
    for i in range(10000000):
        x.append(i)
    fin = datetime.datetime.now()
    print(fin - start)

one()
two()
# чем длиннее список тем больше разница в скорости генератора относительно цикла