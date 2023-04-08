numeroIntroducido = 0
sumaDeNumeros = 0.0

print('Introduce un numero entero')
numeroIntroducido = int(input('> '))


sumaDeNumeros = numeroIntroducido * (numeroIntroducido+1) / 2
print("La suma desde 1 hasta "+str(numeroIntroducido)+ " es "+ str(sumaDeNumeros))