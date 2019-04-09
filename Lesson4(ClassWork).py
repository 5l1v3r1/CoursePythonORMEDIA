print("-------------------------------------------- Цикл FOR")

for i in range(1, 10):
    print(i, end=' ')
print()

print("-------------------------------------------- Цикл WHILE (c ПРЕДусловием)")

i = 1
while i < 10:
    print(i, end=' ')
    i += 1
print()

print("-------------------------------------------- Цикл WHILE (с ПОСТусловием)")

i = 1
while True:
    print(i, end=' ')
    i += 1
    if i >= 10:
        break
print()

print("-------------------------------------------- Условный оператор IF-ELIF-ELSE")

count = 10
if count < 0:
    print("Число меньше нуля")
elif count > 0:
    print("Число больше нуля!")
else:
    print("Равно нулю!")

print("-------------------------------------------- Игра угадай число от 1 до 20 (5 попыток) ")

import random

number = random.randint(1, 20)  # Рандом от 1 до 20
guesses = 0
while guesses < 5:
    print('Напишите число от 1 до 20: ')
    guess = int(input())
    guesses += 1
    if guess == number:
        print('Успех!')
    if guess < number:
        print('Число слишком маленькое. Попробуй еще.')
    if guess > number:
        print('Число слишком большое. Попробуй еще.')
    if guesses == 5:
        print('Ты не угадал число. Исходное число: ' + str(number))
    if guess == number:
        print('Вы угадали число. ' + str(guesses))
        break