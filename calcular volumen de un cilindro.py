# zona de funciones
def capturar_radio():
    radio = float(input("Ingrese el radio del cilindro: "))
    return radio

def capturar_altura():
    altura = float(input("ingrese la altura del cilindro"))
    return altura

def calcular_volumen_circulo(radio, altura):
    pi = 3.1416 
    volumen = (pi * radio ** 2 * altura)   
    return volumen  
def mostrar_resultado(volumen):
    mensaje= ("El volumen del circulo es: " + str(volumen))
    return mensaje
def mostrar_mensaje(mensaje):
    print(mensaje)
# zona principal del codigo
dato_radio= capturar_radio()
dato_altura=capturar_altura()
dato_volumen= calcular_volumen_circulo(dato_radio,dato_altura)
mensaje=mostrar_resultado(dato_volumen)
mostrar_mensaje(mensaje)
 