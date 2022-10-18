def mult(array):
    for i in range(len(array)):
        if array[i] == '*' or array[i] == '/':
            if array[i] == '*':
                bufer = int(array[i-1])*int(array[i+1])
                array.pop(i+1)
                array.pop(i)
                array[i-1] = bufer
                return array
            else:
                bufer = int(array[i-1])/int(array[i+1])
                array.pop(i+1)
                array.pop(i)
                array[i-1] = bufer
                return array


def sum(array):
    for i in range(len(array)):
        if array[i] == '+' or array[i] == '-':
            if array[i] == '+':
                bufer = int(array[i-1])+int(array[i+1])
                array.pop(i+1)
                array.pop(i)
                array[i-1] = bufer
                return array
            else:
                bufer = int(array[i-1])-int(array[i+1])
                array.pop(i+1)
                array.pop(i)
                array[i-1] = bufer
                return array


string = (input('Введите выражение из однозначных чисел и знаков:'))
array = []
for char in string:
    array.append(char)
for i in range(len(array)):
    if array[i] == '+' or array[i] == '-' or array[i] == '*' or array[i] == '/' or array[i].isdigit():
        bool = True
    else:
        bool = False
        break
countMult = 0
countSum = 0
for i in range(len(array)):
    if array[i] == '*' or array[i] == '/':
        countMult += 1
    if array[i] == '+' or array[i] == '-':
        countSum += 1


if bool == True:
    count = 0
    while count < countMult:
        mult(array)
        count += 1
    count = 0
    while count < countSum:
        sum(array)
        count += 1

    print(f'Решение выражения:{array[0]}')
else:
    print('Проверьте правильность введения!')
