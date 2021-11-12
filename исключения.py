
ints = []
try:
    for i in range(10):
        ints.append(i)
    for i in ints:
        print(ints[i+1])
except ValueError:
    print('Это не число. Выходим.')
except Exception:
    print('Это что ещё такое?')
else:
     print('Всё хорошо.')
finally:
    print('Конец')
    # Именно в таком порядке: try, группа except, затем else, и только потом finally.

