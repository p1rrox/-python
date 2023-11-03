import random
from random import randint, choice
import sys
x = input('Выбери игру:Решение задач,Калькулятор, Орел или Решка. Для просмотра статистики в игра Решение задач напишите 4.Для выбора во что играть нужно выбрать 1,2,3.Решение задач(1) Калькулятор(2) Орел или Решка(3)\n')
y = '1'
z = '2'
c = '3'
v = '4'
win = 0
lose = 0
if x == y:  #Решение задач
    Choose_an_action = input('Выберете действие + - * /\n')
    plus = "+"
    minus = "-"
    multiplication = "*"
    division = '/'
    right_Problem_solving = 0
    wrong_Problem_solving = 0

    number = randint(1, 1000)
    number2 = randint(1, 1000)
    if Choose_an_action == plus:#Сложение

        amount = number + number2
        print(number,'+', number2) 
        Enter_the_amount = int(input('Введите сумму\n'))

        if Enter_the_amount == amount:#Сложение правильно
            
            print('Все правильно! Молодец!!!')
            with open('Статистика.txt', 'r') as file:
                right_Problem_solving = int(file.readline())
                wrong_Problem_solving = int(file.readline())

                right_Problem_solving += 1
                
            with open('Статистика.txt', 'w') as file:
                file.write(str((right_Problem_solving)))
                file.write(str('\n'))
                file.write(str(wrong_Problem_solving))  
        elif Enter_the_amount < amount:#Сложение не правильно
            print('Неправильно попробуй снова()')
            with open('Статистика.txt', 'r') as file:
                right_Problem_solving = int(file.readline())
                wrong_Problem_solving = int(file.readline())

                wrong_Problem_solving += 1
                
            with open('Статистика.txt', 'w') as file:
                file.write(str((right_Problem_solving)))
                file.write(str('\n'))
                file.write(str(wrong_Problem_solving))  
        elif Enter_the_amount > amount:#Сложение не правильно 
            print('Неправильно попробуй снова( ')
            with open('Статистика.txt', 'r') as file:
                right_Problem_solving = int(file.readline())
                wrong_Problem_solving = int(file.readline())

                wrong_Problem_solving += 1
                
            with open('Статистика.txt', 'w') as file:
                file.write(str((right_Problem_solving)))
                file.write(str('\n'))
                file.write(str(wrong_Problem_solving))  
    elif Choose_an_action == minus:#Отнимание 
        difference = number - number2
        print(number,'-', number2) 
        Enter_the_difference = int(input('Введите разность\n'))

        if difference == Enter_the_difference:#Отнимание правильно
            with open('Статистика.txt', 'r') as file:
                right_Problem_solving = int(file.readline())
                wrong_Problem_solving = int(file.readline())

                right_Problem_solving += 1
                
            with open('Статистика.txt', 'w') as file:
                file.write(str((right_Problem_solving)))
                file.write(str('\n'))
                file.write(str(wrong_Problem_solving))  
            print('Все правильно!!!!')
        elif difference < Enter_the_difference:#Отнимание не правильно
            with open('Статистика.txt', 'r') as file:
                right_Problem_solving = int(file.readline())
                wrong_Problem_solving = int(file.readline())

                wrong_Problem_solving += 1
            with open('Статистика.txt', 'w') as file:
                file.write(str((right_Problem_solving)))
                file.write(str('\n'))
                file.write(str(wrong_Problem_solving))  
            print('Неправильно попробуй снова(')
        elif difference > Enter_the_difference:#Отнимание не правильно
            with open('Статистика.txt', 'r') as file:
                    right_Problem_solving = int(file.readline())
                    wrong_Problem_solving = int(file.readline())

                    wrong_Problem_solving += 1
                    
            with open('Статистика.txt', 'w') as file:
                    file.write(str((right_Problem_solving)))
                    file.write(str('\n'))
                    file.write(str(wrong_Problem_solving))  
            print('Неправильно попробуй снова( ')
    if Choose_an_action == multiplication:#Умножение

        Composition = number * number2
        print(number,'*', number2) 
        Enter_the_Composition = int(input('Введите разность\n'))
        if Composition == Enter_the_Composition:#Умножение правильно
                with open('Статистика.txt', 'r') as file:
                    right_Problem_solving = int(file.readline())
                    wrong_Problem_solving = int(file.readline())

                    right_Problem_solving += 1
                    
                with open('Статистика.txt', 'w') as file:
                    file.write(str((right_Problem_solving)))
                    file.write(str('\n'))
                    file.write(str(wrong_Problem_solving))  
                print('Все правильно! А ты не плохо справляешься) ')
        elif Composition < Enter_the_Composition:#Умножение не правильно
                with open('Статистика.txt', 'r') as file:
                    right_Problem_solving = int(file.readline())
                    wrong_Problem_solving = int(file.readline())

                    wrong_Problem_solving += 1
                    
                with open('Статистика.txt', 'w') as file:
                    file.write(str((right_Problem_solving)))
                    file.write(str('\n'))
                    file.write(str(wrong_Problem_solving))  
                print('Неправильно попробуй снова(')
        elif Composition > Enter_the_Composition:#Умножение не правильно
            with open('Статистика.txt', 'r') as file:
                right_Problem_solving = int(file.readline())
                wrong_Problem_solving = int(file.readline())

                wrong_Problem_solving += 1               
            with open('Статистика.txt', 'w') as file:
                file.write(str((right_Problem_solving)))
                file.write(str('\n'))
                file.write(str(wrong_Problem_solving))  
            print('Неправильно попробуй снова( ')     
    if Choose_an_action == division:#Деление
        number3 = randint(1, 100)
        number4 = randint(1, 100)
        private = number3 / number4
        print(number3,'/', number4)
        Enter_a_private = float(input('Введите частное\n'))
        if private == Enter_a_private:#Деление правильно
            with open('Статистика.txt', 'r') as file:
                right_Problem_solving = int(file.readline())
                wrong_Problem_solving = int(file.readline())

                right_Problem_solving += 1
                
            with open('Статистика.txt', 'w') as file:
                file.write(str((right_Problem_solving)))
                file.write(str('\n'))
                file.write(str(wrong_Problem_solving))  
            print('Все правильно! МОЛОДЕЦ!!!')
        elif private < Enter_a_private:#Деление не правильно
            with open('Статистика.txt', 'r') as file:
                right_Problem_solving = int(file.readline())
                wrong_Problem_solving = int(file.readline())

                wrong_Problem_solving += 1
                
            with open('Статистика.txt', 'w') as file:
                file.write(str((right_Problem_solving)))
                file.write(str('\n'))
                file.write(str(wrong_Problem_solving))  
            print('Неправильно попробуй снова()')
        elif private > Enter_a_private:#Деление не правильно
            with open('Статистика.txt', 'r') as file:
                right_Problem_solving = int(file.readline())
                wrong_Problem_solving = int(file.readline())

                wrong_Problem_solving += 1
                
            with open('Статистика.txt', 'w') as file:
                file.write(str((right_Problem_solving)))
                file.write(str('\n'))
                file.write(str(wrong_Problem_solving))  
            print("Неправльно пропробуй снова(")
elif x == z:#Калькулятор
    Choose_an_action2 = input('Ввыберете действие +, -, *, /:\n')
    plus2 = '+'
    minus2 = '-'
    multiplication2 = "*"
    division2 = '/'
    
    if Choose_an_action2 == plus2:
        number5 = int(input('Введите первое число:\n'))
        number6 = int(input('Введите второе число:\n'))
        amount2 = number5 + number6 
        print(amount2, 'Спасибо за такой сложный пример')
    elif Choose_an_action2 == minus2:
        number7 = int(input('Введите первое число:\n'))
        number8 = int(input('Введите второе число:\n'))
        amount3 = number7 - number8 
        print(amount3, 'Спасибо за такой сложный пример')
    elif Choose_an_action2 == multiplication2:
        number9 = int(input('Введите первое число:\n'))
        number10 = int(input('Введите второе число:\n'))
        amount4 = number9 * number10
        print(amount4, 'Спасибо за такойсложный пример')
    elif Choose_an_action2 == division2:
        number11 = int(input('Введите первое число:\n'))
        number12 = int(input('Введите второе число:\n'))
        amount5 = number11 / number12
        print(amount5, 'Спасибо за такой сложный пример')
while x == c:#Орел и Решка
    
        p = int(input('Введите орел или решка. Орел = 1,Решка = 2.Напишите 3 чтобы узнать статистик 4 чтобы закончить игру:\n'))
        coin = randint(1,2)
        if p == 4:
            print('Спасибо что ты играл в мою игру)')
            break
        if p == 3:
            print('Выграл:',win)
            print('Проиграл:',lose)
        elif coin == p:
            win += 1
            print('Ты выграл! Молодец')
        elif coin < p:
            lose += 1
            print('Ты проиграл( Повезет в следуший раз')
        elif coin > p:
            lose += 1
            print('Ты проиграл( Повезет в следуший раз')
if x == v:#Статистика Решение задач
    def statistics():
        with open('Статистика.txt', 'r') as file:
                    right_Problem_solving = int(file.readline())
                    wrong_Problem_solving = int(file.readline())
                    print('Побед:',right_Problem_solving)
                    print('Поражений:', wrong_Problem_solving)
    statistics()
