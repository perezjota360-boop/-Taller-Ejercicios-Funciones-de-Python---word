
# zona de funciones

def capturar_datos():
    numero_lado = int(input("Ingrese lado del cuadrado: "))
    return numero_lado

def analizar_area_rectangulo(numero_lado):
    area = numero_lado * numero_lado
    return area

def mostrar_resultado(area):
    mensaje= ("el area del rectangulo es: " + str(area))
    return mensaje
    
def imprimir_mensaje(mensaje):
    print(mensaje)
    return mensaje
    
#programa principal
lado_1= capturar_datos()
area = analizar_area_rectangulo(lado_1)
mostrar_resultado(area)
imprimir_mensaje(mostrar_resultado(area))