 # zona de funciones 
def capturar_datos():
    numero= int(input( "dijite el precio del producto: "))
    return numero

def analizar_datos(numero):
    descuento= numero * 0.1
    pago=numero-descuento
    return pago
def imprimir_datos(pago):
    mensaje = ("el presio a pagar con descuento del 10% es:  " + str(pago)+ "$")
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
    return mensaje

# zona de codigo principal
numero=capturar_datos()
dato_pago= analizar_datos(numero)
imprimir_datos(dato_pago)
imprimir_mensaje(imprimir_datos(dato_pago))
