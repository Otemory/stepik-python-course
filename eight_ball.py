from random import randint, choice
from time import sleep

answers = {1: 'Бесспорно',
           2: 'Предрешено',
           3: 'Никаких сомнений',
           4: 'Определённо да',
           5: 'Можешь быть уверен в этом',
           6: 'Мне кажется - да',
           7: 'Вероятнее всего',
           8: 'Хорошие перспективы',
           9: 'Знаки говорят - да',
           10: 'Да',
           11: 'Пока неясно, попробуй снова',
           12: 'Спроси позже',
           13: 'Лучше не рассказывать',
           14: 'Сейчас нельзя предсказать',
           15: 'Сконцентрируйся и спроси опять',
           16: 'Даже не думай',
           17: 'Мой ответ - нет',
           18: 'По моим данным - нет',
           19: 'Перспективы не очень хорошие',
           20: 'Весьма сомнительно'}

print('Привет, я магический шар, и я знаю ответ на любой твой вопрос.')
print(f'Привет, {input("Давай накомится. Как тебя зовут ")}!')

while True:
    input('Задай свой вопрос ')
    sleep(1)
    print('Сейчас подумаем')
    sleep(3)
    print(choice(answers))
    sleep(1)
    if input('Еще вопросы? да/нет ') == 'да':
        continue
    else:
        print('Возвращайся если возникнут вопросы!')
        break



