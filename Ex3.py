num = int(input('Enter N-number:'))
sum=0
lamb=lambda x: (1+(1/x))**x
if num>=1:
    for i in range(1,num+1):
        sum+=lamb(i)
    print(round(sum,2))
else:
    print('Incorrect number!')