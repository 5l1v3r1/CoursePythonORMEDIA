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
