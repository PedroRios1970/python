# Formato While

num = 0

num = int(input('Introduce un numero >'))

result = 0,0
Finish = 10
Start = 1

print('Con While')

while Start <= Finish:
    result = num * Start
    print (f'El {num} x el {Start} es igual a {result}')
    Start = Start + 1

# Formato For Ranger

print ('Con For')


for res in range(1,11):
    result = num * res
    print (f'El {num} x el {res} es igual a {result}')
