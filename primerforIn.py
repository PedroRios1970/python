nombres =['Angles', 'Yolanda', 'Sonia', 'Estrella']

for nombre in nombres:
    print(nombre)

    """bucle for in range"""

base = int(input('> Introduce el nuemro a elevar: '))

for exponente in range(0,11):
    potencia = base ** exponente
    print(f"{base} elevado a {exponente} es {potencia}")