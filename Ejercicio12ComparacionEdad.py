PrimeraEdad = int(input('Introduce la primera edad > '))
SegundaEdad = int(input('Introduce la segundad edad > '))

if PrimeraEdad == SegundaEdad:
    print('Ambos tienen la misma edad')
elif PrimeraEdad > SegundaEdad:
    print('La primera edad es mayor que la segunda')
else:
    print('La segundad edad es mayor que la primera')