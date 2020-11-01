"""
print('Здесь будет основной урок')

# цикл WHILE
cnt = 0
while cnt < 10:
    print(cnt)
    #cnt = cnt + 1
    cnt +=1

print('цикл закончен')
"""

"""
i = 0
while i <= 20:
    i = i + 1
    x = i % 2
    if x == 0:
        print(i)
"""
"""

i = 33
while i >= 11:
    i = i - 1
    x = i % 2
    if x != 0:
        print(i)
"""

"""
string = 'АБ#ВГ'
i = 0
while i < len(string):
    symbol = string[i]
    i = i + 1
    if symbol == '#': # пропустит данную иетерацию
        continue
    print(symbol)
"""

string = input("Введите любую строку")
i = 0
while i < len(string):
    if string[i:i+2] == "##":
        break
    print(string[i])
    i += 1
else:
    print('Проверено')
