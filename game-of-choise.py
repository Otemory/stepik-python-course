from random import *

num = randint(1, 100)


def is_valid(number):
    if number.isdigit():
        if int(number) in range(1, 101):
            return True
    else:
        return False


print('Добро пожаловать в числовую угадайку')
cnt = 0
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
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')