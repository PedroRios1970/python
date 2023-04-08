ancho= 40
Relleno1 = '-'
Relleno2 = ' '
Cadena_Vacia = ''

Mensaje_inicial = 'Radar de Velocidad'

Velocidad = 0.0
Frequencia0 = 2e-10
Frequencia1 = 2.0000004e-10

Formato_Respuesta = '>>> La velocidad es :%0.2f millas/hora.'

print(Cadena_Vacia.center(ancho,Relleno1))
print(Mensaje_inicial.center(ancho,Relleno2))

Velocidad = 6.685e8*(Frequencia1-Frequencia0)/(Frequencia1+Frequencia0)

print(Cadena_Vacia.center(ancho,Relleno1))
print(Formato_Respuesta.center(ancho,Relleno2) %(Velocidad))

print(Cadena_Vacia.center(ancho,Relleno1))