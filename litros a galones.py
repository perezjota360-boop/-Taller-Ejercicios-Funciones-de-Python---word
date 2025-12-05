def capturar_datos():
    litros=int(input("dijite los litros:"))
    return litros   

def calcular_datos_(galones):
    galones= ((galones)/3.785)
    return galones
  
def mostrar_resultado(galones):
    mensaje= ("la convercion de litros a galones  es: "+ str (galones))
    return mensaje
    

def mostrar_mensaje(mensaje):
    print(mensaje)
    

# zona principal del codigo
dato_lt= capturar_datos()
dato_gl= calcular_datos_(dato_lt)
mensaje=mostrar_resultado(dato_gl)
mostrar_mensaje(mensaje)