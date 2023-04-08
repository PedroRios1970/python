num1, num2, num3, num4, num5 = 0.0, 0.0, 0.0, 0.0, 0.0
Resta1, Resta2, Resta3, Resta4 = 0.0, 0.0, 0.0, 0.0

num1 = float(input('Introduce el numero 1 >'))
num2 = float(input('Introduce el numero 2 >'))
num3 = float(input('Introduce el numero 3 >'))
num4 = float(input('Introduce el numero 4 >'))
num5 = float(input('Introduce el numero 5 >'))

Resta1 = num1 - num2
Resta2 = num1 - num3
Resta3 = num1 - num4
Resta4 = num1 - num5

menor_diferencia = Resta1

if Resta2 < menor_diferencia and Resta2 >=0:
    menor_diferencia = Resta2
elif Resta2 > menor_diferencia and Resta2 <=0:
    menor_diferencia = Resta2
elif Resta3 < menor_diferencia and Resta3 >=0:
    menor_diferencia = Resta3
elif Resta3 > menor_diferencia and Resta3 <=0:
    menor_diferencia = Resta3    
elif Resta4 < menor_diferencia and Resta4 >=0:
    menor_diferencia = Resta4
elif Resta4 > menor_diferencia and Resta4 <=0:
    menor_diferencia = Resta4        

numero_cercano = num1 - menor_diferencia

print('El numero mas cercano a %d es %d'%(num1, numero_cercano))