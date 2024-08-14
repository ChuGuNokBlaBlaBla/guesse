from random import randint

number = randint(1, 10)
print('Угадайте число от 1 до 100')
while True:
    text = int(input('Ввведите число:'))

    if text > number:
        print('Ваше число больше загаданного')
    if text < number:
        print('Ваше число меньше загаданного')   
    if text == number:
        break
print('Вы победили! У вас прекрасная интуиция!')    