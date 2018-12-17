# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# Task 1.

import os
import re


def find_our_directories(regime):
    for directories in os.listdir():
        if re.match('^dir_[1-9]$', directories):
            if regime == 'after_creation':
                print(directories)
            elif regime == 'after_deletion':
                print('Ooops... The directory ' + directories + ' is stay alive.')


for count in range(1, 10):
    if os.path.isdir('dir_' + str(count)):
        print('A directory dir_' + str(count) + ' is already exist. Doing nothing.')
    else:
        print('Making a directory dir_{}.'.format(str(count)))
        os.mkdir('dir_' + str(count))
print()

print('Here you can test what we have done.')
find_our_directories('after_creation')
print()

while True:
    if input('Let''s remove previously created directories? [Y/N]: ') == 'Y':
        for count in range(1, 10):
            os.rmdir('dir_' + str(count))
        break
    else:
        print('It was wrong input. Please, try again.')

print()
find_our_directories('after_deletion')
print()

# Task 2.
import os

for filename in os.listdir():
    if os.path.isdir(filename):
        print('This is a directory:', filename)
    else:
        print('This is not a directory, I suppose it\'s a regular file:', filename)
print()

# Task 3.

import os
import sys
import shutil

try:
    shutil.copy(sys.argv[0], os.path.join(os.getcwd(), 'copy_' + os.path.basename(__file__)))
except Exception as error:
    print('There was an error happened during copy:', error)