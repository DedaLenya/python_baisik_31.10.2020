string = input("Введите любую  строку")
i = 0
while i < len(string):
    if string[i:i+2] == "##":
        break
    print(string[i])
    i += 1
else:
    print('Проверено')
