
'''
Работа с файловой системой. Знакомство с модулем os и os.path
 - практическое понимание базовый работы с файловой системой (получение пути до файлa, создание, удаление директории,
  получение списков файлов, методы isfile/isdir и т.д.). Атрибут __file__.
  Более глубокое понимание класса Path из модуля pathlib - методы работы с данным классом.
'''

import os
import os.path
import requests

# print(os.path.abspath('test'))
# print(os.path.isfile(os.path.abspath('os_path.py')))
# print(os.path.isdir(os.path.abspath('os_path')))


# print(os.listdir(path="."))
def create_dir():
    try:
        name_dir = input('Введите название дериктории:')
        os.mkdir(name_dir)
        os.chdir(name_dir)
        x=open('test.txt', 'w')
        list = [i for i in range(500)]
        for i in list:
            x.write(str(i))

        x.close()
        old_file = open('test.txt', 'r')
        file = open('bin_test.txt', 'w')
        old_file=old_file.read()
        bin_list=bin(int(old_file))
        file.write(bin_list)
        file.close()

    except FileExistsError:
        print('папка уже существует')
    finally:
        print('Папка с файлами успешно созданы')


def del_dir():
    name_dir = input('Введите название дериктории:')
    try:
        try:
            os.rmdir(name_dir)
        except OSError:
            os.chdir(name_dir)
            del_files=os.listdir(path=".")
            x =input(f'Папка содержит в себе:{del_files}.\nхотете удалить имеющиеся файлы?\n:')
            match x:
                case "y"|"Y":
                    for file in del_files:
                        print(f'{file} удален')
                        os.remove(file)
                    os.chdir('..')
                    os.rmdir(name_dir)
                    print('Папка и все ее содержимое удалено')
                case _:
                    print('Ничего не делаем')

    except FileNotFoundError:
        print(f'папка с именем"{name_dir}" не найдена')


question = input("1 - создать папку с тестовым файлом\n2 - Удалить папку и ее содержимое\nВыберите вариант:")
match question:
    case '1':
        create_dir()
    case '2':
        del_dir()
    case _:
        print('вы указали неверное значение')
