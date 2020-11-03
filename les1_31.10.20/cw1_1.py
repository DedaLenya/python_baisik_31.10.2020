# print('*'*40)
# a = float(input('Please inter a: '))
# b = float(input('Please inter b: '))
#
# day = 1
# print(f'{day} day - {a:.2f}')
# while a < b:
#     day += 1
#     a *= 1.1  # short version of a = a + a*0.1
#     print(f'{day} day - {a:.2f}')
#
# print('Answer is:', day)

a = int(input("Результат за день в км>>"))
b = int(input("Результат ожидаемый в км>>"))
d = 1
print(d, "-й день:", round(a, 2))
while a < b:
    d += 1
    a *= 1.1
    print(d, "-й день:", round(a, 2))
print("На", d, "-й день ты достигнешь нужного результата")