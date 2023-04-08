num1, num2, num3 = 0.0, 0.0, 0.0

num1=float(input('Intropduce valor 1 >'))
num2=float(input('Intropduce valor 2 >'))
num3=float(input('Intropduce valor 3 >'))

if num1 > num2 and num1 > num3:
    print(f'{num1} que es el primer numero, es mayor que los otros dos valores')
elif num2 > num1 and num2 >num3:
    print(f'{num2} que es el segundo numero, es mayor que los otros dos valores')
else:
    print(f'{num3} que es el ultimo numero, es mayor de todos')
