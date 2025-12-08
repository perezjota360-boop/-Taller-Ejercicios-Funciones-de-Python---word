#zona de codigo principal
def capturar_datos():
    Longitud = int(input("Ingrese la longitud de un lado: "))
    return Longitud

def calcular_volumen(longitud):
    volumen = (longitud*longitud*longitud) 
    return volumen

def mostrar_resultado(volumen):
    mensaje=("el volumen del cubo es:" + str(volumen)+"cm³")
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
    
    
    
  
#programa principal
dato_longitud = capturar_datos()
volumen = calcular_volumen(dato_longitud)
mensaje=mostrar_resultado(volumen)
imprimir_mensaje(mensaje)
