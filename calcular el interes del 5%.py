 # zona de funciones 
def capturar_datos():
    numero= int(input( "dijite la cantidad de dinero de la cuenta: "))
    return numero

def analizar_datos(numero):
    interes= numero * 0.05
    
    return interes
def imprimir_datos(interes):
    mensaje = ("el interes de la cuenta fue:  " + str(interes)+ "$")
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
    return mensaje

# zona de codigo principal
numero=capturar_datos()
dato_interes= analizar_datos(numero)
imprimir_datos(dato_interes)
imprimir_mensaje(imprimir_datos(dato_interes))
