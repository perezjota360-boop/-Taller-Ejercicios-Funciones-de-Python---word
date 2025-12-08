 # zona de funciones 
def capturar_datos():
    numero_1= int(input( "dijite primer numero: "))
    return numero_1

def caturar_dato2():
    numero_2 = int(input( "dijite primer numero:"))
    return numero_2
def analizar_datos(numero_1, numero_2):
    resta = (numero_1 - numero_2)
    return resta
def imprimir_datos(resta):
    mensaje = (" la resta de los dos numeros es  "+ str (resta))
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
    return mensaje

# zona de codigo principal
dato_num1=capturar_datos()
dato_num2= caturar_dato2()
dato_resta= analizar_datos(dato_num1, dato_num2)
mensaje=imprimir_datos(dato_resta)
imprimir_mensaje(mensaje)
