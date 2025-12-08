#zona de funciones
def capturar_area_base():
    area=float(input("dijite el area de la base:"))
    return area
def capturar_altura():
    altura=float(input("dijite la altura:"))
    return altura
def analizar_datos(area,altura):
    volumen=(( area * altura )/3)
    return volumen
def mostrar_mensaje(volumen):
    mensaje=("el volumen de la piramide es:" + str (volumen)+"cm³")
    return mensaje
def imprimir_mensaje(mensaje):
    print(mensaje)
    
#zona principal
dato_area=capturar_area_base()
dato_altura=capturar_altura()
volumen=analizar_datos(dato_area,dato_altura)
mensaje=mostrar_mensaje(volumen)
imprimir_mensaje(mensaje)    
