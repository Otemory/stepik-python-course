#   импортируем библиотеки
from random import randint


#   Назначаем функции
#   проверка Ответа на да нет


def yes_no(text):
    if text.lower() == 'да':
        return True
    elif text.lower() == 'нет':
        return print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    else:
        return yes_no(input('Не понял ваш ответ. попробуйте еще раз да/нет '))


#   Проверка границы на число
def is_valid(num):
    if num.isdigit():
        if int(num) >= 10:
            return int(num)
        else:
            return is_valid(input('А может быть все-таки введем целое число от 10? '))
    else:
        return is_valid(input('А может быть все-таки введем целое число от 10? '))


#   Проверка числа на число и в границах ли
def is_valid_2(num, amount):
    if num.isdigit():
        if int(num) in range(1, amount + 1):
            return int(num)
        else:
            return is_valid_2(input(f'А может быть все-таки введем целое число от 1 до {amount}? '), amount)
    else:
        return is_valid_2(input(f'А может быть все-таки введем целое число от 1 до {amount}? '), amount)


#    Игра
def game():
    game_number = randint(1, amount)
    cnt = 1
    while True:
        guess = is_valid_2(input(f'Введите число от одного до {amount} '), amount)
        if guess > game_number:
            print('Слишком много, попробуйте еще раз ')
            cnt += 1
        elif guess < game_number:
            print('Слишком мало, попробуйте еще раз ')
            cnt += 1
        else:
            print(f'Вы угадали c {cnt} попытки, поздравляем!')
            break



#    Приветствие
print('Добро пожаловать в числовую угадайку')

#    Хотите сыграть
answer = yes_no(input('Хотите сыграть? да/нет '))
#    Начинаем игру
while answer:
    amount = is_valid(input('Ведите число от 10, иначе совсем не интересно: '))
    game()
    answer = yes_no(input('Хотите сыграть еще? да/нет '))





