
from random import choice


def is_valid_number(innumber):
    if innumber.isdigit() and int(innumber) > 0:
        return int(innumber)
    print('Введено некорректное число!')
    return -1


def configure_charset(symbols):
    while True:
        decision = input(f'Использовать символы {symbols} ? (y / n) ')
        if decision == 'y':
            return True
        elif decision == 'n':
            return False
        else:
            print("Пожалуйста, введите символ 'y' - да или 'n' - нет")


def generate_password(length, chars):
    pword = ''
    if chars != '':
        for _ in range(length):
            pword += choice(chars)
        return pword
    return -1


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
bad_symb = 'il1Lo0O'
chars = ''

print('Добро пожаловать в генератор паролей')

pcount = -1
while pcount < 1:
    pcount = is_valid_number(input('Укажите количество паролей для генерации (натуральное число): '))

plength = -1
while plength < 1:
    plength = is_valid_number(input('Укажите требуемую длину паролей (натуральное число): '))

if configure_charset(digits):
    chars += digits
if configure_charset(lowercase_letters):
    chars += lowercase_letters
if configure_charset(uppercase_letters):
    chars += uppercase_letters
if configure_charset(punctuation):
    chars += punctuation
if not configure_charset(bad_symb):
    for ch in bad_symb:
        chars.replace(ch, '')

print('-' * 10)
for _ in range(pcount):
    password = generate_password(plength, chars)
    if password == -1:
        print('Для генерации пароля выбрано недостаточно символов')
        break
    else:
        print(password)
print('-' * 10)