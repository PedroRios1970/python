import math

val_a, val_b, val_c, discriminant, x = 0,0,0,0,0

val_a = int(input('Valor de a ?> '))
val_b = int(input('Valor de b ?> '))
val_c = int(input('Valor de c ?> '))

def solveEqucion (a,b,c):
    try:
        discriminant = val_b * val_b - 4 * a * c
        if discriminant < 0:
         return "La ecuacion no tiene solucion"
        elif discriminant == 0:
         x = -val_b / (2*a)
         return "La solucion unica es x = "+x
        else:
            x1 = (-val_b+math.sqrt(discriminant))/(2*a)
            x2 = (+val_b+math.sqrt(discriminant))/(2*a)
            x1 = round(x1, 2)
            x2 = round(x2, 2)
            return "Las soluciones son x1 ="+str(x1)+ " y x2 ="+str(x2)
    except ZeroDivisionError:
        return 'Error de Division por 0'

resultado = solveEqucion(val_a, val_b, val_c)
print(resultado)