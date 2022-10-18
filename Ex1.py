def multiDigit(array):
    for i in range(len(array)):
        if str(array[i]).isdigit() and str(array[i+1]).isdigit():
            array[i] = int(array[i])*10+int(array[i+1])
            array.pop(i+1)
            return array


def factor(array):
    for i in range(len(array)-1):
        if array[i] == 'f':
            bufer = float(array[i-1])**float(array[i+1])
            array.pop(i+1)
            array.pop(i)
            array[i-1] = bufer
            return array


def mult(array):
    for i in range(len(array)):
        if array[i] == '*' or array[i] == '/':
            if array[i] == '*':
                bufer = float(array[i-1])*float(array[i+1])
                array.pop(i+1)
                array.pop(i)
                array[i-1] = bufer
                return array
            else:
                bufer = float(array[i-1])/float(array[i+1])
                array.pop(i+1)
                array.pop(i)
                array[i-1] = bufer
                return array


def sum(array):
    for i in range(len(array)):
        if array[i] == '+' or array[i] == '-':
            if array[i] == '+':
                bufer = float(array[i-1])+float(array[i+1])
                array.pop(i+1)
                array.pop(i)
                array[i-1] = bufer
                return array
            else:
                bufer = float(array[i-1])-float(array[i+1])
                array.pop(i+1)
                array.pop(i)
                array[i-1] = bufer
                return array


string = (input(
    'Введите выражение из чисел и знаков(символ (f) для возведения в степень):'))
array = []
for char in string:
    array.append(char)
for i in range(len(array)):
    if array[i] == '+' or array[i] == '-' or array[i] == '*' or array[i] == '/' or array[i] == 'f' or array[i].isdigit():
        bool = True
    else:
        bool = False
        break
countMult = 0
countSum = 0
countFactor = 0
for i in range(len(array)):
    if array[i] == 'f':
        countFactor += 1
    if array[i] == '*' or array[i] == '/':
        countMult += 1
    if array[i] == '+' or array[i] == '-':
        countSum += 1
while len(array) > ((countMult+countSum+countFactor)*2+1):
    multiDigit(array)


if bool == True:
    count = 0
    while count < countFactor:
        factor(array)
        count += 1
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
