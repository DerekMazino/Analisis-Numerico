#Mantenimiento
def manejo_cadena_funcion(cadena):
    for i in cadena:
        if i is int:
            print('Numero: '+i)
manejo_cadena_funcion('2x^2-1')