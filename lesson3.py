import random


start = input('Вы запустили игру "Камень, ножницы, бумага". Хотите поиграть? (Вводите + или -): ')

if start == '+':
    print('Если захотите закончить вводите "-".')
    print('Если захотите узнать счёт вводите "с".')
    user_ball = 0
    rand_ball = 0
    while True:
        user = input("Камень, ножницы или бумага? (Вводите к, н или б): ")
        list_play = ['к', 'н', 'б']
        if user in list_play:
            rand = random.choice(list_play)
            print(rand)

            if rand == 'Камень' and user == 'ножницы':
                rand_ball += 1
            if rand == 'Камень' and user == 'бумага':
                user_ball += 1
            if rand == 'ножницы' and user == 'Камень':
                user_ball += 1
            if rand == 'ножницы' and user == 'б':
                rand_ball += 1
            if rand == 'бумага' and user == 'ножницы':
                user_ball += 1
            if rand == 'бумага' and user == 'Камень':
                rand_ball += 1
        elif user == 'с':
            print('Ваши баллы - ', user_ball, '. Баллы вашего соперника - ', rand_ball, ".")
        elif user == '-':
            print('Ваши баллы - ', user_ball, '. Баллы вашего соперника - ', rand_ball, ".")
            print('Конец игры! Заходите ещё!')
            break
        else:
            print('Вводите к, н или б')


if start == '-':
    print('Жаль... :(')
else:
    print('Простите, я вас не понял, если хотите играть перезапустите программу и введите "+". Спасибо!')




























