# zona de funciones
def capturar_datos():
    radio = float(input("Ingrese el radio del cono: "))
    return radio 
def capturar_altura():
    altura=float(input("ingrese altura del cono:"))
    return altura

def calcular_volumen_cono(radio,altura):
    pi = 3.1416 
    volumen = (1/3*pi * radio**2*altura )   
    return volumen  
     
  
def mostrar_resultado(volumen):
    mensaje= ("El volumen del cono es: " + str(volumen))
    return mensaje
    

def mostrar_mensaje(mensaje):
    print(mensaje)
    

# zona principal del codigo
dato_radio= capturar_datos()
dato_altura= capturar_altura()
dato_volumen= calcular_volumen_cono(dato_radio, dato_altura)
mensaje=mostrar_resultado(dato_volumen)
mostrar_mensaje(mensaje)
 
 