import random

def is_valid(n, x):  # функция проверки правильности ввода числа
    if n.isdigit() and 1 <= int(n) <= int(x):
        return True
    else:
        return False

def is_valid_range(n):  # функция проверки правильности ввода диапазона
    if n.isdigit() and int(n) >= 2:
        return True
    else:
        return False
    
# основная программа
print('Добро пожаловать в числовую угадайку')
while True:
    n = input('Выберите наибольшее число угадайки: ')
    if not is_valid_range(n):
        print('Введите целое число больше 1: ')
        continue
    else:
        num = random.randint(1, int(n))
        count = 1
        while True:
            test = input(f'Угадайте целое число от 1 до {n}: ')
            if not is_valid(test, n):
                print('А может быть все-таки введем целое число от 1 до ', n, '?', sep='')
                continue
            else:
                test = int(test)
                if test < num:
                    count += 1
                    print(f'Число {test} МЕНЬШЕ загаданного, попробуйте еще разок')
                    continue
                elif test > num:
                    count += 1
                    print(f'Число {test} БОЛЬШЕ загаданного, попробуйте еще разок')
                    continue
                else:
                    print('Вы угадали с', count, 'попытки,', 'поздравляем!')
                break

    # продолжение игры либо конец
    new_game = input('Сыграем еще?(д = да, н = нет) ')
    if new_game.lower() == 'н':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break
    else:
        continue