from random import *
num = randint(1, 100)
while True:
    guess = int(input('Enter your guess: '))
    if guess > num:
        print('Слишком много, попробуйте еще раз')
    elif guess < num:
        print('Слишком мало, попробуйте еще раз')
    else:
        print('Вы угадали, поздравляем!')
        break