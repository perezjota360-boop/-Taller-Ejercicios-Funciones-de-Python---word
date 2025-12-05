# zona de funciones
def capturar_datos():
    radio = float(input("Ingrese el radio del circulo: "))
    return radio 

def calcular_volumen_circulo(radio):
    pi = 3.1416 
    volumen = (4/3 * pi * radio ** 3  )   
    return volumen  
     
  
def mostrar_resultado(volumen):
    mensaje= ("El volumen del circulo es: " + str(volumen))
    return mensaje
    

def mostrar_mensaje(mensaje):
    print(mensaje)
    

# zona principal del codigo
dato_radio= capturar_datos()
dato_volumen= calcular_volumen_circulo(dato_radio)
mensaje=mostrar_resultado(dato_volumen)
mostrar_mensaje(mensaje)
 
 



