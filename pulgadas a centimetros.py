def capturar_datos():
    pulgadas=int(input("dijite las pulgadas:"))
    return pulgadas

def calcular_datos_(pulgadas):
    centimetros= ((pulgadas)*2.54)
    return centimetros
  
def mostrar_resultado(centimetros):
    mensaje= ("la convercion de pulgadas a centimetros es: "+ str (centimetros))
    return mensaje
    

def mostrar_mensaje(mensaje):
    print(mensaje)
    

# zona principal del codigo
dato_pulgada= capturar_datos()
dato_cm= calcular_datos_(dato_pulgada)
mensaje=mostrar_resultado(dato_cm)
mostrar_mensaje(mensaje)