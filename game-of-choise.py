from random import *


def is_valid(number):
    if number.isdigit():
        if int(number) in range(1, 101):
            return True
    else:
        return False


def is_valid2(number):
    if number.isdigit():
        if int(number) >= 10:
            return True
    else:
        return False


print('Добро пожаловать в числовую угадайку')
answer = input('Хотите сыграть? да/нет ')
while answer.lower() == 'да':
    n = input('Ведите число от 10, иначе совсем не интересно: ')
    if not is_valid2(n):
        print('А может быть все-таки введем целое число от 10?')
        continue
    else:
        n = int(n)
        num = randint(1, n)

    cnt = 1
    while True:
        guess = input('Ведите число от 1 до 100: ')

        if not is_valid(guess):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        else:
            guess = int(guess)
            if guess > num:
                print('Слишком много, попробуйте еще раз')
                cnt += 1
            elif guess < num:
                print('Слишком мало, попробуйте еще раз')
                cnt += 1
            else:
                print(f'Вы угадали c {cnt} попытки, поздравляем!')
                break
    answer = input('Хотите сыграть еще? да/нет ')
else:
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
