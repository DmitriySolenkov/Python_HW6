# Семинар 2 Задание 1
num = int(input('Enter N-number:')) 
mult=lambda x: 3*x+1
if num >= 1:
    dictionary = {a: mult(a) for a in range(1, num+1)}
    print(dictionary)
else:
    print('Incorrect number!')