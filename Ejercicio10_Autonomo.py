
Pago_Semanal = 40
Pago_Mensual = 160
Relleno1 = '-'
Relleno2 = ' '
Cadena_Vacia = ''
ancho= 40
Formato_Menbrete = 'Calculadora FREELANCE (EUR)'
Pregunta_Horas = '>>>¿Precio de la hora a facturar?  '
Error_Formato = 'Solo se puedes poner numeros'

#Funciones para el calculo de valores 
def multiplicamosValores (Valor1, valor2):
    return Valor1 * valor2




print(Cadena_Vacia.center(ancho,Relleno1))
print(Formato_Menbrete.center(ancho,Relleno2))
print(Cadena_Vacia.center(ancho,Relleno1))

try:
    Euros_Por_Hora = float(input(Pregunta_Horas))

    #Llamar a la funcion para hacer el calculo
    resultado_semana = multiplicamosValores (Euros_Por_Hora, Pago_Semanal)
    resultato_mes = multiplicamosValores(Euros_Por_Hora, Pago_Mensual)
    print(Cadena_Vacia.center(ancho,Relleno1))
    print('>>> El pago Semanal es : %0.2f'%(resultado_semana))
    print('>>> El pago Mensual es : %0.2f'%(resultato_mes))
    
except ValueError:
    print(Error_Formato.center(ancho,Relleno1))
    print(Cadena_Vacia.center(ancho,Relleno1))












