# zona de funciones
def capturar_datos():
    base = float(input("dijite la base del prisma triangular: "))
    return base
def capturar_datos2():
    ancho = float(input("ingrese el ancho del prisma triangular:"))
    return ancho
 
def capturar_altura():
    altura=float(input("ingrese altura del prisma triangular:"))
    return altura

def calcular_volumen(base, ancho ,altura):
    volumen=((base*ancho*altura)/2)
    return volumen
    
  
  
def mostrar_resultado(volumen):
    mensaje= ("El volumen del prisma triangular es: " + str(volumen)+"cm³") 
    return mensaje
    

def mostrar_mensaje(mensaje):
    print(mensaje)
    

# zona principal del codigo
base= capturar_datos()
ancho=capturar_datos2()
dato_altura= capturar_altura()
dato_volumen= calcular_volumen(base,ancho, dato_altura)
mensaje=mostrar_resultado(dato_volumen)
mostrar_mensaje(mensaje)
 