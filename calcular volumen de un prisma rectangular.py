# zona de funciones
def capturar_datos():
    longitud = float(input("ingrese la longitud del prisma "))
    return longitud
def capturar_datos2():
    ancho = float(input("ingrese el ancho del prisma: "))
    return ancho
 
def capturar_altura():
    altura=float(input("ingrese altura del prisma:"))
    return altura

def calcular_volumen_prisma(longitud,ancho, altura):
    
    volumen = (longitud*ancho*altura)   
    return volumen
     
  
def mostrar_resultado(volumen):
    mensaje= ("El area del prisma rectangular es: " + str(volumen)+"cm³") 
    return mensaje
    

def mostrar_mensaje(mensaje):
    print(mensaje)
    

# zona principal del codigo
dato_longitud= capturar_datos()
dato_ancho=capturar_datos2()
dato_altura= capturar_altura()
dato_volumen= calcular_volumen_prisma(dato_longitud,dato_ancho, dato_altura)
mensaje=mostrar_resultado(dato_volumen)
mostrar_mensaje(mensaje)
 