def capturar_datos():
    libras=int(input("dijite las libras:"))
    return libras

def calcular_datos_(kilogramos):
    kilogramos= ((kilogramos)/2.205)
    return kilogramos
  
def mostrar_resultado(kilogramos):
    mensaje= ("la convercion de pulgadas a centimetros es: "+ str (kilogramos))
    return mensaje
    

def mostrar_mensaje(mensaje):
    print(mensaje)
    

# zona principal del codigo
dato_lb= capturar_datos()
dato_kg= calcular_datos_(dato_lb)
mensaje=mostrar_resultado(dato_kg)
mostrar_mensaje(mensaje)