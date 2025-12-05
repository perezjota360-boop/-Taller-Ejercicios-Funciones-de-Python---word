# zona de funciones

def capturar_datos():
    numero_longitud = int(input("Ingrese un numero longitud: "))
    return numero_longitud
def capturar_datos2():
    numero_ancho = int(input("Ingrese un numero ancho: "))
    return numero_ancho

def analizar_area_rectangulo(longitud, ancho):
    area = longitud * ancho
    return area

def mostrar_resultado(area):
    mensaje= ("el area del rectangulo es: " + str(area))
    return mensaje
    
def imprimir_mensaje(mensaje):
    print(mensaje)
    return mensaje
    
#programa principal
longitud= capturar_datos()
ancho= capturar_datos2()
area = analizar_area_rectangulo(longitud, ancho)
mostrar_resultado(area)
imprimir_mensaje(mostrar_resultado(area))
  