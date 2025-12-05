def capturar_datos():
    hora=int(input("dijite la hora:"))
    return hora   

def calcular_datos_(minutos):
    minutos= ((minutos)*60)
    return minutos
  
def mostrar_resultado(minutos):
    mensaje= ("la hora en minutos es: "+ str (minutos))
    return mensaje
    

def mostrar_mensaje(mensaje):
    print(mensaje)
    

# zona principal del codigo
dato_lt= capturar_datos()
dato_gl= calcular_datos_(dato_lt)
mensaje=mostrar_resultado(dato_gl)
mostrar_mensaje(mensaje)