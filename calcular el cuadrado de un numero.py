 # zona de funciones 
def capturar_datos():
    numero= int(input( "dijite el numero: "))
    return numero
def analizar_datos(numero ):
    cuadrado = (numero*numero )
    return cuadrado
def imprimir_datos(numero,cuadrado):
    mensaje =("el resultado de :"+ str (numero)+"² es=" +str (cuadrado))
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
    return mensaje

# zona de codigo principal
dato_num1=capturar_datos()
dato_cuadrado= analizar_datos(dato_num1 )
mensaje=imprimir_datos(dato_num1, dato_cuadrado)
imprimir_mensaje(mensaje)
