valor_a, valor_b, solucion = 0,0,0

valor_a = int(input('Introduce el valor de a >'))
valor_b = int(input('Introduce el valor de b >'))

if valor_b == 0:
    print('La ecuacion tiene multiples soluciones')
elif valor_a == 0:
    print('La ecuacion no tiene solucion')    
else: 
    solucion = -valor_b / valor_a
    print('La ecuacion vale %d'%(solucion))
    
