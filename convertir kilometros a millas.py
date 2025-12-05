def capturar_datos():
    kilometro=int(input("dijite kilometros"))
    return kilometro

def calcular_datos_(kilometro):
    millas= ((kilometro)/1.609)
    return millas  
  
def mostrar_resultado(millas):
    mensaje= ("la convercion de kilometros a millas es: "+ str (millas))
    return mensaje
    

def mostrar_mensaje(mensaje):
    print(mensaje)
    

# zona principal del codigo
dato_kilometro= capturar_datos()
dato_millas= calcular_datos_(dato_kilometro)
mensaje=mostrar_resultado(dato_millas)
mostrar_mensaje(mensaje)
 