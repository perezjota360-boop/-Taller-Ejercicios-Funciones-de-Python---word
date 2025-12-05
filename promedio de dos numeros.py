#zona de funciones
def capturar_datos():
    numero1=int(input("dijite primer numero"))
    return numero1
def capturar_dato2():
    numero2= int(input("dijite segundo numero"))
    return numero2
def analizar_datos(numero1,numero2):
    promedio = (numero1+numero2)/2
    return promedio
def mostrar_mensaje(promedio):
    mensaje = ("el predio de los dos numeros es:", (promedio))
    return mensaje
def imprimir_mensaje(mensaje):
    print (mensaje)
    return mensaje
#zona de condigo principal
dato_num1=capturar_datos()
dato_num2= capturar_dato2()
promedio= analizar_datos(dato_num1, dato_num2)
mostrar_mensaje(promedio)
imprimir_mensaje(mostrar_mensaje(promedio))