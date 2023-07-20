import random

def rock_paper_scissors(number_wins):                      #Камень, Ножницы, Бумага
    wins_user = 0
    wins_PC = 0
    
    while True:
        if (wins_user < number_wins) and (wins_PC < number_wins): # Условие входа при котором игра продолжается
            action_computer = random.randint(1, 3) # Генерируется число от 1 до 3, границы включая
            if action_computer == 1: # Происходит присвоения имен к генерируемым числам, для того чтобы лучше отображать в терминале что было выбрано компьютером
                combination = 'камень'
            elif action_computer == 2:
                combination = 'ножницы'
            else:
                combination = 'бумага'

            action = int(input('1 - Камень, 2 - Ножницы, 3 - Бумага: ')) # Пользователь вводит свое число

            if action_computer == action: # В этом условие проверяется, кто победил в раунде
                print('\nНичья. У противника тоже', combination)
                print(f'Количество побед: Компьютер = {wins_PC}  Пользователь = {wins_user}\n')
            elif (action == 1 and action_computer == 2) or (action == 2 and action_computer == 3) or (action == 3 and action_computer == 1):
                print('\nТы победил! У противника', combination)
                wins_user += 1
                print(f'Количество побед: Компьютер = {wins_PC}  Пользователь = {wins_user}\n')
            else:
                print('\nТы проиграл! У противника', combination)
                wins_PC += 1
                print(f'Количество побед: Компьютер = {wins_PC}  Пользователь = {wins_user}\n')

        elif wins_user == number_wins: # Игра заканчивается, если пользователь выйграл нужное количество раундов в игре
            print(f'\nТы победил в игре! Компьютер = {wins_PC}  Пользователь = {wins_user}\n')
            break
        else:  # Игра заканчивается, если компьютер выйграл нужное количество раундов в игре
            print(f'\nКомпьютер победил в игре! Компьютер = {wins_PC}  Пользователь = {wins_user}\n')
            break

def guess_the_number():                         #Угадай число
    hidden_number =  random.randint(1, 100)  # Компьютер генерирует число, которое нужно будет угадать
    attempt = 7 # Количество попыток, для того чтобы отгадать число
    while attempt > 0:
        estimated_number = int(input('Введите предполагаемое число от 1 до 100: '))
        attempt -= 1
        if hidden_number > estimated_number: # Условие на проверку числа которое ввел пользователь и число которое сгенерировал компьютер
            print('Загаданное число больше, чем ваше. \nОсталось попыток:', attempt)
            print()
            continue
        elif hidden_number < estimated_number:
            print('Загаданное число меньше, чем ваше. \nОсталось попыток:', attempt)
            print()
            continue
        elif hidden_number == estimated_number:
            print('Вы угадали загаданное число. Оно равно', hidden_number)
            break
    else:
        print('Попытки закончились! Компьютер загадал', hidden_number)
    

def mainMenu():
    perform = int(input('Выберите игру (1 - камень, ножницы, бумага; 2 - Угадай число): '))
    if perform == 1:
        number_wins = int(input('Введите до скольки побед будет игра: '))
        rock_paper_scissors(number_wins)
    elif perform == 2:
        guess_the_number()
    else:
        print('Ошибка ввода. Введите 1 или 2')
        mainMenu()

mainMenu()
