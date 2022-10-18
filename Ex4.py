# Семинар 2 Задание 2
def mult(num):
    sum=1
    for i in range(1,num+1):
        sum*=i
    return sum

num = int(input('Enter N-number:'))
array=[]
for i in range(1,num+1):
    array.append(i)
arrayMult=list(map(mult,array))
print(arrayMult)