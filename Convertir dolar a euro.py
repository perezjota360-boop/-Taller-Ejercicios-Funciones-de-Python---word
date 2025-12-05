def capturar_datos():
    dolar = int(input("Ingrese cantidad de dolares"))
    return dolar

def calcular_dolar_(dolar):
    euro= (dolar * 0.86)
    return euro  
  
def mostrar_resultado(euro):
    mensaje= ("la convercion de dolar a euro es: "+ str (euro))
    return mensaje
    

def mostrar_mensaje(mensaje):
    print(mensaje)
    

# zona principal del codigo
dato_dolar= capturar_datos()
dato_euro= calcular_dolar_(dato_dolar)
mensaje=mostrar_resultado(dato_euro)
mostrar_mensaje(mensaje)
 