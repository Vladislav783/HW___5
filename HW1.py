#1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_text = open('test.txt', 'w')
line = input('Введите текст: \n' + " ")
while line:
    my_text.writelines(line)
    line = input('Введите текст:  \n' + " ")
    if not line:
        break

my_text.close()
my_text = open('test.txt', 'r')
content = my_text.readlines()
print(f'{content}')
my_text.close()

#пытаюсь понять как намутить пробел между line
