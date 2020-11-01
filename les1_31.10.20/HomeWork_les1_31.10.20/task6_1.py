"""
6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить
не менее b километров. Программа должна принимать значения параметров a и b и выводить
одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
"""

a = int(input("Результат за день в км>>"))
b = int(input("Результат ожидаемый в км>>"))
d = 0
while a*0.9 <= b:
    d += 1
    print(d, "-й день:", round(a, 2))
    a = a * 1.1
print("На", d, "-й день ты достигнешь нужного результата")
