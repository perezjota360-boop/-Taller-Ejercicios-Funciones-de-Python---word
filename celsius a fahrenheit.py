def capturar_datos():
    celsius = int(input("Ingrese grados celsius: "))
    return celsius

def calcular_celsius_(celsius):
    fahrenheit= ((celsius* 9/5)+32)   
    return fahrenheit  
  
def mostrar_resultado(fahrenheit):
    mensaje= ("Los celsius a fahrenheit son: "+ str (fahrenheit))
    return mensaje
    

def mostrar_mensaje(mensaje):
    print(mensaje)
    

# zona principal del codigo
dato_celsius= capturar_datos()
dato_fahrenheit= calcular_celsius_(dato_celsius)
mensaje=mostrar_resultado(dato_fahrenheit)
mostrar_mensaje(mensaje)
 