# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Целое положительное >>'))
r = -1
while number > 10:
    d = number % 10
    number //= 10
    if d > r:
        r = d
print(r)
