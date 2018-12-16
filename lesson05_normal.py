# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import lesson05_easy

path_to_current_directory = os.getcwd()
continue_or_no = 'Y'
while continue_or_no == 'Y':
    print('This is an utility that allow follow:')
    print('1. Change current directory to defined.')
    print('2. Show contain of current directory.')
    print('3. Delete a folder in current directory.')
    print('4. Create a floler in current directory')
    print()

    while True:
        try:
            choise_is = int(input('Please, enter your choice: '))
        except Exception as error:
            print('That was a bad choice. Try again buddy.')
        else:
            break

    if choise_is == 1:
        while True:
            target_directory = input('Please, enter a path to target directory: ')
            if target_directory == '':
                print('The target directory is not changed, it\'s follow:', path_to_current_directory)
                break
            elif easy.is_directory_exist(target_directory):
                path_to_current_directory = target_directory
                print('The target directory now is:', path_to_current_directory)
                break
            else:
                print('You have entered wrong target directory, try again or press \'Enter\' button.')
    elif choise_is == 2:
        print('Here is a list of current directory')
        for current_directory_item in os.listdir(path_to_current_directory):
            print(current_directory_item)
    elif choise_is == 3:
        while True:
            folder_to_delete = input('Please, in current directory, enter a folder name, you would like to delete: ')
            if folder_to_delete == '':
                continue
            else:
                print('You would like to delete folder: ', folder_to_delete)
                full_path_to_folder_to_delete = os.path.join(path_to_current_directory, folder_to_delete)
                if easy.is_directory_exist(full_path_to_folder_to_delete):
                    print('Ok, I see the directory \'{}\' is exist, let\'s try to delete it.'.format(
                        full_path_to_folder_to_delete))
                    easy.directory_remove(full_path_to_folder_to_delete)
                break
    elif choise_is == 4:
        while True:
            folder_to_create = input('Please, in current directory, enter a folder name, you would like to create: ')
            if folder_to_create == '':
                continue
            else:
                print('You would like to create the folder: ', folder_to_create)
                full_path_to_folder_to_create = os.path.join(path_to_current_directory, folder_to_create)
                print('Ok, let\'s try to create the folder \'{}\'.'.format(full_path_to_folder_to_create))
                easy.directory_create(full_path_to_folder_to_create)
                break
    try:
        continue_or_no = input('Would you like to continue work with this utility [Y/N]: ')
    except Exception:
        print('You didn\'t enter \'Y\', so I suppose you want to exit. You\'ve got it.')
    else:
        if continue_or_no != 'N':
            print('I see you wish not to continue. Bye, bye fella.')