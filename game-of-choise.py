from random import *

num = randint(1, 100)


def is_valid(number):
    if number.isdigit():
        if int(number) in range(1, 101):
            return True
    else:
        return False


print('Добро пожаловать в числовую угадайку')

while True:
    guess = input('Enter your guess: ')
    print(is_valid(guess))
    if not is_valid(guess):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    else:
        guess = int(guess)
        if guess > num:
            print('Слишком много, попробуйте еще раз')
        elif guess < num:
            print('Слишком мало, попробуйте еще раз')
        else:
            print('Вы угадали, поздравляем!')
            break
