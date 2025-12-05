# zona de funciones
def capturar_datos():
    longitud_base1 = float(input("ingrese la longitud de la primera base: "))
    return longitud_base1
def capturar_datos2():
    longitud_base2 = float(input("ingrese la longitud de la segunda base: "))
    return longitud_base2
 
def capturar_altura():
    altura=float(input("ingrese altura del trapecio:"))
    return altura

def calcular_area_trapecio(longitud_base1,longitud_base2, altura):
    
    area = ((longitud_base1+ longitud_base2)*(altura)/2)   
    return area  
     
  
def mostrar_resultado(area):
    mensaje= ("El area del trapecio es: " + str(area)+"cm²") 
    return mensaje
    

def mostrar_mensaje(mensaje):
    print(mensaje)
    

# zona principal del codigo
dato_longitud1= capturar_datos()
dato_longitud2=capturar_datos2()
dato_altura= capturar_altura()
dato_area= calcular_area_trapecio(dato_longitud1,dato_longitud2, dato_altura)
mensaje=mostrar_resultado(dato_area)
mostrar_mensaje(mensaje)
 