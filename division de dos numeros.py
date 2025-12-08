 # zona de funciones 
def capturar_datos():
    numero_1= int(input( "dijite primer numero: "))
    return numero_1

def caturar_dato2():
    numero_2 = int(input( "dijite segundo numero:"))
    return numero_2
def analizar_datos(numero_1, numero_2):
    division = (numero_1 / numero_2)
    return division
def imprimir_datos(division):
    mensaje = (" la division de los dos numeros es  "+ str (division))
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
    return mensaje

# zona de codigo principal
dato_num1=capturar_datos()
dato_num2= caturar_dato2()
dato_division= analizar_datos(dato_num1, dato_num2)
mensaje=imprimir_datos(dato_division)
imprimir_mensaje(mensaje)